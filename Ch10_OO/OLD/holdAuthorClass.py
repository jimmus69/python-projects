
from PersonClass import *
from BookClass import *

class AuthorClass(object, PersonClass, BookClass):
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

    def called():
        print "AuthorClass Called!"
	
	called = staticmethod(called)
