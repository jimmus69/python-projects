"""
       Class: IntegerList
        File: IntegerListClass.py
    Function: Explore some more about classes using a list of integers
"""

class IntegerList:
    def __init__( self, integer_list ):
            self.iList = integer_list

    def reverse( self ):
        self.iList.reverse()
        return self.iList

    def display( self ):
        return str(self.iList)[1:-1]
            
    def __add__(self, value):
        for q in range(len(self.iList)):
            self.iList[q] = self.iList[q] + value
        return self.iList
                
                             
