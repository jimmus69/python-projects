# second.py

"""
This module imports first.py. It then defines the function sub_2
and the dictionary mod_dic. The purpose of the module is to show
module nesting and then something about the from ... import command.
"""

#import first
from first import all

def sub_2( a, b ):
    """
    sub_2( a, b ) -> a - b
    """
    return a -b

def display_mod_int():
    """
    display_mod_int() -> first.mod_int
    """
#    print first.mod_int
    print mod_int

mod_dic =  { 'a':1, 'b':2, 'c':3 }

