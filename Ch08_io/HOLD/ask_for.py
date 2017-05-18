#! /usr/bin/python

def stdin_str( question ):
    return raw_input( question )

if __name__ == "__main__":
    import sys
    print stdin_str(sys.argv[1])

