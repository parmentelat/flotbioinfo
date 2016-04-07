# -*- coding: utf-8 -*-
from nbautoeval.exercice_regexp import ExerciceRegexp, ExerciceRegexpGroups
from nbautoeval.args import Args

######################################## au_moins_deux
germs = [ 'AGCT', 'CAGT', 'TATG', 'CGTA' ]

import itertools

inputs =  []
inputs += ['AGCTTATATATACAGT']
inputs += [
    "".join(x) for x in itertools.permutations(germs)
    ]

# XXX @BEG@ week=6 sequence=6 name=pythonid more=regexp
au_moins_deux = "TA(TA)+"
# @END@

exo_au_moins_deux = ExerciceRegexp('au_moins_deux',
                                   au_moins_deux,
                                   [Args(x) for x in inputs],
                                   match_otherwise_search = False,
                                   exemple_how_many = 8)
au_moins_deux_ko = "TATA"

