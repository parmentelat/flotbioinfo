# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

from nbautoeval.exercice_function import ExerciceFunction
from nbautoeval.args import Args

nucleotides = 'CAGT'

# @BEG@ name=calcul_gc_at
def calcul_gc_at(adn):
    """
    calcul des pourcentages de GC et de AT dans un adn
    """
    total = len(adn)
    nb_gc = 0.
    for nucleo in adn:
        if nucleo in "GC":
            nb_gc += 1
    return ( nb_gc / total, (total - nb_gc) / total)
# @END@

def calcul_gc_at_ko(adn):
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

inputs_calcul_gc_at = [
    Args(line.strip()) for line in raw.split("\n") if line
]

exo_calcul_gc_at = ExerciceFunction(calcul_gc_at,
                                    inputs_calcul_gc_at,
                                    layout='pprint',
                                    layout_args=(40, 25, 25),
)
