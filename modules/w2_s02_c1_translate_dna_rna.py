
# coding: utf-8

# <span style="float:left;">Licence CC BY-NC-ND</span><span style="float:right;">François Rechenmann &amp; Thierry Parmentelat&nbsp;<img src="media/inria-25.png" style="display:inline"></span><br/>

# # Translating DNA into RNA

# In this notebook we will implement the very simple algorithm that translates DNA into corresponding RNA, after our usual python2/python3 compatibility cell:

# In[ ]:

# this is so that we can use print() in python2 like in python3
from __future__ import print_function
# with this, division will behave in python2 like in python3
from __future__ import division


# ### The algorithm

# The job is obviously as simple as it gets. Our first naive version is to create an empty string that we fill as we go. When doing this we will use the `+` operator on strings, that allows to create a new chain, as can be seen here:

# In[ ]:

# from two strings
st1 = "abc"
st2 = "def"
# using + we get the concatenation 
concatenated = st1 + st2
#CLEANUP print(concatenated)


# In[ ]:

# notice that the two input strings are unchanged
#CLEANUP print("st1:", st1, "st2:", st2)


# Also notice that python comes with a `+=` shorthand, that behaves like this:

# In[ ]:

# from one string
string = "ATGC"
# we can easily add at its end
string += "CGAT"
# and now string contains both parts
#CLEANUP print(string)


# Thanks to this concatenation operation on strings, we can implement our translation algorithm like this:

# In[ ]:

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


# Then for example:

# In[ ]:

dna = "ATTCGATCGGGTATTACG"
rna = translate_dna_to_rna(dna)
#CLEANUP print(rna)


# ### Performance consideration (advanced)

# This section is optional, and targets those of you who have more advanced notions of python than what we have seen so far. 
# 
# I would like to draw your attention on the `timeit` module, that is designed to help you measure the performance of a code fragment. For example, if we wanted to see how much time this translation function requires, we could write:

# In[ ]:

# import the timeit module that does performance measurements
import timeit

# let us use a somewhat larger sample - around 400 000 nucléotides
big_dna = 10**5 * 'ACGT' 

#CLEANUP print(timeit.timeit('translate_dna_to_rna(big_dna)', 
                    "from __main__ import translate_dna_to_rna, big_dna",
                    number=10))


# In my environment, this prints something in the order of `0.5` (seconds), which tells us that for evaluating 10 times (this is what `number=10` is here for) the call to `translate_dna_to_rna(big_dna)`, it takes around a half second.
# 
# The second argument to `timeit`, in our case `from __main__ import translate_dna_to_rna, big_dna`, allows to expose to `timeit` the 2 symbols that we need (the function and the sample). 
