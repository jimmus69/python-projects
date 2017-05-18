#! /usr/bin/env python
# call.py

import subprocess

# make list of strings if command larger than 1 string
output = subprocess.call([ 'ls', '-l'])
print output,
