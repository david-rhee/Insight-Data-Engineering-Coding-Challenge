#!/usr/bin/env python
import os, sys, string, time, argparse

''' 

USEAGE: python words_tweeted.py -options <addtional parameters>
PURPOSE:
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

Processes an input file (containing tweets in each line) to count unique words for each tweet.
The resulting counts are inserted to a dictionary for output later.

'''
def process_file(filename, words_tweeted) :
    # Declare variables
    max_width = 0
    counter = 0

    # Read line by line
    with open(filename, 'rU') as infile:
        for line in infile :               
            word_list = string.split(line)

            # For each tweet, count words and put in dictionary
            for word in word_list :
                if words_tweeted.has_key(word) :
                    words_tweeted[word] += 1
                else :
                    words_tweeted[word] = 1
                    if max_width < len(word) :
                        max_width = len(word)

            # Count the number of tweets being read
            counter += 1

    # Return number of tweeter feeds and maximum size of the word
    return counter, max_width

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
    usage='python words_tweeted.py -options <addtional parameters>'
    description='This program reads a text file containing tweets in each line, counts unique words and stores it in a dictionary.\
                Subsquently, the program outputs the sorted dictionary.'
    parser = argparse.ArgumentParser(usage=usage,description=description)
    parser.add_argument("-i", "--input", action="store", nargs=1, dest="input", metavar=("input"), help="Input file name.")
    parser.add_argument("-o", "--output", action="store", nargs=1, dest="output", metavar=("output"), help="Output file name.")
    args = parser.parse_args()

    # Check options
    if args.input and args.output :
        # Validate input option
        if not os.path.isfile(args.input[0]) :
            print 'Error! Input file "%s" does not exist.'%args.input[0]
            sys.exit(1)          
    else :
        print 'Error! Check the parameters.'
        sys.exit(1)

    # Declare variables
    words_tweeted = {}

    # Process input file
    start_time = time.time()
    counter, max_width = process_file(args.input[0], words_tweeted)
    words_tweeted_print(args.output[0], max_width, words_tweeted) 
    print("- Input                : %s" %(args.input[0]))
    print("- Output               : %s" %(args.output[0]))
    print("- No. of records       : %s tweets" %(counter))
    print("- Calculation time     : %s seconds" %(time.time() - start_time))

########################################################################################################################
########################################################################################################################
# Run
######################################################################################################################## 
########################################################################################################################
if __name__ == '__main__':
    print("----------------------------")
    print("| Running words_tweeted.py |")
    print("----------------------------")
    main()