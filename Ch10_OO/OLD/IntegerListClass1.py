"""
       Class: IntegerList
        File: IntegerListClass.py
    Function: Explore some more about classes using a list of integers
"""

class IntegerList:
    def __init__( self, integer_list ):
        if all( map( lambda x: str(x).isdigit(), integer_list)):
            self.list = integer_list
        else:
            raise
