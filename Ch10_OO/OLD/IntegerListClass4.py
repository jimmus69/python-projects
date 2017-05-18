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

    def reverse( self ):
        self.list.reverse()

    def display( self ):
        return str(self.list)[1:-1]
            
    def __add__(self, value):
        temp_list = []
        if type(value) == type(1):
            for q in range(len(self.list)):
                temp_list.append(self.list[q] + value)
            return IntegerList( temp_list )
        else:
            for q in range(len(self.list)):
                temp_list.append(self.list[q] + value[q])
            return IntegerList( temp_list )

    def __eq__( self, value):
        if type(value) == type(self):
            return self.list == value.list
        else:
            return self.list == value
                
                             
