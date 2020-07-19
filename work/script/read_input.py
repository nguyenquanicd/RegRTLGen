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
from openpyxl import load_workbook

## Main process
# load input spec
input_file = argv[1]
workbook = load_workbook(filename=input_file)

# create variable structure
RegSpec = open(script_path + "/RegSpec.py", "w")
RegSpec.write("RegSpec = {}\n") # new RegSpec

# CommonInfo sheet
CommonInfoSheet = workbook["CommonInfo"]
common_table_flag = 0
line = "\n"
for row in CommonInfoSheet.rows:
  if common_table_flag == 1:
    if row[0].value != 'x':
      for i in range(1, len(row)):
        if row[i].value != None:
          line += str(row[i].value) + ': ' 
      line = line.rstrip(": ") + "\n"
  elif row[0].value == 'GenEn': # begin of CommonInfo table
    common_table_flag = 1  
line = re.sub("\n", "\n//", line) # add // for comment in rtl code
RegSpec.write("RegSpec['GenUserHeader'] = \"\"\"%s\"\"\"\n" % line) # add RegSpec['GenUserHeader']

# Module specifications
for sheet in workbook:
  if re.search("^RegSpec_", sheet.title):
    # new RegSpec['RegSpec_*']
    content = "RegSpec['%s'] = {}\n" % sheet.title

    config_table_flag   = 0
    register_table_flag = 0
    register_count      = 0
    for row in sheet.rows:
      if config_table_flag == 1:
        config_name  = row[0].value
        config_value = row[1].value
        if config_name == None: # end of table
          config_table_flag = 0
          continue
        elif config_name == 'Property': # info row
          continue
        elif config_name == 'Gen':
          if config_value == 'Yes':
            gen_flag = 1
            continue
          else:
            gen_flag = 0 # skip spec, reduce time
            break
        elif config_name == 'Module name':
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenModuleName',     config_value)
        elif config_name == 'Interface':                                                                   
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'Interface',         config_value)
        elif config_name == 'DataWidth':                                                                   
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenDataParam',      config_value)
        elif config_name == 'AddrWidth':                                                                   
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenAddrParam',      config_value)
        elif config_name == 'Reset':
          GenAsyncReset = 1 if config_value == 'Async' else 0
          GenSyncReset  = 0 if config_value == 'Async' else 1
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenAsyncReset',     GenAsyncReset)
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenSyncReset',      GenSyncReset)
        elif config_name == 'Synchronization':
          GenAsyncParam = 1 if config_value == 'Async' else 0
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenAsyncParam',     GenAsyncParam)
        elif config_name == 'SynchronousStage':
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenSyncStageParam', config_value)
        elif config_name == 'Write protection':
          GenWProtParam = 1 if config_value == 'Yes' else 0
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenWProtParam',     GenWProtParam)
        elif config_name == 'Secure':
          GenSecParam   = 1 if config_value == 'Yes' else 0
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenSecParam',       GenSecParam)
        elif config_name == 'SlaveError':
          GenWProtErrParam = 1 if 'WProt' in config_value else 0
          GenSecErrParam   = 1 if 'Sec'   in config_value else 0
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenWProtErrParam',  GenWProtErrParam)
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenSecErrParam',    GenSecErrParam)
      elif register_table_flag == 1:
        bit_range = row[0].value
        if bit_range == None: # end of table
          register_table_flag = 0
          continue
        elif bit_range == 'Bit': # info row
          continue
        else:
          reset_value      = row[1].value
          GenRegField      = row[2].value
          RW_property      = row[3].value
          Field_Desciption = row[4].value
          if GenRegField not in temp_register: # new GenRegField
            temp_register[GenRegField] = {}
            register_field_count += 1
            register_field_count_current = register_field_count
            register_field_name = "Register_Field_No_" + str(register_field_count_current)
            register_field_split_count = 0
            
            # new RegSpec['RegSpec_*']['<register>']['<register_field>']
            content += "RegSpec['%s']['%s']['%s'] = {}\n" % (sheet.title, register_name, register_field_name)
  
            # new RegSpec['RegSpec_*']['<register>']['<register_field>']['Common_Config']
            content += "RegSpec['%s']['%s']['%s']['Common_Config'] = {}\n" % (sheet.title, register_name, register_field_name)
          
            # GenRegField, Field_Desciption, RW_Property, & Ful_BitRange
            content += "RegSpec['%s']['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, register_field_name, 'GenRegField', GenRegField)
            content += "RegSpec['%s']['%s']['%s']['Common_Config']['%s'] = \"\"\"%s\"\"\"\n" % (sheet.title, register_name, register_field_name, 'Field_Desciption', Field_Desciption)
            content += "RegSpec['%s']['%s']['%s']['Common_Config']['%s'] = []\n" % (sheet.title, register_name, register_field_name, 'RW_Property')
            content += "RegSpec['%s']['%s']['%s']['Common_Config']['%s'] = []\n" % (sheet.title, register_name, register_field_name, 'Ful_BitRange')
          else: # continue for GenRegField from previous split
            register_field_count_current = temp_register[GenRegField]['field_count']
            register_field_name = "Register_Field_No_" + str(register_field_count_current)
            register_field_split_count = temp_register[GenRegField]['split_count']
            
          # split property of GenRegField
          bit_range_list = str(bit_range).split('/')
          reset_value_list = str(reset_value).split('/')
          RW_property_list = str(RW_property).split('/')
          
          # correct len of reset_value_list, in cased user not define fully
          if len(reset_value_list) < len(bit_range_list):
            for i in range(len(reset_value_list), len(bit_range_list)):
              reset_value_list.append("'0")
          
          for i in range(0, len(bit_range_list)):
            register_field_split_count += 1
            register_field_split_name = "Register_Field_Split_No_" + str(register_field_split_count)
            
            
            # new RegSpec['RegSpec_*']['<register>']['<register_field>']['<register_field_split>']
            content += "RegSpec['%s']['%s']['%s']['%s'] = {}\n" % (sheet.title, register_name, register_field_name, register_field_split_name)
            
            # GenPartialBitRange & GenFieldReset of BitRange
            content += "RegSpec['%s']['%s']['%s']['%s']['%s'] = \"%s\"\n" % (sheet.title, register_name, register_field_name, register_field_split_name, 'GenPartialBitRange', bit_range_list[i])
            content += "RegSpec['%s']['%s']['%s']['%s']['%s'] = \"%s\"\n" % (sheet.title, register_name, register_field_name, register_field_split_name, 'GenFieldReset', reset_value_list[i])
            
            # estimate Strobe_Index
            bit_range_list_array = str(bit_range_list[i]).split(':')
            bit_max = int(max(bit_range_list_array))
            bit_min = int(min(bit_range_list_array))
            strobe_index = int(bit_max/8)
            
            # Strobe_Index
            content += "RegSpec['%s']['%s']['%s']['%s']['%s'] = \"%s\"\n" % (sheet.title, register_name, register_field_name, register_field_split_name, 'GenPStrbIndex', strobe_index)
            
            # Ful_BitRange
            content += "RegSpec['%s']['%s']['%s']['Common_Config']['%s'].append(%d)\n" % (sheet.title, register_name, register_field_name, 'Ful_BitRange', bit_max)
            content += "RegSpec['%s']['%s']['%s']['Common_Config']['%s'].append(%d)\n" % (sheet.title, register_name, register_field_name, 'Ful_BitRange', bit_min)
            
            # RW_Property
            content += "RegSpec['%s']['%s']['%s']['%s']['%s'] = []\n" % (sheet.title, register_name, register_field_name, register_field_split_name, 'RW_Property')
            for i in range(0, len(RW_property_list)):
              RW_property = RW_property_list[i]
              content += "RegSpec['%s']['%s']['%s']['%s']['%s'].append(\"%s\")\n" % (sheet.title, register_name, register_field_name, register_field_split_name, 'RW_Property', RW_property)
              # whole field RW_Property
              content += "RegSpec['%s']['%s']['%s']['Common_Config']['%s'].append(\"%s\")\n" % (sheet.title, register_name, register_field_name, 'RW_Property', RW_property)
              # whole register RW_Property
              strobe_config = "Strobe_" + str(strobe_index)
              content += "RegSpec['%s']['%s']['Common_Config']['%s']['%s'].append(\"%s\")\n" % (sheet.title, register_name, 'RW_Property', strobe_config, RW_property)
          
          temp_register[GenRegField]['field_count'] = register_field_count_current
          temp_register[GenRegField]['split_count'] = register_field_split_count
      elif row[0].value == 'Table':
        table_name = row[1].value
        if table_name == 'RegFile': # begin of config table
          config_table_flag = 1
          # new RegSpec['RegSpec_*']['Common_Config'] 
          content += "RegSpec['%s']['Common_Config'] = {}\n" % sheet.title
          
          # GenRDataOR
          content += "RegSpec['%s']['Common_Config']['GenRDataOR'] = []\n" % sheet.title
        elif table_name == 'Gen':  # begin of register tables (Gen enable)
          register_table_flag = 1
          register_count += 1
          register_name = "Register_No_" + str(register_count)
          register_field_count = 0
          temp_register = {}
          
          # new RegSpec['RegSpec_*']['<register>']
          content += "RegSpec['%s']['%s'] = {}\n" % (sheet.title, register_name)

          # new RegSpec['RegSpec_*']['<register>']['Common_Config']
          content += "RegSpec['%s']['%s']['Common_Config'] = {}\n" % (sheet.title, register_name)
          
          # GenRegName, Register_Description & GenRegOffsetParam
          GenRegName           = row[2].value
          Register_Description = row[3].value
          GenRegOffsetParam     = row[4].value
          content += "RegSpec['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, 'GenRegName',           GenRegName)
          content += "RegSpec['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, 'Register_Description', Register_Description)
          content += "RegSpec['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, 'GenRegOffsetParam',     GenRegOffsetParam)
          
          # add for GenRDataOR
          content += "RegSpec['%s']['Common_Config']['GenRDataOR'].append(\"%s_rvalue\")\n" % (sheet.title, GenRegName)
          
          # new list of RW_Property
          content += "RegSpec['%s']['%s']['Common_Config']['%s'] = {}\n" % (sheet.title, register_name, 'RW_Property')
          for i in range(0, 4):
            strobe_config = "Strobe_" + str(i)
            content += "RegSpec['%s']['%s']['Common_Config']['%s']['%s'] = []\n" % (sheet.title, register_name, 'RW_Property', strobe_config)
    if gen_flag == 1:
      RegSpec.write(content)

# finish
RegSpec.close()   
open("finish_read_input", 'w').close()
