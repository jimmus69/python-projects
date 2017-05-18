
"""
      Module:  dictionaryRoutines
    Function:  Based upon the first character of the key program adds (+),
               removes (-), looks up (=) the value for the key, or prints (!)
               the dictionary.
"""

def add_key( key, dictionary):
    """
    Action letter +
    Asks for value to associate with key
    Does no checking if key is already in dictionary
    """
    value = raw_input( "Enter value:  ")
    dictionary[key] = value
    print key, "->", value, "added to dictionary"

def remove_key( key, dictionary ):
    """
    Action letter -
    If key exists in dictionary removes entry.
    If key not in dictionary returns statement: <key> not in dictionary
    """
    if key in dictionary:
       del dictionary[key]
       print key, "removed from dictionary"
    else:
       print key, "not in dictionary"

def lookup_key( key, dictionary ):
    """
    Action letter =
    Returns <key> -> <value> if key in dictionary
    If key not in dictionary returns statement: <key> not in dictionary
    """
    if key in dictionary:
       print key, "->", dictionary[key]
    else:
       print key, "not in dictionary"

def print_dictionary(dictionary):
    """
    Action letter !
    Print out the entire dictionary 1 key value pair per line
    """
    for key in dictionary.keys():
        print key, "->", dictionary[key]

