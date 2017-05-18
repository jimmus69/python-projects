"""

       Class:  LocalVariables
        File:  LocalVariablesClass.py
    Function:  Contains shared variable for local functions
"""
from SharedVariablesClass import SharedVariables

class LocalVariables(SharedVariables):
    float_val = 42.14159
    str_val = SharedVariables.str_val + ". And that's the Truth"
    
