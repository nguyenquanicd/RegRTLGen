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

## Main process
from openpyxl import load_workbook

# load input spec
input_file = argv[1]
workbook = load_workbook(filename=input_file)

# create variable structure
RegSpec = open(script_path + "/RegSpec.py","w")
content = "RegSpec = {}\n"
RegSpec.write(content) # new RegSpec

# CommonInfo sheet
CommonInfoSheet = workbook["CommonInfo"]
common_table_flag = 0
line = ''
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
content = "RegSpec['Common_Info'] = \"\"\"%s\"\"\"\n" % line
RegSpec.write(content) # add RegSpec['Common_Info']

# Module specifications
for sheet in workbook:
  if re.search("^RegSpec_", sheet.title):
    content = "RegSpec['%s'] = {}\n" % sheet.title
    RegSpec.write(content) # new RegSpec['RegSpec_*']
    
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
          config = 'Gen'
        elif row[0].value == 'Module name':
          config = 'Module_Name'
        elif row[0].value == 'Interface':
          config = 'Interface'
        elif row[0].value == 'DataWidth':
          config = 'DataWidth'
        elif row[0].value == 'AddrWidth':
          config = 'AddrWidth'
        elif row[0].value == 'Reset':
          config = 'Reset'
        elif row[0].value == 'Synchronization':
          config = 'Synchronization'
        elif row[0].value == 'SynchronousStage':
          config = 'SynchronousStage'
        elif row[0].value == 'Write protection':
          config = 'Write_Protection'
        elif row[0].value == 'Secure':
          config = 'Secure'
        elif row[0].value == 'SlaveError':
          config = 'SlaveError'
        content = "RegSpec['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, config, row[1].value)
        RegSpec.write(content)
      elif register_table_flag == 1:
        if row[0].value == None: # end of table
          register_table_flag = 0
          continue
        elif row[0].value == 'Bit': # info row
          continue
        else:
          register_field_count += 1
          register_field_name = "Register_Field_No_" + str(register_field_count)
          
          content = "RegSpec['%s']['%s']['%s'] = {}\n" % (sheet.title, register_name, register_field_name)
          RegSpec.write(content) # new RegSpec['RegSpec_*']['<register>']['<register_field>']
          
          content = "RegSpec['%s']['%s']['%s']['Common_Config'] = {}\n" % (sheet.title, register_name, register_field_name)
          RegSpec.write(content) # new RegSpec['RegSpec_*']['<register>']['<register_field>']['Common_Config']
          
          config = 'Field_Name'
          content = "RegSpec['%s']['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, register_field_name, config, row[2].value)
          RegSpec.write(content)
          
          config = 'Field_Desciption'
          content = "RegSpec['%s']['%s']['%s']['Common_Config']['%s'] = \"\"\"%s\"\"\"\n" % (sheet.title, register_name, register_field_name, config, row[4].value)
          RegSpec.write(content)
          
          bit_range_list = str(row[0].value).split('/')
          reset_value_list = str(row[1].value).split('/')
          RW_property_list = str(row[3].value).split('/')
          
          # correct len, in cased user not define fully
          if len(reset_value_list) < len(bit_range_list):
            for i in range(len(reset_value_list), len(bit_range_list)):
              reset_value_list.append("'0")
          
          register_field_split_count = 0
          for i in range(0, len(bit_range_list)):
            register_field_split_count += 1
            register_field_split_name = "Register_Field_Split_No_" + str(register_field_split_count)
            content = "RegSpec['%s']['%s']['%s']['%s'] = {}\n" % (sheet.title, register_name, register_field_name, register_field_split_name)
            RegSpec.write(content) # new RegSpec['RegSpec_*']['<register>']['<register_field>']['<register_field_split>']
            
            config = 'Bit_Range'
            content = "RegSpec['%s']['%s']['%s']['%s']['%s'] = \"%s\"\n" % (sheet.title, register_name, register_field_name, register_field_split_name, config, bit_range_list[i])
            RegSpec.write(content)
            
            config = 'Reset_Value'
            content = "RegSpec['%s']['%s']['%s']['%s']['%s'] = \"%s\"\n" % (sheet.title, register_name, register_field_name, register_field_split_name, config, reset_value_list[i])
            RegSpec.write(content)
            
            config = 'Strobe_Index'
            bit_range_list_array = str(bit_range_list[i]).split(':')
            bit_max = int(max(bit_range_list_array))
            if bit_max < 8:
              strobe_index = 0
            elif bit_max < 16:
              strobe_index = 1
            elif bit_max < 24:
              strobe_index = 2
            elif bit_max < 32:
              strobe_index = 3
            content = "RegSpec['%s']['%s']['%s']['%s']['%s'] = \"%s\"\n" % (sheet.title, register_name, register_field_name, register_field_split_name, config, strobe_index)
            RegSpec.write(content)
            
            config = 'RW_Property'
            content = "RegSpec['%s']['%s']['%s']['%s']['%s'] = []\n" % (sheet.title, register_name, register_field_name, register_field_split_name, config)
            RegSpec.write(content)
            for i in range(0, len(RW_property_list)): 
              content = "RegSpec['%s']['%s']['%s']['%s']['%s'].append(\"%s\")\n" % (sheet.title, register_name, register_field_name, register_field_split_name, config, RW_property_list[i])
              RegSpec.write(content)
              
              if strobe_index == 0:
                content = "RegSpec['%s']['%s']['Common_Config']['%s']['Strobe_0'].append(\"%s\")\n" % (sheet.title, register_name, config, RW_property_list[i])
              elif strobe_index == 1:
                content = "RegSpec['%s']['%s']['Common_Config']['%s']['Strobe_1'].append(\"%s\")\n" % (sheet.title, register_name, config, RW_property_list[i])
              elif strobe_index == 2:
                content = "RegSpec['%s']['%s']['Common_Config']['%s']['Strobe_2'].append(\"%s\")\n" % (sheet.title, register_name, config, RW_property_list[i])
              elif strobe_index == 3:
                content = "RegSpec['%s']['%s']['Common_Config']['%s']['Strobe_3'].append(\"%s\")\n" % (sheet.title, register_name, config, RW_property_list[i])
              RegSpec.write(content)
      else:
        if row[0].value == 'Table':
          if row[1].value == 'RegFile': # begin of config table
            config_table_flag = 1
            content = "RegSpec['%s']['Common_Config'] = {}\n" % sheet.title
            RegSpec.write(content) # new RegSpec['RegSpec_*']['Common_Config'] 
          else:  # begin of register tables
            register_table_flag = 1
            register_count += 1
            register_name = "Register_No_" + str(register_count)
            register_field_count = 0
            
            content = "RegSpec['%s']['%s'] = {}\n" % (sheet.title, register_name)
            RegSpec.write(content) # new RegSpec['RegSpec_*']['<register>']
            
            content = "RegSpec['%s']['%s']['Common_Config'] = {}\n" % (sheet.title, register_name)
            RegSpec.write(content) # new RegSpec['RegSpec_*']['<register>']['Common_Config']
            
            config = 'Generate_Flag'
            content = "RegSpec['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, config, row[1].value)
            RegSpec.write(content)
            
            config = 'Register_Name'
            content = "RegSpec['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, config, row[2].value)
            RegSpec.write(content)
            
            config = 'Register_Description'
            content = "RegSpec['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, config, row[3].value)
            RegSpec.write(content)
            
            config = 'Initial_Value'
            content = "RegSpec['%s']['%s']['Common_Config']['%s'] = \"%s\"\n" % (sheet.title, register_name, config, row[4].value)
            RegSpec.write(content)
            
            config = 'RW_Property'
            content = "RegSpec['%s']['%s']['Common_Config']['%s'] = {}\n" % (sheet.title, register_name, config)
            RegSpec.write(content)
            content = "RegSpec['%s']['%s']['Common_Config']['%s']['Strobe_0'] = []\n" % (sheet.title, register_name, config)
            RegSpec.write(content)
            content = "RegSpec['%s']['%s']['Common_Config']['%s']['Strobe_1'] = []\n" % (sheet.title, register_name, config)
            RegSpec.write(content)
            content = "RegSpec['%s']['%s']['Common_Config']['%s']['Strobe_2'] = []\n" % (sheet.title, register_name, config)
            RegSpec.write(content)
            content = "RegSpec['%s']['%s']['Common_Config']['%s']['Strobe_3'] = []\n" % (sheet.title, register_name, config)
            RegSpec.write(content)
            
          
# finish
RegSpec.close()    
open("finish_read_input", 'w').close()
