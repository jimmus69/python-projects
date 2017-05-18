"""
        Class: BookClass
         File: BookClass.py
     Function: Manages a list of tuples on books
               [ ('title', 'date'),...]
"""

class BookClass:
    """
        Manages a list of tuples on books
        [ ('title', 'date'),...]
    """

    def __init__(self):
        self.books = []

    def add_book( self, title, date ):
        if ( title, date ) not in self.books:
            self.books.append( (title, date) )
            return True
        else:
            return False

    def remove_book( self, title, date ):
        if ( title, date ) in self.books:
            self.books.remove( (title, date) )
            return True
        else:
            return False

    def get_books( self ):
        return self.books
        

    
