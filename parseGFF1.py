#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO
from collections import defaultdict


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

list = []

# open and read in GFF file
with open (args.gff, 'r') as gff_in:

    # create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')

    # loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
        # starting of the sequence
        start  = line[3]
        # end of the sequence
        end    = line[4]
        # strand of chromosome
        strand = line[6]
        # CDS specification
        feature = line[2]
        # semicolon delimited list of feature description
        desp = line[-1]

        # extracting the sequence
        feat_start = int(line[3]) - 1
        feat_end = int(line[4])

        # extracting just the exons (CDS)
        if feature == 'CDS':

            # extracting needed features from list
            desp_split = desp.split(';')
            gene_info = desp_split[0]
            gene = gene_info[5:]

            # adding trailing whitespaces so that all sequences start at same spot
            gene_len = len(gene)
            space_add = 16 - gene_len
            spaces = ' ' * space_add

            # accounting for some sequences on the reverse strand
            if strand == '-': 
                rev_feat_seq = genome.seq[feat_start:feat_end].reverse_complement()
                list.append(gene + spaces + rev_feat_seq)
                #print(str(len(spaces)) + rev_feat_seq)
            else:
                feat_seq = genome.seq[feat_start:feat_end]
                list.append(gene + spaces + feat_seq)
                #print(str(len(spaces)) + feat_seq)

        else: 
            continue
        
# sort the list by gene name and exon number
list.sort()
# print(*list , sep="\n")

# dictionary: key = gene name, value = sequence
gene_dict = defaultdict(dict)

# header name
const = ">Citrullus_lanatus_"

# looping through to add keys of gene names and sequence values to those keys
for s in list:
    gene_name = const + s[0:5] + "\n"
    gene_seq = s[16:]
    # print(gene_name)
    # print(gene_seq)

    # build dictionary
    # test whether this key (gene names) exists in the dictionary
    # if it exists, concatenate the sequences of the exons
    if gene_dict[gene_name]:
        gene_dict[gene_name] += gene_seq
    
    # if it doesn't exist, add sequences to the key
    else:
        gene_dict[gene_name] = gene_seq

# loop over dictionary
for i,j in gene_dict.items():
    print(i,j)
