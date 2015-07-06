#!/usr/bin/env python
import os, sys, string, time, argparse

''' 

USEAGE: python words_tweeted_utils.py -options <addtional parameters>
PURPOSE: For big tweet.txt (~ 500 million tweets), it would be ideal to split the input and use words_tweet.py seperately to generated the output.
        This utils script can be used to combine these individual output files.
DATE: 07/06/2015
Version: 0.1
AUTHOR: David Rhee
Modifier:
Email: david.rhee@einstein.yu.edu

'''

########################################################################################################################
########################################################################################################################
# Functions
######################################################################################################################## 
########################################################################################################################
''' 

Processes an input file that contains unique word and its count per line.
The resulting counts are inserted to a dictionary for output later.

'''
def process_file(filename, words_tweeted) :
    # Declare variables
    max_width = 0

    # Read line by line
    with open(filename, 'rU') as infile:
        for line in infile :               
            word, count = string.split(line)

            # For each word, check if it already exists in a dictionary
            if words_tweeted.has_key(word) :
                words_tweeted[word] += int(count)
            else :
                words_tweeted[word] = int(count)
                if max_width < len(word) :
                    max_width = len(word)

    # Return maximum size of the word
    return max_width

'''

Given dictionary is sorted and its contents exported to an output file.

'''
def words_tweeted_print(filename, max_width, words_tweeted) :
    # Sort the keys
    keys = words_tweeted.keys()
    keys.sort()  

    # Export the content of the dictionary to an output file
    outfile = open(filename, 'w')
    for key in keys :
        outfile.write("{0}\t{1}\n".format(key.ljust(max_width), str(words_tweeted[key])))
    outfile.close()

########################################################################################################################
########################################################################################################################
# Main
######################################################################################################################## 
########################################################################################################################
def main() :    
    # Parse options
    usage='python words_tweeted_utils.py -options <addtional parameters>'
    description='This program reads multiple input files (unique word - count), joins results, and export to output file.'
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument("-i", "--inputs", action="store", nargs='*', dest="inputs", metavar=("inputs"), help="Input file name(s) - space delimited")
    parser.add_argument("-o", "--output", action="store", nargs=1, dest="output", metavar=("output"), help="Output file name.")
    args = parser.parse_args()

    # Check options
    if args.inputs and args.output :
        for input_file in args.inputs :
            # Validate input option
            if not os.path.isfile(input_file) :
                print 'Error! Input file "%s" does not exist.'%input_file
                sys.exit(1)          
    else :
        print 'Error! Check the parameters.'
        sys.exit(1)

    # Declare variables
    words_tweeted = {}
    max_width = 0
    
    # Process input file
    start_time = time.time()

    # For each input files
    for input_file in args.inputs :

        # Read the content and fill the dictionary        
        tmp_max_width = process_file(input_file, words_tweeted)

        if max_width < tmp_max_width :
            max_width = tmp_max_width
        
    words_tweeted_print(args.output[0], max_width, words_tweeted) 
    print("- Inputs               : %s" %(args.inputs))
    print("- Output               : %s" %(args.output[0]))
    print("- Calculation time     : %s seconds" %(time.time() - start_time))

########################################################################################################################
########################################################################################################################
# Run
######################################################################################################################## 
########################################################################################################################
if __name__ == '__main__':
    print("----------------------------")
    print("| Running words_tweeted_utils.py |")
    print("----------------------------")
    main()