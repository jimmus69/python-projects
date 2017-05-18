
from PersonClass import *
from BookClass import *

class AuthorClass(PersonClass, BookClass):
    """
       Class: AuthorClass
        File: AuthorClass.py
    Function: An extension of PersonClass and BookClass to
              manage an author
    """
    #timesCalled = 0

    def __init__(self, full_name, country='unknow', publisher='unknow'):
        PersonClass.__init__(self, full_name, country)
        BookClass.__init__(self)
        self.publisher = publisher
		addParentCountPersonClass()

    def update_publisher( self, publisher ):
        self.publisher = publisher
        return True

