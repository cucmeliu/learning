#!/usr/bin/python
# Filenam e: cat.py
import sys

def readfile(filename):
    '''Print a file to the standard output.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line, # notice com m a
    f.close()

# Script starts from here
if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':
        print 'V ersion 1.2'
    elif option == 'help':
        print '''\
        This program prints files to the standard output.
        Any number of files can be specified.
        O ptions include:
        --version : Prints the version num ber
        --help : D isplay this help'''
    else:
        print 'U nknown option.'
        sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
