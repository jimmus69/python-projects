#! /usr/bin/python

"""
     Program:  ch05_17_function_passing.py
    Function:  Exploring the names of fuctions
"""

def simple_sort(list_sort, cmp_function):
    new_list_sort = list_sort[:]

    def swap( list_in, a, b ):
        temp = list_in[a]
        list_in[a] = list_in[b]
        list_in[b] = temp
        return

    again = True

    while again:
        again = False
        for i in range(0,len(new_list_sort) - 1):
            value = cmp_function(new_list_sort[i],new_list_sort[i + 1])
            if value:
                swap(new_list_sort, i, i+1)
                again = True
    return new_list_sort
                
def string_length_compare(a, b):
    offsetA = len(a) -1;
    offsetB = len(b) -1;
    while offsetA > 0 and offsetB > 0:
	if a[offsetA] > b[offsetB]:
	    return True
        else:
            offsetA -= 1
            offsetB -= 1
    return False 

list1 = [ 'mer', 'azbc', 'zz', 'qrx', 'abb', 'azbb' ]

print "      List to be sorted: ", list1

sorted_list1 = simple_sort( list1, string_length_compare)

print "After list to be sorted: ", list1
print "      After sorted list: ", sorted_list1

print "\nThat's all folks!"

