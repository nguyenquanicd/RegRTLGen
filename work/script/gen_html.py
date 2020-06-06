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
from RegSpec import *

# finish
open("finish_gen_html", 'w').close()
