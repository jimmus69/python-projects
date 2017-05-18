#! /usr/bin/env python

import sys, pprint
mod = __import__(sys.argv[1])

names = [ name for name in dir(mod) if name[0] != '_']
pprint.pprint(names)
