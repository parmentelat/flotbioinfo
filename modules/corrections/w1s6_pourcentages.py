# -*- coding: utf-8 -*-
from nbautoeval.exercice_function import ExerciceFunction
from nbautoeval.args import Args

nucleotides = 'CAGT'
# @BEG@ name=pourcentages
def pourcentages(adn):
    "calcule des pourcentages de CAGT dans un adn"
    total = len(adn)
    return {
        nucleotide : len([p for p in adn if p == nucleotide])*100./total
        for nucleotide in nucleotides
    }
# @END@

def pourcentages_ko():
    return { p:0.25 for p in nucleotides }

from samples import slides

inputs_pourcentages = [
    Args('ACGTACGA'),
    Args('ACGTACGATCGATCGATGCTCGTTGCTCGTAGCGCT'),
    # la séquence du transparent 1.6
    Args(slides['1.6']),
]

exo_pourcentages = ExerciceFunction(pourcentages, inputs_pourcentages,
                                    layout='pprint',
                                    layout_args=(40, 25, 25),
)
