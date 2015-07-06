Insight Data Engineering - Coding Challenge
===========================================================

This challenge is to implement two features.

1. Calculate the total number of times each word has been tweeted.
2. Calculate the median number of *unique* words per tweet, and update this median as tweets come in.

More details can be found at https://github.com/InsightDataScience/cc-example

## Contents

This is the tree view of this repo:

    |-- License.txt
    |-- README.md
    |-- run.sh
    |-- src
    |  |-- blist-1.3.6.tar.gz
    |  |-- median_unique.py
    |  |-- words_tweeted.py
    |  |-- words_tweeted_utils.py
    |-- tweet_input
    |  |-- tweets.txt
    |-- tweet_output

## Requirements

- (Linux / Mac OS X) environment
- BASH (For run.sh)
- Python 2.7.6
- blist 1.3.6 package (https://pypi.python.org/pypi/blist)

## Installation (Linux / Mac OS X)

Executing run.sh script will install and run both features:

    ./run.sh

You can also manually install blist 1.3.6 with following commands:

    cd src
    tar -xvzf blist-1.3.6.tar.gz
    cd blist-1.3.6
    python setup.py install

## Execute both features

To run both features, simply type the following command (this will also install blist 1.3.6 package before features are executed):

    ./run.sh

## Execute individually

To calculate the total number of times each word has been tweeted:

    cd src
    python words_tweeted.py -i ../tweet_input/tweets.txt -o ../tweet_output/ft1.txt


To calculate the median number of *unique* words per tweet, and update this median as tweets come in:

    cd src
    python median_unique.py -i ../tweet_input/tweets.txt -o ../tweet_output/ft2.txt

## Optional

For big tweet.txt, you can split the tweet.txt into smaller files and run words_tweeted.py concurrently, and combine the results with words_tweeted_utils.py.
You can achieve this by using the Linux's split program (http://manpages.ubuntu.com/manpages/hardy/man1/avisplit.1.html).

e.g.:

    cd tweet_input
    split -l 100000000 tweets.txt tmp_

    cd ../src
    python words_tweeted.py -i ../tweet_input/tmp_aa -o ../tweet_output/tmp_ft1.txt > status_1.txt 2>&1 &
    python words_tweeted.py -i ../tweet_input/tmp_ab -o ../tweet_output/tmp_ft2.txt > status_2.txt 2>&1 &
    python words_tweeted.py -i ../tweet_input/tmp_ac -o ../tweet_output/tmp_ft3.txt > status_3.txt 2>&1 &
    python words_tweeted.py -i ../tweet_input/tmp_ad -o ../tweet_output/tmp_ft4.txt > status_4.txt 2>&1 &

    python words_tweeted_utils.py -i ../tweet_output/tmp_ft1.txt ../tweet_output/tmp_ft2.txt ../tweet_output/tmp_ft3.txt ../tweet_output/tmp_ft4.txt -o ../tweet_output/ft1.txt

## Licence

Copyright (C) 2015 David Rhee (david.rhee@einstein.yu.edu)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.