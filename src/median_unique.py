#!/usr/bin/env python
import os, sys, string, time, argparse, bisect
from blist import sortedlist

''' 

USEAGE: python median_unique.py -options <addtional parameters>
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

Finds a median from a sorted list.

'''
def median_of_list(tmp_list):
    if len(tmp_list) == 1: # If list only contains 1 element, return it
        return tmp_list[0]
    elif len(tmp_list) %2 == 1: # If list contains odd elements, return the middle element
        return tmp_list[((len(tmp_list)+1)/2)-1]
    else: # If list contains even elements, return the average of two middle elements    
        return float(sum(tmp_list[(len(tmp_list)/2)-1:(len(tmp_list)/2)+1]))/2

''' 

Processes an input file (containing tweets in each line) to count unique words for each tweet.
The resulting unique tweet count is appended to a list for further processing.

'''
def process_file(filename, median_unique_words_tweeted) :
    # Read line by line
    with open(filename, 'rU') as infile:
        for line in infile :
               
            word_list = string.split(line)
            word_dict = {}

            # For each tweet, find unique words
            for word in word_list :    
                if word_dict.has_key(word):
                    word_dict[word] += 1
                else :
                    word_dict[word] = 1

            # For each tweet, append the resulting unique word counts to a list
            median_unique_words_tweeted.append(len(word_dict))

'''

Sorts a given list containing unique word counts, calculates the median, and add to a new list.
Prints the new list containing updated median result.

'''
def unique_median_print(filename, median_unique_words_tweeted) :
    # Declare variables
    #tmp_median_unique_words_tweeted = []
    tmp_median_unique_words_tweeted = sortedlist([])
    new_median_unique_words_tweeted = []

    # For each unique word counts, append to a new list, sort and find the median of updated list
    for x in median_unique_words_tweeted:
        #bisect.insort(tmp_median_unique_words_tweeted, x, lo=0, hi=len(tmp_median_unique_words_tweeted))
        tmp_median_unique_words_tweeted.add(x)
        new_median_unique_words_tweeted.append(median_of_list(tmp_median_unique_words_tweeted))

    # Export the content of the updated list to an output file
    outfile = open(filename, 'w')
    for item in new_median_unique_words_tweeted :
        outfile.write("{0}\n".format(str(item)))
    outfile.close()

########################################################################################################################
########################################################################################################################
# Main
######################################################################################################################## 
########################################################################################################################
def main() :
    # Declare variables
    median_unique_words_tweeted = []

    # Parse options
    usage='python median_unique.py -options <addtional parameters>'
    description='This program reads a text file containing tweets in each line, counts unique words and stores it in a list.\
                Subsquently, the program calculates the median of the list and updates as the list grows.'
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

    # Process file
    start_time = time.time()
    process_file(args.input[0], median_unique_words_tweeted)
    unique_median_print(args.output[0], median_unique_words_tweeted)  
    print("- Input : %s" %(args.input[0]))
    print("- Output : %s" %(args.output[0]))
    print("- No. of records : %s tweets" %(len(median_unique_words_tweeted)))
    print("- Calculation time : %s seconds" %(time.time() - start_time))

########################################################################################################################
########################################################################################################################
# Run
######################################################################################################################## 
########################################################################################################################
if __name__ == '__main__':
    print("----------------------------")
    print("| Running median_unique.py |")
    print("----------------------------")
    main()