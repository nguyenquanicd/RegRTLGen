#!/usr/bin/python3.8

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

from tqdm import tqdm

def progress_observe(base_bar_name, full_bar, speed_low, speed_high, max_count, finish_flag, error_flag):
  count = 0
  while (not os.path.exists(finish_flag)):
    if count == 0:
      bar_name = base_bar_name
      progress_bar(bar_name, full_bar, speed_low, speed_high, finish_flag, error_flag)
    else:
      print (base_bar_name, ": is nearly done, let wait one more time!")
      bar_name = base_bar_name + ' (' + str(count) + ')'
      progress_bar(bar_name, full_bar, speed_low, speed_high, finish_flag, error_flag)
    count += 1
    if count == max_count:
      print ("Progress %s is taking too long time!" % base_bar_name)
      break

def progress_bar(bar_name, full_bar, speed_low, speed_high, finish_flag, error_flag):
  with tqdm(total=full_bar, desc=bar_name, bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
    for i in range(full_bar):
      if os.path.exists(error_flag):
        print ("ERROR FOUND! Plz check Error.log")
        stop_progress()
      if os.path.exists(finish_flag):
        pbar.n = full_bar
        pbar.refresh()
      else:
        time.sleep(speed_low)
        pbar.update()

def progress_bar2(bar_name, full_bar, speed_low, speed_high, max_count, finish_flag, error_flag):
  count = 0
  with tqdm(total=full_bar, desc=bar_name, bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
    if os.path.exists(finish_flag):
      pbar.n = full_bar
      pbar.refresh()
    else:
      while (not os.path.exists(finish_flag)):
        for i in range(full_bar):
          time.sleep(speed_low)  
          if os.path.exists(error_flag):
            print ("ERROR FOUND! Plz check Error.log")
            stop_progress()
          elif os.path.exists(finish_flag):
            pbar.n = full_bar
            pbar.refresh()
            break
          elif count != 0:
            pbar.n = i
            pbar.refresh()
          else:
            pbar.update()
        count = count + 1
        if count == max_count:
          print ("Progress %s is taking too long time!" % base_bar_name)
          break
        
def remove_finish_flag():
  if os.path.exists('finish_read_input'):
    os.remove("finish_read_input")
  if os.path.exists('finish_gen_rtl'):
    os.remove("finish_gen_rtl")
  if os.path.exists('finish_gen_html'):
    os.remove("finish_gen_html")
  if os.path.exists('finish_gen_uvm'):
    os.remove("finish_gen_uvm")

def stop_progress():
  remove_finish_flag()
  open("finish_all", 'w').close()
  sys.exit()
  
remove_finish_flag()
#progress_observe("Read Input Spec ", 100, 0.03, 0.01, 5, "finish_read_input", "Error.log")
#progress_observe("Generate RTL    ", 100, 0.03, 0.01, 5, "finish_gen_rtl", "Error.log")
#progress_observe("Generate HTML   ", 100, 0.03, 0.01, 5, "finish_gen_html", "Error.log")
progress_bar2("Read Input Spec ", 100, 0.03, 0.01, 15, "finish_read_input", "Error.log")
progress_bar2("Generate RTL    ", 100, 0.03, 0.01, 15, "finish_gen_rtl", "Error.log")
progress_bar2("Generate HTML   ", 100, 0.03, 0.01, 15, "finish_gen_html", "Error.log")
progress_bar2("Generate UVM    ", 100, 0.03, 0.01, 15, "finish_gen_uvm", "Error.log")

remove_finish_flag()
open("finish_all", 'w').close()
