#!/usr/bin/python3.8

import sys
import os
import string
import re
import time
import subprocess
import datetime
import shutil
from sys import argv

# import library
script_path = os.path.dirname(__file__)
lib_path = script_path + "/../../lib/pyLib"
sys.path.append(lib_path)
from RegSpec import RegSpec

internal_conditions = ["RWI", "RO", "ROC", "ROS"]
pulse_conditions    = ["POW", "POW0", "POW1"]

## Main process
for spec_cnt in range(1, len([*RegSpec])):
  spec_sheet  = [*RegSpec][spec_cnt]
  module_name = RegSpec[spec_sheet]['Common_Config']['GenModuleName']
  
  # copy UVM env
  input_path  = script_path + "/../../lib/uvmLib"
  output_path = script_path + "/../../output/" + module_name + "_uvm"
  shutil.copytree(input_path, output_path, dirs_exist_ok=True)
  
  # copy DUT
  RTL_path = script_path + "/../../output/" + module_name + ".sv"
  DUT_path = output_path + "/dut/"
  shutil.copy2(RTL_path, DUT_path)

  Interface_content          = ""
  Transaction_content        = ""
  Driver_content_default     = "      default : begin \n"
  Monitor_content_create     = ""
  Monitor_content_regist     = ""
  Monitor_content_collect    = ""
  Monitor_content_task       = ""
  Scoreboard_content_declare = ""
  Scoreboard_content_var     = ""
  Scoreboard_content_create  = ""
  Scoreboard_content_regist  = ""
  Scoreboard_content_func    = ""
  Env_content_connect        = ""
  Top_content_connect        = ""
  
  for reg_cnt in range(1, len([*RegSpec[spec_sheet]])):
    reg_key = [*RegSpec[spec_sheet]][reg_cnt]
    GenRegName        = RegSpec[spec_sheet][reg_key]['Common_Config']['GenRegName']
    GenRegOffsetParam = RegSpec[spec_sheet][reg_key]['Common_Config']['GenRegOffsetParam']
    
    # Monitor common content
    Monitor_content_create  += f"  {GenRegName}_monitor co_{GenRegName}_monitor; \n"
    Monitor_content_create  += f"  uvm_analysis_port #({GenRegName}_monitor) ap_{GenRegName}_monitor; \n"
    Monitor_content_regist  += f"    co_{GenRegName}_monitor = {GenRegName}_monitor::type_id::create(\"co_{GenRegName}_monitor\",this); \n"
    Monitor_content_regist  += f"    ap_{GenRegName}_monitor = new(\"ap_{GenRegName}_monitor\", this);	\n"
    Monitor_content_collect += f"      {GenRegName}_collect_data(); \n"
    
    # Scoreboard common content
    Scoreboard_content_declare  += f"`uvm_analysis_imp_decl(_frmMonitor_{GenRegName}) \n"
    Scoreboard_content_create   += f"  uvm_analysis_imp_frmMonitor_{GenRegName} #({GenRegName}_monitor, RegRTL_Scoreboard) aimp_frmMonitor_{GenRegName}; \n"
    Scoreboard_content_regist   += f"    aimp_frmMonitor_{GenRegName} = new(\"aimp_frmMonitor_{GenRegName}\", this); \n"
    Scoreboard_content_assign   = ""
    
    # Env common connect
    Env_content_connect += f"    co_RegConfig_Agent.co_RegConfig_Monitor.ap_{GenRegName}_monitor.connect(co_RegRTL_Scoreboard.aimp_frmMonitor_{GenRegName}); \n"
    
    # output logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_reg,
    Interface_content         += f"  logic [31:0] {GenRegName}_reg; \n"
    Transaction_content_create = f"  rand logic [31:0] {GenRegName}_reg; \n"
    Transaction_content_regist = f"    `uvm_field_int({GenRegName}_reg, UVM_ALL_ON) \n"
    Monitor_content_change     = f"vif_RegConfig_IF.{GenRegName}_reg \n"  
    Monitor_content_assign     = f"        co_{GenRegName}_monitor.{GenRegName}_reg = vif_RegConfig_IF.{GenRegName}_reg; \n"
    Scoreboard_content_var    += f"  logic [31:0] {GenRegName}_reg; \n"
    Scoreboard_content_assign += f"    {GenRegName}_reg = {GenRegName}_Trans.{GenRegName}_reg; \n"
    Top_content_connect       += f"    .{GenRegName}_reg(vRegConfig_Interface_Top.{GenRegName}_reg), \n"
    
    # output logic $GenRegName_read_en
    for strobe_cnt in range (0, len([*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']])):
      strobe_key = [*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']][strobe_cnt]
      if 'POR' in RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property'][strobe_key]:
        Interface_content          += f"  logic {GenRegName}_read_en; \n"
        Transaction_content_create += f"  rand logic {GenRegName}_read_en; \n"
        Transaction_content_regist += f"    `uvm_field_int({GenRegName}_read_en, UVM_ALL_ON) \n"
        Monitor_content_change     += f"        or vif_RegConfig_IF.{GenRegName}_read_en \n"  
        Monitor_content_assign     += f"        co_{GenRegName}_monitor.{GenRegName}_read_en = vif_RegConfig_IF.{GenRegName}_read_en; \n"
        Scoreboard_content_var     += f"  logic {GenRegName}_read_en; \n"
        Scoreboard_content_assign  += f"    {GenRegName}_read_en = {GenRegName}_Trans.{GenRegName}_read_en; \n"
        Top_content_connect        += f"    .{GenRegName}_read_en(vRegConfig_Interface_Top.{GenRegName}_read_en), \n"
        break
    
    # output logic [REGGEN_STRB_WIDTH-1:0] $GenRegName_byte_we
    byte_we_match = 0
    for strobe_cnt in range (0, len([*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']])):
      strobe_key = [*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']][strobe_cnt]
      for condition in pulse_conditions:
        if condition in RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property'][strobe_key]:
          byte_we_match = 1
          break
      if byte_we_match == 1:
        Interface_content          += f"  logic [3:0] {GenRegName}_byte_we; \n"
        Transaction_content_create += f"  rand logic [3:0] {GenRegName}_byte_we; \n"
        Transaction_content_regist += f"    `uvm_field_int({GenRegName}_byte_we, UVM_ALL_ON) \n"
        Monitor_content_change     += f"        or vif_RegConfig_IF.{GenRegName}_byte_we \n"  
        Monitor_content_assign     += f"        co_{GenRegName}_monitor.{GenRegName}_byte_we = vif_RegConfig_IF.{GenRegName}_byte_we; \n"
        Scoreboard_content_var     += f"  logic [3:0] {GenRegName}_byte_we; \n"
        Scoreboard_content_assign  += f"    {GenRegName}_byte_we = {GenRegName}_Trans.{GenRegName}_byte_we; \n"
        Top_content_connect        += f"    .{GenRegName}_byte_we(vRegConfig_Interface_Top.{GenRegName}_byte_we), \n"
        break
        
    # input logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_ivalue
    ivalue_match = 0
    for strobe_cnt in range (0, len([*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']])):
      strobe_key = [*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']][strobe_cnt]
      for condition in internal_conditions:
        if condition in RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property'][strobe_key]:
          ivalue_match = 1
          break
      if ivalue_match == 1:
        Interface_content          += f"  logic [31:0] {GenRegName}_ivalue; \n"
        Transaction_content_create += f"  rand logic [31:0] {GenRegName}_ivalue; \n"
        Transaction_content_regist += f"    `uvm_field_int({GenRegName}_ivalue, UVM_ALL_ON) \n"
        Driver_content_case         = f"      {GenRegOffsetParam} : begin \n"
        Driver_content_case        += f"        v_RegConfig_IF.{GenRegName}_ivalue = Config_Trans.Data; \n"
        Driver_content_default     += f"        v_RegConfig_IF.{GenRegName}_ivalue = 'h0; \n"
        Monitor_content_change     += f"        or vif_RegConfig_IF.{GenRegName}_ivalue \n"  
        Monitor_content_assign     += f"        co_{GenRegName}_monitor.{GenRegName}_ivalue = vif_RegConfig_IF.{GenRegName}_ivalue; \n"
        Scoreboard_content_var     += f"  logic [31:0] {GenRegName}_ivalue; \n"
        Scoreboard_content_assign  += f"    {GenRegName}_ivalue = {GenRegName}_Trans.{GenRegName}_ivalue; \n"
        Top_content_connect        += f"    .{GenRegName}_ivalue(vRegConfig_Interface_Top.{GenRegName}_ivalue), \n"
        break  

    for field_cnt in range(1, len([*RegSpec[spec_sheet][reg_key]])):
      field_key = [*RegSpec[spec_sheet][reg_key]][field_cnt]
      GenRegField     = RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['GenRegField']
      bit_max = int(max(RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['Ful_BitRange']))
      bit_min = int(min(RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['Ful_BitRange']))
      if bit_max == bit_min:
        GenFullBitRange = f"Driver_IWE[{bit_max}]"
      else:
        GenFullBitRange = "|Driver_IWE[{}:{}]".format(bit_max, bit_min)
        
      # input logic $GenRegName_$GenRegField_iwe
      for condition in internal_conditions:
        if condition in RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['RW_Property']:
          Interface_content          += f"  logic {GenRegName}_{GenRegField}_iwe; \n"
          Transaction_content_create += f"  rand logic {GenRegName}_{GenRegField}_iwe; \n"
          Transaction_content_regist += f"    `uvm_field_int({GenRegName}_{GenRegField}_iwe, UVM_ALL_ON) \n"
          Driver_content_case        += f"        v_RegConfig_IF.{GenRegName}_{GenRegField}_iwe = {GenFullBitRange}; \n"
          Driver_content_default     += f"        v_RegConfig_IF.{GenRegName}_{GenRegField}_iwe = 'h0; \n"
          Monitor_content_change     += f"        or vif_RegConfig_IF.{GenRegName}_{GenRegField}_iwe \n"  
          Monitor_content_assign     += f"        co_{GenRegName}_monitor.{GenRegName}_{GenRegField}_iwe = vif_RegConfig_IF.{GenRegName}_{GenRegField}_iwe; \n"
          Scoreboard_content_var     += f"  logic {GenRegName}_{GenRegField}_iwe; \n"
          Scoreboard_content_assign  += f"    {GenRegName}_{GenRegField}_iwe = {GenRegName}_Trans.{GenRegName}_{GenRegField}_iwe; \n"
          Top_content_connect        += f"    .{GenRegName}_{GenRegField}_iwe(vRegConfig_Interface_Top.{GenRegName}_{GenRegField}_iwe), \n"
          break

      for split_cnt in range(1, len([*RegSpec[spec_sheet][reg_key][field_key]])):
        split_key = [*RegSpec[spec_sheet][reg_key][field_key]][split_cnt]
        GenPStrbIndex = RegSpec[spec_sheet][reg_key][field_key][split_key]['GenPStrbIndex']
        
        # output logic $GenRegName_$GenRegField_$GenPStrbIndex_w1
        if 'POW1' in RegSpec[spec_sheet][reg_key][field_key][split_key]['RW_Property']:
          Interface_content          += f"  logic {GenRegName}_{GenRegField}_{GenPStrbIndex}_w1; \n"
          Transaction_content_create += f"  rand logic {GenRegName}_{GenRegField}_{GenPStrbIndex}_w1; \n"
          Transaction_content_regist += f"    `uvm_field_int({GenRegName}_{GenRegField}_{GenPStrbIndex}_w1, UVM_ALL_ON) \n"
          Monitor_content_change     += f"        or vif_RegConfig_IF.{GenRegName}_{GenRegField}_{GenPStrbIndex}_w1 \n"  
          Monitor_content_assign     += f"        co_{GenRegName}_monitor.{GenRegName}_{GenRegField}_{GenPStrbIndex}_w1 = vif_RegConfig_IF.{GenRegName}_{GenRegField}_{GenPStrbIndex}_w1; \n"
          Scoreboard_content_var     += f"  logic {GenRegName}_{GenRegField}_{GenPStrbIndex}_w1; \n"
          Scoreboard_content_assign  += f"    {GenRegName}_{GenRegField}_{GenPStrbIndex}_w1 = {GenRegName}_Trans.{GenRegName}_{GenRegField}_{GenPStrbIndex}_w1; \n"
          Top_content_connect        += f"    .{GenRegName}_{GenRegField}_{GenPStrbIndex}_w1(vRegConfig_Interface_Top.{GenRegName}_{GenRegField}_{GenPStrbIndex}_w1), \n"
        # output logic $GenRegName_$GenRegField_$GenPStrbIndex_w0
        if 'POW0' in RegSpec[spec_sheet][reg_key][field_key][split_key]['RW_Property']:
          Interface_content          += f"  logic {GenRegName}_{GenRegField}_{GenPStrbIndex}_w0; \n"
          Transaction_content_create += f"  rand logic {GenRegName}_{GenRegField}_{GenPStrbIndex}_w0; \n"
          Transaction_content_regist += f"    `uvm_field_int({GenRegName}_{GenRegField}_{GenPStrbIndex}_w0, UVM_ALL_ON) \n"
          Monitor_content_change     += f"        or vif_RegConfig_IF.{GenRegName}_{GenRegField}_{GenPStrbIndex}_w0 \n"  
          Monitor_content_assign     += f"        co_{GenRegName}_monitor.{GenRegName}_{GenRegField}_{GenPStrbIndex}_w0 = vif_RegConfig_IF.{GenRegName}_{GenRegField}_{GenPStrbIndex}_w0; \n"
          Scoreboard_content_var     += f"  logic {GenRegName}_{GenRegField}_{GenPStrbIndex}_w0; \n"
          Scoreboard_content_assign  += f"    {GenRegName}_{GenRegField}_{GenPStrbIndex}_w0 = {GenRegName}_Trans.{GenRegName}_{GenRegField}_{GenPStrbIndex}_w0; \n"
          Top_content_connect        += f"    .{GenRegName}_{GenRegField}_{GenPStrbIndex}_w0(vRegConfig_Interface_Top.{GenRegName}_{GenRegField}_{GenPStrbIndex}_w0), \n"
          
    Transaction_content += f"""
class {GenRegName}_monitor extends uvm_sequence_item;
  
{Transaction_content_create}
  `uvm_object_utils_begin({GenRegName}_monitor)
{Transaction_content_regist}
  `uvm_object_utils_end
  
  function new(string name = "{GenRegName}_monitor");
    super.new(name);
  endfunction: new

endclass: {GenRegName}_monitor
"""
    
    Monitor_content_task += f"""
  virtual task {GenRegName}_collect_data();
    while(1) begin
      @({Monitor_content_change}
      ) begin
        #1ps
{Monitor_content_assign}
        ap_{GenRegName}_monitor.write(co_{GenRegName}_monitor);
      end
    end
  endtask: {GenRegName}_collect_data
"""
    
    Scoreboard_content_func += f"""
  function void write_frmMonitor_{GenRegName}({GenRegName}_monitor {GenRegName}_Trans);
{Scoreboard_content_assign}
  endfunction
"""
    
    if ivalue_match == 1:      
      Driver_content_case += "      end \n"
  Driver_content_default  += "      end \n"
  
  # Create: RegConfig_Interface.sv
  sample_path = input_path + "/uvm_comp/RegConfig_Interface.sv"
  uvm_sample = open(sample_path, "r")
  lines = uvm_sample.readlines()
  line_print = ""
  for line in lines:
    if '// Content' in line:
      line_print += Interface_content
    else:
      line_print += line
  final_path = output_path + "/uvm_comp/RegConfig_Interface.sv"
  uvm_final = open(final_path, "w")
  uvm_final.write(line_print)
  uvm_final.close()
  
  # Create: RegConfig_Transaction.sv
  sample_path = input_path + "/uvm_comp/RegConfig_Transaction.sv"
  uvm_sample = open(sample_path, "r")
  lines = uvm_sample.readlines()
  line_print = ""
  for line in lines:
    if '// Content' in line:
      line_print += Transaction_content
    else:
      line_print += line
  final_path = output_path + "/uvm_comp/RegConfig_Transaction.sv"
  uvm_final = open(final_path, "w")
  uvm_final.write(line_print)
  uvm_final.close()
  
  # Create: RegConfig_Driver.sv
  sample_path = input_path + "/uvm_comp/RegConfig_Driver.sv"
  uvm_sample = open(sample_path, "r")
  lines = uvm_sample.readlines()
  line_print = ""
  for line in lines:
    if '// Content' in line:
      line_print += Driver_content_case
      line_print += Driver_content_default
    else:
      line_print += line
  final_path = output_path + "/uvm_comp/RegConfig_Driver.sv"
  uvm_final = open(final_path, "w")
  uvm_final.write(line_print)
  uvm_final.close()
  
  # Create: RegConfig_Monitor.sv
  sample_path = input_path + "/uvm_comp/RegConfig_Monitor.sv"
  uvm_sample = open(sample_path, "r")
  lines = uvm_sample.readlines()
  line_print = ""
  for line in lines:
    if '// Content create' in line:
      line_print += Monitor_content_create
    elif '// Content regist' in line:
      line_print += Monitor_content_regist
    elif '// Content collect' in line:
      line_print += Monitor_content_collect
    elif '// Content task' in line:
      line_print += Monitor_content_task
    else:
      line_print += line
  final_path = output_path + "/uvm_comp/RegConfig_Monitor.sv"
  uvm_final = open(final_path, "w")
  uvm_final.write(line_print)
  uvm_final.close()
  
  # Create: RegRTL_Scoreboard.sv
  sample_path = input_path + "/uvm_comp/RegRTL_Scoreboard.sv"
  uvm_sample = open(sample_path, "r")
  lines = uvm_sample.readlines()
  line_print = ""
  for line in lines:
    if '// Content declare' in line:
      line_print += Scoreboard_content_declare
    elif '// Content internal variables' in line:
      line_print += Scoreboard_content_var
    elif '// Content create' in line:
      line_print += Scoreboard_content_create
    elif '// Content regist' in line:
      line_print += Scoreboard_content_regist
    elif '// Content function' in line:
      line_print += Scoreboard_content_func
    else:
      line_print += line
  final_path = output_path + "/uvm_comp/RegRTL_Scoreboard.sv"
  uvm_final = open(final_path, "w")
  uvm_final.write(line_print)
  uvm_final.close()
  
  # Create: RegRTL_Env.sv
  sample_path = input_path + "/uvm_comp/RegRTL_Env.sv"
  uvm_sample = open(sample_path, "r")
  lines = uvm_sample.readlines()
  line_print = ""
  for line in lines:
    if '// Content connect' in line:
      line_print += Env_content_connect
    else:
      line_print += line
  final_path = output_path + "/uvm_comp/RegRTL_Env.sv"
  uvm_final = open(final_path, "w")
  uvm_final.write(line_print)
  uvm_final.close()
  
  # Create: RegRTL_Top.sv
  sample_path = input_path + "/sim/RegRTL_Top.sv"
  uvm_sample = open(sample_path, "r")
  lines = uvm_sample.readlines()
  line_print = ""
  for line in lines:
    if '  dut_top dut_top(' in line:
      line_print += f"  {module_name} {module_name}( \n"
    elif '//RegConfig Interface' in line:
      line_print += line
      line_print += Top_content_connect
    else:
      line_print += line
  final_path = output_path + "/sim/RegRTL_Top.sv"
  uvm_final = open(final_path, "w")
  uvm_final.write(line_print)
  uvm_final.close()

# finish
open("finish_gen_uvm", 'w').close()
