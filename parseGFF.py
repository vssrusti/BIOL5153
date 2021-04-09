#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description='this script will parse a Gff file and extract each feature from the genome')

# add positional arguments (required and order matters)
parser.add_argument('gff', help='name of the GFF file')
parser.add_argument('fasta', help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# open and read in the FASTA file
genome = SeqIO.read(args.fasta, 'fasta')

# open and read in GFF file
with open (args.gff, 'r') as gff_in:
    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')

    # loop over all the lines in our reader object (i.e., parsed file)
    fasta = []
    for line in reader:
        start  = line[3]
        end    = line[4]
        strand = line[6]

        # feature header
        header = genome.id , line[8:10]

        # extracting the sequence
        feature_start = (int(line[3])) - 1
            # print (feature_start)
        feature_end = int(line[4])
            # print(feature_end)
        feature_seq = genome.seq[feature_start:feature_end]
            # print (feature_seq)
        
        # putting in FASTA format with header and appending the extracted sequences
        fasta.append('>%s\n%s' % (header, feature_seq))

# printing output in FASTA format
with open('assn06.fasta', 'w') as fasta_out:
    fasta_out.write('\n'.join(fasta))
