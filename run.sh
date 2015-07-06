#!/bin/bash

#########################################################################################################
# Install blist package
cd src
tar -xvzf blist-1.3.6.tar.gz
cd blist-1.3.6
python setup.py install

#########################################################################################################
# Run words_tweeted.py and median_unique.py
cd ..
python words_tweeted.py -i ../tweet_input/tweets.txt -o ../tweet_output/ft1.txt
python median_unique.py -i ../tweet_input/tweets.txt -o ../tweet_output/ft2.txt