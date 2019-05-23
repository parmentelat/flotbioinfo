def translate_dna_to_rna(dna):
    """"
    Translates a DNA string into its RNA counterpart
    by replacing all occurrences of T into U
    """
    rna = ""
    for nucleo in dna:
        # replace a Thymine into Uracile
        if nucleo == 'T':
            rna += "U"
        else:
            rna += nucleo
    return rna
