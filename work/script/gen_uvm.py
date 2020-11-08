#!/usr/bin/python3

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
pulse_conditions = ["POW", "POW0", "POW1"]

## Main process
for spec_cnt in range(1, len([*RegSpec])):
  spec_sheet = [*RegSpec][spec_cnt]
  input_path = script_path + "/../../lib/uvmLib"
  output_path = script_path + "/../../output/" + RegSpec[spec_sheet]['Common_Config']['GenModuleName'] + "_uvm"
  shutil.copytree(input_path, output_path, dirs_exist_ok=True)
  
  # RegConfig_Interface.sv
  RegConfig_Interface_content  = ""
  
  for reg_cnt in range(1, len([*RegSpec[spec_sheet]])):
    reg_key = [*RegSpec[spec_sheet]][reg_cnt]
    GenRegName = RegSpec[spec_sheet][reg_key]['Common_Config']['GenRegName']
    
    # output logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_reg,
    RegConfig_Interface_content += "  logic [31:0] " + GenRegName + "_reg; \n"
    
    # output logic $GenRegName_read_en
    for strobe_cnt in range (0, len([*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']])):
      strobe_key = [*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']][strobe_cnt]
      if 'POR' in RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property'][strobe_key]:
        RegConfig_Interface_content += "  logic " + GenRegName + "_read_en; \n"
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
        RegConfig_Interface_content += "  logic [3:0] " + GenRegName + "_byte_we; \n"
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
        RegConfig_Interface_content += "  logic [31:0] " + GenRegName + "_ivalue; \n"
        break  

    for field_cnt in range(1, len([*RegSpec[spec_sheet][reg_key]])):
      field_key = [*RegSpec[spec_sheet][reg_key]][field_cnt]
      GenRegField = RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['GenRegField']
      
      # input logic $GenRegName_$GenRegField_iwe
      for condition in internal_conditions:
        if condition in RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['RW_Property']:
          RegConfig_Interface_content += "  logic " + GenRegName + "_" + GenRegField + "_iwe; \n"
          break

      for split_cnt in range(1, len([*RegSpec[spec_sheet][reg_key][field_key]])):
        split_key = [*RegSpec[spec_sheet][reg_key][field_key]][split_cnt]
        GenPStrbIndex = RegSpec[spec_sheet][reg_key][field_key][split_key]['GenPStrbIndex']
        
        # output logic $GenRegName_$GenRegField_$GenPStrbIndex_w1
        if 'POW1' in RegSpec[spec_sheet][reg_key][field_key][split_key]['RW_Property']:
          RegConfig_Interface_content += "  logic " + GenRegName + "_" + GenRegField + "_" + GenPStrbIndex +  "_w1; \n"
        # output logic $GenRegName_$GenRegField_$GenPStrbIndex_w0
        if 'POW0' in RegSpec[spec_sheet][reg_key][field_key][split_key]['RW_Property']:
          RegConfig_Interface_content += "  logic " + GenRegName + "_" + GenRegField + "_" + GenPStrbIndex +  "_w0; \n"
  
  # Create: RegConfig_Driver.sv
  final_path = output_path + "/uvm_comp/RegConfig_Interface.sv"
  uvm_final = open(final_path, "w")
  line_print = ""
  # read sample
  sample_path = input_path + "/uvm_comp/RegConfig_Interface.sv"
  uvm_sample = open(sample_path, "r")
  lines = uvm_sample.readlines()
  for line in lines:
    if '// Content' in line:
      line_print += RegConfig_Interface_content
    else:
      line_print += line
  # write all content
  uvm_final.write(line_print)
  uvm_final.close()

# finish
open("finish_gen_uvm", 'w').close()
