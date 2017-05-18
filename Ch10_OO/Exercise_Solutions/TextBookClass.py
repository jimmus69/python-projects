
from PersonClass import *
from BookClass import *

class TextBookClass(BookClass):
    """
       Class: AuthorClass
        File: AuthorClass.py
    Function: An extension of PersonClass and BookClass to
              manage an author
    """

    def __init__(self, full_name, country='unknow', publisher='unknow'):
        PersonClass.__init__(self, full_name, country)
        BookClass.__init__(self)
        self.publisher = publisher

    def update_publisher( self, publisher ):
        self.publisher = publisher
        return True

    def update_country( self, country ):
        self.country = country
        return True

    def update_full_name( self, full_name):
        self.full_name = full_name
        return True

    
        
