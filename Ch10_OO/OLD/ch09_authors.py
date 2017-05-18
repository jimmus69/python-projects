#! /usr/bin/python

"""
     program: authors.py
    Function: Manages a dictionary of authors
"""

from __future__ import print_function
import sys
import os
from authors_functions import *


if os.path.exists('authors.pickle'):
    try:
        author_file = open( 'authors.pickle', 'rb')
        try:
            authors = cPickle.load(author_file)
            author_file.close()
        except:
            authors = {}
    except:
        print("Could not open authors.pickle", file=sys.stderr)
        exit(1)
else:
    authors = {}
    
while True:
    response = get_response()
    if response == 'quit':
        break
    elif response == 'add_author':
        if not new_author(authors):
            print("Author in database")
    elif response == 'add_book':
        if not add_author_book(authors):
            print("Author not in database")
    elif response == 'delete_book':
        delete_author_book(authors)
    elif response == 'list_authors':
        author_list = list_authors(authors)
        if len(author_list) == 0:
            print ("No authors in database.")
        else:
            print("Author List")
            for author in author_list:
                print (author)
    elif response == 'list_books':
        books = list_author_books(authors)
        if books == "No author":
            print("No author in database")
        else:
            if len(books) == 0:
                print("Author has no books in database")
            else:
                print("Book List")
                for book in books:
                    print(book[0])
    else:
        print("Selection not valid:", response )

author_shutdown(authors)

