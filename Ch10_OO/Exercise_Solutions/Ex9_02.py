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
        temp_list = []
        if type(value) == int:
            for q in range(len(self.iList)):
                self.iList[q] = self.iList[q] + value
            return self.iList
        else:
            for q in range(len(self.iList)):
                temp_list.append(self.iList[q] + value[q])
            return IntegerList( temp_list )
                
    def __eq__(self, value):
			if type(value) == list:
				if len(self.iList) != len(value):
					return False
				for q in range(len(self.iList)):
					if self.iList[q] != value[q]:
						return False
				return True
			if isinstance(value, IntegerList):
				if len(self.iList) != len(value.iList):
					return False
				for q in range(len(self.iList)):
					if self.iList[q] != value.iList[q]:
						return False
				return True

                             
