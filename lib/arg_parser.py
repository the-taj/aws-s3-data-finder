#!/usr/bin/env python3
###############################################
## Purpose: Provies argument parsing capability
###############################################
import argparse

parser = argparse.ArgumentParser(description='''''')

###############################################
## String options
###############################################
parser.add_argument('-nk', '--num_keys', default=200000, help='Number of keys to get per bucket')

###############################################
## Bucket names or lists
###############################################
#Given bucket name or list of names
parser.add_argument('-n', '--bucket_name', default="", help='Name to run')
parser.add_argument('-nl', '--name_list', default="", help='List of names to run')

###############################################
## String options
###############################################
parser.add_argument('-c', '--characters', default="", help='Characters to run via random/bruteforce, e.g. "abcdefg.."')
parser.add_argument('-nc', '--num_chars', type=int, help='Lenght of bucket name"')
# parser.add_argument('-nr', '--num_range_characters', default="", help='Range lenght of bucket names, e.g. 3-5"')
parser.add_argument('-ac', '--random_chars', action='store_true', help='Run random chars"')
parser.add_argument('-rc', '--all_chars', action='store_true', help='Run all chars')
parser.add_argument('-pp', '--prefix_postfix', action='store_true', help='Run with prefixes and postfixes')
parser.add_argument('-sa', '--start_after', default='', help='For all_chars, start after this string')


###############################################
## Optional
###############################################
#Rerun previously run buckets
parser.add_argument('--rerun', action='store_true', help="Rerun previously searched buckets")
#Test mode just to see the bucket names
parser.add_argument('-t', '--test', action='store_true', help="Test mode to just print the bucket names being run")

###############################################
## Debug Options
###############################################
parser.add_argument('-v', '--print_verbose', action='store_true', help="Print verbose (critical and errors)")
parser.add_argument('-vv', '--print_very_verbose', action='store_true', help="Print very verbose (critical, errors, and warnings")

#Compile the argument paser options
args = parser.parse_args()