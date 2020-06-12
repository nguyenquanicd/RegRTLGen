#!/usr/bin/python

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
  else:
    if row[0].value == 'GenEn': # begin of CommonInfo table
      common_table_flag = 1  
line = re.sub("\n", "\n//", line) # add // for comment in rtl code
RegSpec.write("RegSpec['GenUserHeader'] = \"\"\"%s\"\"\"\n" % line) # add RegSpec['GenUserHeader']

# Module specifications
for sheet in workbook:
  if re.search("^RegSpec_", sheet.title):
    # new RegSpec['RegSpec_*']
    content = "RegSpec['%s'] = {}\n" % sheet.title

    config_table_flag = 0
    register_table_flag = 0
    register_count = 0
    for row in sheet.rows:
      if config_table_flag == 1:
        if row[0].value == None: # end of table
          config_table_flag = 0
          continue
        elif row[0].value == 'Property': # info row
          continue
        elif row[0].value == 'Gen':
          if row[1].value == 'Yes':
            gen_flag = 1
            continue
          else:
            gen_flag = 0 # skip spec, reduce time
            break
        elif row[0].value == 'Module name':
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenModuleName',     row[1].value)
        elif row[0].value == 'Interface':                                                                   
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'Interface',         row[1].value)
        elif row[0].value == 'DataWidth':                                                                   
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenDataParam',      row[1].value)
        elif row[0].value == 'AddrWidth':                                                                   
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenAddrParam',      row[1].value)
        elif row[0].value == 'Reset':
          GenAsyncReset = 1 if row[1].value == 'Async' else 0
          GenSyncReset = 0 if row[1].value == 'Async' else 1
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenAsyncReset',     GenAsyncReset)
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenSyncReset',      GenSyncReset)
        elif row[0].value == 'Synchronization':
          GenAsyncParam = 1 if row[1].value == 'Async' else 0
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenAsyncParam',     GenAsyncParam)
        elif row[0].value == 'SynchronousStage':
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenSyncStageParam', row[1].value)
        elif row[0].value == 'Write protection':
          GenWProtParam = 1 if row[1].value == 'Yes' else 0
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenWProtParam',     GenWProtParam)
        elif row[0].value == 'Secure':
          GenSecParam = 1 if row[1].value == 'Yes' else 0
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenSecParam',       GenSecParam)
        elif row[0].value == 'SlaveError':
          GenWProtErrParam = 1 if 'WProt' in row[1].value else 0
          GenSecErrParam = 1 if 'Sec' in row[1].value else 0
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenWProtErrParam',  GenWProtErrParam)
          content += "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, 'GenSecErrParam',    GenSecErrParam)
      elif register_table_flag == 1:
        if row[0].value == None: # end of table
          register_table_flag = 0
          continue
        elif row[0].value == 'Bit': # info row
          continue
        else:
          if row[2].value not in temp_register: # new GenRegField
            temp_register[row[2].value] = {}
            register_field_count += 1
            register_field_count_current = register_field_count
            register_field_name = "Register_Field_No_" + str(register_field_count_current)
            register_field_split_count = 0
            
            # new RegSpec['RegSpec_*']['<register>']['<register_field>']
            content += "RegSpec['%s']['%s']['%s'] = {}\n" % (sheet.title, register_name, register_field_name)
  
            # new RegSpec['RegSpec_*']['<register>']['<register_field>']['Common_Config']
            content += "RegSpec['%s']['%s']['%s']['Common_Config'] = {}\n" % (sheet.title, register_name, register_field_name)
          
            # GenRegField, Field_Desciption & RW_Property
            content += "RegSpec['%s']['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, register_field_name, 'GenRegField', row[2].value)
            content += "RegSpec['%s']['%s']['%s']['Common_Config']['%s'] = \"\"\"%s\"\"\"\n" % (sheet.title, register_name, register_field_name, 'Field_Desciption', row[4].value)
            content += "RegSpec['%s']['%s']['%s']['Common_Config']['%s'] = []\n" % (sheet.title, register_name, register_field_name, 'RW_Property')
          else: # continue for GenRegField from previous split
            register_field_count_current = temp_register[row[2].value]['field_count']
            register_field_name = "Register_Field_No_" + str(register_field_count_current)
            register_field_split_count = temp_register[row[2].value]['split_count']
            
          # split property of GenRegField
          bit_range_list = str(row[0].value).split('/')
          reset_value_list = str(row[1].value).split('/')
          RW_property_list = str(row[3].value).split('/')
          
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
            strobe_index = int(bit_max/8)
            
            # Strobe_Index
            content += "RegSpec['%s']['%s']['%s']['%s']['%s'] = \"%s\"\n" % (sheet.title, register_name, register_field_name, register_field_split_name, 'GenPStrbIndex', strobe_index)
            
            # RW_Property
            content += "RegSpec['%s']['%s']['%s']['%s']['%s'] = []\n" % (sheet.title, register_name, register_field_name, register_field_split_name, 'RW_Property')
            for i in range(0, len(RW_property_list)): 
              content += "RegSpec['%s']['%s']['%s']['%s']['%s'].append(\"%s\")\n" % (sheet.title, register_name, register_field_name, register_field_split_name, 'RW_Property', RW_property_list[i])
              # whole field RW_Property
              content += "RegSpec['%s']['%s']['%s']['Common_Config']['%s'].append(\"%s\")\n" % (sheet.title, register_name, register_field_name, 'RW_Property', RW_property_list[i])
              # whole register RW_Property
              strobe_config = "Strobe_" + str(strobe_index)
              content += "RegSpec['%s']['%s']['Common_Config']['%s']['%s'].append(\"%s\")\n" % (sheet.title, register_name, 'RW_Property', strobe_config, RW_property_list[i])
          
          temp_register[row[2].value]['field_count'] = register_field_count_current
          temp_register[row[2].value]['split_count'] = register_field_split_count
      else:
        if row[0].value == 'Table':
          if row[1].value == 'RegFile': # begin of config table
            config_table_flag = 1
            # new RegSpec['RegSpec_*']['Common_Config'] 
            content += "RegSpec['%s']['Common_Config'] = {}\n" % sheet.title
          elif row[1].value == 'Gen':  # begin of register tables (Gen enable)
            register_table_flag = 1
            register_count += 1
            register_name = "Register_No_" + str(register_count)
            register_field_count = 0
            temp_register = {}
            
            # new RegSpec['RegSpec_*']['<register>']
            content += "RegSpec['%s']['%s'] = {}\n" % (sheet.title, register_name)

            # new RegSpec['RegSpec_*']['<register>']['Common_Config']
            content += "RegSpec['%s']['%s']['Common_Config'] = {}\n" % (sheet.title, register_name)
            
            # GenRegName, Register_Description & Initial_Value
            content += "RegSpec['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, 'GenRegName',           row[2].value)
            content += "RegSpec['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, 'Register_Description', row[3].value)
            content += "RegSpec['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, 'Initial_Value',        row[4].value)
            
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
