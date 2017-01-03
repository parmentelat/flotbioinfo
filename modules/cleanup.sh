#!/bin/sh
# a simple utility to do a first-pass cleanup on .py files
# downloaded from a notebook
# this is for the few notebooks that are imported in other notebooks
# we have 5 of them as of jan. 2017
#
# this script is best-effort, it comments off print() statements
# it was off with e.g. w2_s02_c1_translate_dna_rna because of a multi-line print
#

for file in "$@"; do
    sed -i \
	-e "s,^\( *print(\),#CLEANUP \1," \
	$file
done
