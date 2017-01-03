# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

nucleotides = 'CAGT'

# @BEG@ name=count_gc_at
def count_gc_at(dna):
    """
    calcul des pourcentages de GC et de AT dans un dna
    """
    total = len(dna)
    nb_gc = 0.
    for nucleo in dna:
        if nucleo in "GC":
            nb_gc += 1
    return ( nb_gc / total, (total - nb_gc) / total)
# @END@

def count_gc_at_ko(dna):
    return (0.25, 0.75)

raw = """
    CCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAA
    TTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGG
    TATAGGCATAGCGCACAGACAGATAAAAATTACAGAGTACACAACATCCA
    ATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGACGCGT
    CCCGCACCTGACAGTGCGGGCTTTTTTTTTCGACCAAAGGTAACGAGGTA
    GTTCGGCGGTACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCG
    AGGCAGGGGCAGGTGGCCACCGTCCTCTCTGCCCCCGCCAAAATCACCAA
    AAAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
    GACGGGACTCGCCGCCGCCCAGCCGGGGTTCCCGCTGGCGCAATTGAAAA
    GCCCAAATAAAACATGTCCTGCATGGCATTAGTTTGTTGGGGCAGTGCCC
"""

inputs_count_gc_at = [
    Args(line.strip()) for line in raw.split("\n") if line
]

exo_count_gc_at = ExerciseFunction(
    count_gc_at,
    inputs_count_gc_at,
    layout='pprint',
    layout_args=(40, 25, 25),
)
