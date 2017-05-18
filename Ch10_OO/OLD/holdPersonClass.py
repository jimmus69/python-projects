"""
        Class:  PersonClass
         File:  PersonClass.py
     Function:  Records the full name of a person and the
                country of origin.
"""

from SharedFunctions import *
    
class PersonClass:

    """
        Very basic information on a person.
        Full name as a string and country as a string.
    """

	timesCalled = 0
    
    def __init__( self, full_name, country):
        """
            PersonClass( fullname, country_of_origin ) returns a
            reference to a dictionary object with data
        """
        self.full_name = list(full_name.split())
        self.country = country

    def update_full_name( self, name):
	self.full_name = list(name.split())

    def get_full_name(self):
        """
            full_name() returns the full name
        """
        return concat( self.full_name, sep=' ')

    def get_first_name(self):
        """
            first_name() returns the first name
        """
        return self.full_name[0]

    def get_last_name(self):
        """
            last_name() returns family name
        """
        return self.full_name[-1]

    def update_country( self, new_country):
        self.country = new_country

    def get_country(self):
        """
            country() returns the country of origin
        """
        return self.country

    @classmethod
    def classcall(im_self):
        print im_self.__name__
        print "class called: ", im_self.timesCalled

