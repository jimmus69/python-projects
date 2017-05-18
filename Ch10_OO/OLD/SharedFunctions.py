"""
       Module:  SharedFunctions
         File:  SharedFunctions.py
     Function:  Contained shared functions
"""

def sep( string_value ):
    """
       sep( string_value ) returns a list of the charecters
       in the string
    """
    local_list = []
    for q in range(len(string_value)):
        local_list.append(string_value[q])
    return local_list

def concat( list_value, sep='' ):
    """
        concat( list_value, sep='') takes a list of strings
        and returns a single string.
    """
    local_string = ''
    for q in range(len(list_value)):
        local_string += (list_value[q] + sep)
    if sep != '':
        local_string = local_string[:-1]
    return local_string

