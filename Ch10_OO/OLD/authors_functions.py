"""
      module: authors_functions
        file: authors_functions.py
    function: functions to support ch09_authors.py
"""

import cPickle
from AuthorClass import *

def get_response():
    question = '''
                Enter  q  for quit
                      aa  for add author
                      ab  for add book
                      la  for list authors
                      lb  for list books
                      db  for delete book
                Selection: '''
    
    possible_responses = { 'aa':'add_author',
                           'ab':'add_book',
                           'db':'delete_book',
                           'lb': 'list_books',
                           'la':'list_authors',
                           'q':'quit'
                         }
    
    while True:
        try:
            letter_response = raw_input(question)
        except:
            response = 'quit'
            return response

        if letter_response in possible_responses:
            response = possible_responses[letter_response]
            return response
        else:
            print"Response must be in", str(possible_responses.keys())[1:-1]
            print"Please re-enter"

def new_author(authors):
    full_name = raw_input( "Full name:  " )
    country = raw_input( "Country of origin: ")
    temp_author = AuthorClass( full_name )
    if country != '':
        temp_author.update_country(country)
    author_key = temp_author.get_last_name().upper()
    if author_key in authors and \
           full_name == authors[author_key].get_full_name():
        return False
    else:
        authors[author_key] = temp_author
        return True

def list_authors(authors):
    author_list = []
    if len(authors) > 0:
        for author_key in authors:
            author_list.append(authors[author_key].get_full_name())
    return author_list

def delete_author_book(authors):
    print("Got to delete_author_book")
    return True

def author_shutdown(authors):
    author_file = open('authors_new.pickle', "wb")
    cPickle.dump(authors,author_file,protocol=2)
    author_file.close()
    print "That's all folks!"

def add_author_book(authors):
    full_name = raw_input("Author's Name: ")
    title = raw_input("Book title: ")
    date = raw_input("Date published: ")

    key = full_name.split()[-1].upper()

    if key not in authors:
        return False
    else:
        authors[key].add_book( title, date)
        return True

def list_author_books(authors):
    full_name = raw_input("Author's Name: ")

    books = "No author"

    key = full_name.split()[-1].upper()
   
    if key in authors:
        books = authors[key].get_books()

    return books
