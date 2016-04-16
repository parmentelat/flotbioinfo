# -*- coding: utf-8 -*-

def translate_adn_to_arn(adn):
    """"
    Traduit un brin d'ADN en ARN en remplaçant toutes
    les occurrences de T en U
    """
    arn = ""
    for nucleo in adn:
        # traduire une Thymine en Uracile
        if nucleo == 'T':
            arn += "U"
        else:
            arn += nucleo
    return arn
