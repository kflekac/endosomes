"""
coding: utf-8
confidence_filtering.py
version 2.0
author: Kahli
usage: confidence_filtering.py

Takes three file names as input:
A) A MITAB 2.7 format \*.txt file that contains PPI data for the entire cellular system
B) A MITAB 2.7 format \*.txt file that contains PPI data extracted from (A) for a relevant sub-cellular system
C) An output file name

It then calculates a confidence (weight) value for that interaction. These are based on evidence type,
number of publications associated with each, publication throughput, and number of associated evidence methods.

Dependencies:
    python 2.7.13
    pandas v_0.20.3-py27_0
    numpy v_1.13.1
"""

import os
import sys
import pandas as pd
from collections import Counter

#Functions
# Log a message to stderr
def msg(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Log an error to stderr and quit with non-zero error code
def err(*args, **kwargs):
    msg(*args, **kwargs)
    sys.exit(1);

# Check file exists
def check_file(f):
    return os.path.isfile(f)

# Cleaning "pubmed:" str from a pubmed ID
def pmid_cleaner(pmid):
    pmid = str(pmid)
    if 'pubmed' in pmid:
        colon = pmid.find(":")
        pmid = pmid[colon + 1:]
    return pmid

# File names required
full_ppi_path = "H.Sapiens(pmid).txt"
network_ppi_path = "EECargoPreNetwork.txt"
#Optional output to different directory
output_path = ""

# Checking if file paths exist, etc
if not check_file(full_ppi_path):
    err('ERROR: Cannot find "{}". Check file exists in the specified directory.'.format(full_ppi_path))

if not check_file(network_ppi_path):
    err('ERROR: Cannot find "{}". Check file exists in the specified directory.'.format(network_ppi_path))

#Creating a counted collection of how often each unique PMID occurs throughout network
full_ppi_file = pd.read_table(full_ppi_path)

# Need 'Publication Identifier(s)' column to contain lists of unique elements, not str
full_ppi_file['Publication Identifier(s)'] = full_ppi_file['Publication Identifier(s)'].apply(lambda x: list(set(x.split("|"))))
pmid_count = Counter(pmid_cleaner(pmid) for pmid_list in full_ppi_file['Publication Identifier(s)'] for pmid in pmid_list)


# The extracted subcellular network file
network_ppi_file = pd.read_table(network_ppi_path)

# making the PMIDs and Methods columns into lists of unique elements
network_ppi_file['Publication Identifier(s)'] = network_ppi_file['Publication Identifier(s)'].apply(lambda x: list(set(x.split("|"))))
network_ppi_file["Interaction detection method(s)"] = network_ppi_file["Interaction detection method(s)"].apply(lambda x: list(set(x.split("|"))))


network_ppi_file['Num Publications'] = network_ppi_file['Publication Identifier(s)'].apply(len)
network_ppi_file["Num Methods"] = network_ppi_file['Interaction detection method(s)'].apply(len)
# This column contains the minimum count of the pmids listed in 'Publication Identifier(s)'
# Not the case for this file, but could cause bug if min == 0
network_ppi_file["Throughput"] = network_ppi_file['Publication Identifier(s)'].apply(lambda x: min([pmid_count[pmid_cleaner(pmid)] for pmid in x]))
# Create a new column, where Weight = (Num_Methods + Num_Pubs) / Throughput
network_ppi_file["Weight"] = network_ppi_file.apply(lambda row: (float(row["Num Methods"] + row["Num Publications"]))/float(row["Throughput"]), axis = 1)


# Writing weight un/filtered tab-delim *.txt
unfiltered_out_path = output_path + "/weighted_ppi_file.txt"
network_ppi_file.to_csv(unfiltered_out_path, sep = "\t", index = False)

# OPTIONAL: Filter and write your network file based on the weight column
filtered_ppi = network_ppi_file[network_ppi_file["Weight"]>= 0.5] #Change as required
filtered_out_path = output_path + "weighted_0.5_ppi_file.txt"
filtered_ppi.to_csv(filtered_out_path, sep = "\t", index = False)
