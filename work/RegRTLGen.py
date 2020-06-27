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
lib_path = script_path + "/../lib/pyLib"
sys.path.append(lib_path)

# remove old log
if os.path.exists("Error.log"):
  os.remove("Error.log")
if os.path.exists('finish_all'):
  os.remove("finish_all")
# progress bar
command = script_path + "/script/progress_bar.py"
subprocess.Popen(command, shell=True)

# read input specification
input_file = argv[1]
command = script_path + "/script/read_input.py " + argv[1]
subprocess.call(command, shell=True)

# generate RegRTL
command = script_path + "/script/gen_rtl.py " + "RegSpec.py"
subprocess.Popen(command, shell=True)

# create html specification
command = script_path + "/script/gen_html.py " + "RegSpec.py"
subprocess.Popen(command, shell=True)

# finish
while (not os.path.exists("finish_all")):
  time.sleep(1)
os.remove("finish_all")

print ("\n\tCongratulation! Mission completed!")
