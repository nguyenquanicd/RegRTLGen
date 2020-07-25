#!/usr/bin/python3

import sys
import os
import string
import re
import time
import subprocess
import datetime
from sys import argv

# import library
script_path = os.path.dirname(__file__)
lib_path = script_path + "/../../lib/pyLib"
sys.path.append(lib_path)
from RegSpec import RegSpec

# in RegSpec[RegSpec_*]['Common_Config'] = {}
normal_variables = ["GenModuleName", "GenDataParam", "GenAddrParam", "GenAsyncParam", "GenSyncStageParam", "GenWProtParam", "GenSecParam", "GenWProtErrParam", "GenSecErrParam"]
normal_conditions = ["GenSyncReset", "GenAsyncReset", "GenWProtParam"]

# sub function
def normal_variables_replace(line):
  for variable in normal_variables:
    if variable in line:
      chosen_variable = re.escape("$" + variable) # variable -> \$variable
      line = re.sub(chosen_variable, RegSpec[spec_sheet]['Common_Config'][variable], line)
  return line

def process_loop (loop_type, lines_temp, line_print, reg_key, field_key, split_key):
  for line_temp in lines_temp:
    print_flag = 0
    first_element = line_temp.split()[0] if '$' in line_temp else "" # get first element of line_temp
    if '$GenNOT' in first_element:
      print_flag = 1 # default is print, met condition to not print
      first_element = first_element.replace('$GenNOT', '') # remove $GenNOT
      line_temp = line_temp.replace('$GenNOT', '') # remove $GenNOT
      line_temp = line_temp.replace(' ', '', 1) # remove 1 space at the  beginning
      
      list_condition = re.escape(first_element) # backslash: $first_element -> \$first_element
      line_temp = re.sub(list_condition, "", line_temp) # keep rtl code, remove list_condition
      match_condition = 0
      
      condition_array = first_element.replace('$', ' ').strip().split() # remove $, split into array
      if loop_type == 1:
        if '$GenPStrbIndex' in line_temp: # sample line got $GenPStrbIndex -> need to clone
          line_temp_total = ''
          for strobe_cnt in range (0, len([*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']])):
            strobe_key = [*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']][strobe_cnt]
            line_temp_each = line_temp
            line_temp_each = line_temp_each.replace('$GenPStrbIndex', str(strobe_cnt)) # clone strobe line from sample line
            for condition in condition_array:
              if condition in RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property'][strobe_key]:
                match_condition = 1
                break
            if match_condition == 0:
              line_temp_total += line_temp_each # strobe line can print out
            else:
              match_condition = 0 # reset check flag
          if line_temp_total != '':
            line_temp = line_temp_total # replace sample line after check each strobe
          else:
            print_flag = 0
        else:
          for condition in condition_array: # check all RW property
            for strobe_cnt in range (0, len([*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']])):
              strobe_key = [*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']][strobe_cnt]
              if condition in RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property'][strobe_key]:
                match_condition = 1
                break
            if match_condition == 1:
              print_flag = 0
              break
      else:
        if loop_type == 2:
          condition_check = RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['RW_Property']
        elif loop_type == 3:
          condition_check = RegSpec[spec_sheet][reg_key][field_key][split_key]['RW_Property']
        for condition in condition_array: # check all RW property
          if condition in condition_check:
            print_flag = 0
            break
    elif '$Gen' in first_element: 
      line_temp_backup = line_temp
      condition = re.escape(first_element) # backslash: $first_element -> \$first_element
      line_temp = re.sub(condition, "", line_temp) # keep rtl code, remove condition
      
      condition = condition.replace('\$','')     
      if condition in normal_conditions: # first element is normal condition for gen or not gen
        if RegSpec[spec_sheet]['Common_Config'][condition] == "0": # condition = 0, not gen
          continue
        else:
          line_temp = line_temp.replace(' ', '', 1) # remove 1 space at the  beginning
          print_flag = 1
      else:
        line_temp = line_temp_backup
        print_flag = 1
    elif '$' in first_element:
      list_condition = re.escape(first_element) # backslash: $first_element -> \$first_element
      line_temp = re.sub(list_condition, "", line_temp) # keep rtl code, remove list_condition
      line_temp = line_temp.replace(' ', '', 1) # remove 1 space at the  beginning
      match_condition = 0
      
      condition_array = first_element.replace('$', ' ').strip().split() # remove $, split into array
      if loop_type == 1:
        if '$GenPStrbIndex' in line_temp: # sample line got $GenPStrbIndex -> need to clone
          line_temp_total = ''
          for strobe_cnt in range (0, len([*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']])):
            strobe_key = [*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']][strobe_cnt]
            line_temp_each = line_temp
            line_temp_each = line_temp_each.replace('$GenPStrbIndex', str(strobe_cnt)) # clone strobe line from sample line
            for condition in condition_array:
              if condition in RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property'][strobe_key]:
                line_temp_total += line_temp_each # strobe line match condition to print out
                break
          if line_temp_total != '':
            line_temp = line_temp_total # replace sample line after check each strobe
            print_flag = 1  
        else:
          for condition in condition_array: # check all RW property
            for strobe_cnt in range (0, len([*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']])):
              strobe_key = [*RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property']][strobe_cnt]
              if condition in RegSpec[spec_sheet][reg_key]['Common_Config']['RW_Property'][strobe_key]:
                match_condition = 1
                break
            if match_condition == 1:
              print_flag = 1
              break
      else:
        if RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['GenRegField'] == 'RESERVED':
          print_flag = 1 if 'RESERVED' in condition_array else 0
        else:
          if loop_type == 2:
            condition_check = RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['RW_Property']
          elif loop_type == 3:
            condition_check = RegSpec[spec_sheet][reg_key][field_key][split_key]['RW_Property']
          for condition in condition_array: # check all RW property
            if condition in condition_check:
              print_flag = 1
              break
    else:
      print_flag = 1
      
    if print_flag == 1:
      # Reg Common_Config
      if '$GenRegName' in line_temp:
        line_temp = line_temp.replace('$GenRegName', RegSpec[spec_sheet][reg_key]['Common_Config']['GenRegName'])
      if '$GenRegOffsetParam' in line_temp:
        line_temp = line_temp.replace('$GenRegOffsetParam', RegSpec[spec_sheet][reg_key]['Common_Config']['GenRegOffsetParam'])
      # Field Common_Config
      if '$GenRegField' in line_temp:
        line_temp = line_temp.replace('$GenRegField', RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['GenRegField'])
      # BitRange Common_Config
      if '$GenPartialBitRange' in line_temp:
        line_temp = line_temp.replace('$GenPartialBitRange', RegSpec[spec_sheet][reg_key][field_key][split_key]['GenPartialBitRange'])
      if '$GenFieldReset' in line_temp:
        line_temp = line_temp.replace('$GenFieldReset', RegSpec[spec_sheet][reg_key][field_key][split_key]['GenFieldReset'])
      if '$GenPStrbIndex' in line_temp:
        line_temp = line_temp.replace('$GenPStrbIndex', RegSpec[spec_sheet][reg_key][field_key][split_key]['GenPStrbIndex']) 
      # Remain Other
      if '$GenFullBitRange' in line_temp:
        bit_max = int(max(RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['Ful_BitRange']))
        bit_min = int(min(RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['Ful_BitRange']))
        GenFullBitRange = str(bit_max) if bit_max == bit_min else str(bit_max) + ":" + str(bit_min)
        line_temp = line_temp.replace('$GenFullBitRange', GenFullBitRange)
      if '$Gen' in line_temp: # has normal variables to be replaced
        line_temp = normal_variables_replace(line_temp)
      line_print += line_temp
  return line_print
  
def process_print (process_type, lines, line_print, line_internal_print):
  loop_flag = 0
  for line in lines:
    if loop_flag != 0:
      if '$GenEndLoop' in line:
        loop_block.close()
        loop_block = open("loop_block_temp", "r")
        lines_temp = loop_block.readlines()
        
        if loop_flag == 3:
          for reg_cnt in range(1, len([*RegSpec[spec_sheet]])):
            reg_key = [*RegSpec[spec_sheet]][reg_cnt]
            for field_cnt in range(1, len([*RegSpec[spec_sheet][reg_key]])):
              field_key = [*RegSpec[spec_sheet][reg_key]][field_cnt]
              for split_cnt in range(1, len([*RegSpec[spec_sheet][reg_key][field_key]])):
                split_key = [*RegSpec[spec_sheet][reg_key][field_key]][split_cnt]
                line_print = process_loop(3, lines_temp, line_print, reg_key, field_key, split_key)
        elif loop_flag == 2:
          for reg_cnt in range(1, len([*RegSpec[spec_sheet]])):
            reg_key = [*RegSpec[spec_sheet]][reg_cnt]
            for field_cnt in range(1, len([*RegSpec[spec_sheet][reg_key]])):
              field_key = [*RegSpec[spec_sheet][reg_key]][field_cnt]
              line_print = process_loop(2, lines_temp, line_print, reg_key, field_key, "")
        elif loop_flag == 1:
          for reg_cnt in range(1, len([*RegSpec[spec_sheet]])):
            reg_key = [*RegSpec[spec_sheet]][reg_cnt]
            line_print = process_loop(1, lines_temp, line_print, reg_key, "", "")
        loop_flag = 0
        continue
      else:
        loop_block.write(line.replace('  ', '', 1)) # store line in loop_block, remove 2 space at the beginning
        continue
    else:
      if '$GenStartLoop$GenRegName$GenRegField$GenPartialBitRange' in line:
        loop_flag = 3
        loop_block = open("loop_block_temp", "w")
        continue
      elif '$GenStartLoop$GenRegName$GenRegField' in line:
        loop_flag = 2
        loop_block = open("loop_block_temp", "w")
        continue
      elif '$GenStartLoop$GenRegName' in line:
        loop_flag = 1
        loop_block = open("loop_block_temp", "w")
        continue
      elif process_type == "top":
        if '$GenUserHeader' in line:
          line = line.replace('$GenUserHeader', RegSpec['GenUserHeader'])
        elif '$GenInternalSignal' in line:
          line_print += line_internal_print
          continue
        elif '$Gen' in line: # line has condition/normal variables
          first_element = line.split()[0] # get first element of line
          if '$Gen' in first_element: # first element is normal condition for gen or not gen
            condition = re.escape(first_element) # backslash: $first_element -> \$first_element
            line = re.sub(condition, "", line) # keep rtl code, remove condition
            line = line.replace(' ', '', 1) # remove 1 space at the  beginning
            
            condition = condition.replace('\$','')
            if RegSpec[spec_sheet]['Common_Config'][condition] == "0": # condition = 0, not gen
              continue
          if '$GenRDataOR' in line: # special case for GenRDataOR
            GenRDataOR = " | ".join(RegSpec[spec_sheet]['Common_Config']['GenRDataOR'])
            line = line.replace('$GenRDataOR', GenRDataOR)
          if '$Gen' in line: # remain variables after check condition
            line = normal_variables_replace(line)
      else:
        if '$Gen' in line:
          line = normal_variables_replace(line)

    line_print += line
  return line_print
  
## Main process
for spec_cnt in range(1, len([*RegSpec])):
  # prepare output RTL
  spec_sheet = [*RegSpec][spec_cnt]
  output_path = script_path + "/../../output/" + RegSpec[spec_sheet]['Common_Config']['GenModuleName'] + ".sv"
  rtl_output = open(output_path, "w")
  
  # read sample InternalSignal RTL
  sample_path = script_path + "/../../lib/rtlLib/RegGen_ApbIf_InternalSignal.sv"
  rtl_sample = open(sample_path, "r")
  lines = rtl_sample.readlines()
  line_internal_print = process_print ("internal", lines, '', '')

  # read sample RTL
  sample_path = script_path + "/../../lib/rtlLib/RegGen_ApbIf.sv"
  rtl_sample = open(sample_path, "r")
  lines = rtl_sample.readlines()
  line_print = process_print ("top", lines, '', line_internal_print)
  
  # write all content to output RTL
  rtl_output.write(line_print)
  rtl_output.close()

# finish
os.remove('loop_block_temp')
open("finish_gen_rtl", 'w').close()
