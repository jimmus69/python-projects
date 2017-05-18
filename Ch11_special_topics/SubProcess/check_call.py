#! /usr/bin/env python
# check_call.py

# THIS DID NOT WORK

import subprocess

try:
   subprocess.check_call("notCommand")
except subprocess.CalledProcessError  as err:
   print 'Error: ', err
 
