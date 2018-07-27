#-----------------------------------------------------------------------------
# This is a program that will help read fields from a text file
# seperated by a seperator
#
# Written by Rakshith Varadaraju, July 23 2018 for Homework 9 in SSW-810
#-----------------------------------------------------------------------------

def extract(filename, num_fields, sep='\t', header=False):
    '''This is a python generator that reads a file one line at a time
    and returns the values from the line seperated by the seperator'''
    try:
        fp = open(filename, 'r')
    except FileNotFoundError:
        print("Can't open", filename)
    else:
        with fp:
            line_number = 0
            for line in fp:
                line_number += 1
                if header:
                    header = False
                    continue
                line_elements = line.strip().split(sep)
                if len(line_elements) == num_fields:
                    yield line_elements
                else:
                    raise ValueError(filename + " has " + str(len(line_elements)) + 
                    " fields on line " + str(line_number) + " but expected " + 
                    str(num_fields))