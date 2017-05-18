# first_doc.py

"""
The first module is for learning how to import attributes
and the problems of importing attributes that are variables
in the module.
"""

mod_int = 25
mod_list = [ 1, 2, 3]

def ident():
    """
    Returns a string saying which module being accessed
    """
    print "From the module", __name__
    return

def add_2( a, b ):
    """
    add_2( a, b) -> a + b
    """
    return a + b
