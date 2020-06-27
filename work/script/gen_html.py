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

## Main process
for spec_cnt in range(1, len([*RegSpec])):
  # prepare output HTML
  spec_sheet = [*RegSpec][spec_cnt]
  output_path = script_path + "/../../output/" + RegSpec[spec_sheet]['Common_Config']['GenModuleName'] + ".html"
  html_output = open(output_path, "w")
  line_print = "<html>\n<body>\n" # header of html
  
  sumarize_table = "Register list of module: %s\n" % (RegSpec[spec_sheet]['Common_Config']['GenModuleName'])
  sumarize_table += "<table border=\"1\">\n"
  sumarize_table += "<tr><td>name<td>offset<td>reset\n"
  
  detail_table = ""
  for reg_cnt in range(1, len([*RegSpec[spec_sheet]])):
    reg_key = [*RegSpec[spec_sheet]][reg_cnt]
    
    GenRegName           = RegSpec[spec_sheet][reg_key]['Common_Config']['GenRegName']
    Register_Address     = RegSpec[spec_sheet][reg_key]['Common_Config']['Register_Address']
    Register_Description = RegSpec[spec_sheet][reg_key]['Common_Config']['Register_Description']
    
    sumarize_table += "<tr><td>%s<td>%s<td>%s\n" % (GenRegName, Register_Address, 'T.B.D')
    detail_table   += "%s offset:%s reset:%s<br>\n" % (GenRegName, Register_Address, 'T.B.D')
    detail_table   += " %s<br>\n" % (Register_Description)
    detail_table   += "<table border=\"1\">\n"
    detail_table   += "<tr><td>bit<td>reset<td>description\n"
    
    for field_cnt in range(1, len([*RegSpec[spec_sheet][reg_key]])):
      field_key = [*RegSpec[spec_sheet][reg_key]][field_cnt]
      for split_cnt in range(1, len([*RegSpec[spec_sheet][reg_key][field_key]])):
        split_key = [*RegSpec[spec_sheet][reg_key][field_key]][split_cnt]
        GenPartialBitRange = RegSpec[spec_sheet][reg_key][field_key][split_key]['GenPartialBitRange']
        GenFieldReset      = RegSpec[spec_sheet][reg_key][field_key][split_key]['GenFieldReset']
        Field_Desciption   = RegSpec[spec_sheet][reg_key][field_key]['Common_Config']['Field_Desciption']
        detail_table   += "<tr><td>%s<td>%s<td>%s\n" % (GenPartialBitRange, GenFieldReset, Field_Desciption)
    detail_table += "</table>\n<p>\n" # end of each detail table
  sumarize_table += "</table>\n<p>\n" # end of sumarize_table
  
  line_print += sumarize_table
  line_print += detail_table
  line_print += "</body>\n</html>\n" # footer of html
  
  html_output.write(line_print) # write all content to output HTML
  html_output.close()

# finish
open("finish_gen_html", 'w').close()
