#! /usr/bin/python

import time

class flushfile(object):
  def __init__(self, f):
    self.f = f 
  def write(self, x):
    self.f.write(x)
    self.f.flush()
 
import sys
sys.stdout = flushfile(sys.stdout)


name = raw_input( "Please enter your first Name:  " )
print "Hello", name 
time.sleep(5)
print "Good-bye", name 
