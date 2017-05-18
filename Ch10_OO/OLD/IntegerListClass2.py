#! /usr/bin/python

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

    def display( self ):
        return str(self.list)[1:-1]

    def reverse( self ):
        self.list.reverse()

    def __eq__(self, b):
        if len(self.list) != len(b.list):
            return False
        else:
            for i in range(len(self.list)):
                if self.list[i] != b.list[i]:
                     return False
            else:
                return True

    def __len__( self ):
        return len(self.list)
    
    def __str__( self ):
        return str(self.list)[1:-1]

    def __add__( self, a):
        """
           a is an integer add a to each element of the list
        """
        if type(a) == type(1):
            for i in range(len(self.list)):
                self.list[i] += a
            return True
        if type(a) == type(self):
            if len(self.list) != len(a):
                return False
            for i in range(len(self.list)):
                self.list[i] = self.list[i] + a.list[i]
            return True
        if type(a) == type([1,2]):
            # check for all integer in a
            if len(self.list) != len(a):
                return False
            for i in range(len(self.list)):
                self.list[i] = self.list[i] + a[i]
            return True
          

one = IntegerList(range(1,5))

print one.display()

#two = IntegerList(range(1,5))
two = IntegerList([1,2])
print two.display()

print one +  range(1,5)
print one.display()
print "printing IntegerList: ", one
