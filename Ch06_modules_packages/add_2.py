#! /usr/bin/env python

def add_2( a, b ):
    return a + b

if __name__ == "__main__":
    import sys
    print add_2(int(sys.argv[1]), int(sys.argv[2]))

