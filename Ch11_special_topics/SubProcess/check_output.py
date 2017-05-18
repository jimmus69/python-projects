#! /usr/bin/env python
# check_output.py

import subprocess

output = subprocess.check_output('ls')
print output,
