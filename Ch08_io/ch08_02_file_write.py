#! /usr/bin/env python

"""
     Program: ch08_02_file_write.py
    Function: Something on write to a file
"""

import sys

work_file = raw_input( "Enter file to write to: " )
if work_file == "":
    print >>sys.stderr, "No file entered:", work_file
    sys.exit(1)

try: 
    file_write = open( work_file, "w")
except IOError, err:
    print >>sys.stderr, "Error: ", err
    sys.exit(1)
except:
    print >>sys.stderr, "Unknow error with file", work_file
    sys.exit(1)

while True:
    try: 
        line = raw_input("Enter: ")
    except EOFError:
        break
    except:
        print >>sys.stderr, "Unknow error with input"
        file_write.close()
        sys.exit(1)
    else:
        file_write.write(line + "\n")

file_write.close()
print "\nThat's all folks!" 
sys.exit(0)
