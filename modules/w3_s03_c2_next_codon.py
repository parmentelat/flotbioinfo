#!/usr/bin/env python
# coding: utf-8

# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>François Rechenmann &amp; Thierry Parmentelat</span>
# <span><img src="media/inria-25-alpha.png" /></span>
# </div>

# # `next_start_codon` and `next_stop_codon`

# Let us now remember the algorithm that searches for coding regions, that we have seen in the previous sequence, and in which we have been using two utility functions to locate **Start** and **Stop** codons. Here is the code that we used at that time, and that uses the concepts that we just saw in the notebooks on searching patterns in strings in python.

# ### The `%` operator for computing moduli

# In the following code, we will use the '%' operator that computes the modulo - i.e. the rest in integer division - between two numbers. For example:

# In[ ]:


# 25 = 2 * 10 + 5 
#print("the rest of 25 divided by 10 is", 25 % 10)


# ### The `continue` statement

# Our code this time uses the `continue` statement, that allows to exit the current loop (here a `for` loop) and to **move to the next iteration**.

# In[ ]:


# an example with a `continue` statement
# the main loop scans numbers 0, 1, 2, 3 and 4
#for i in range(5):
#    # but we decide to ignore multiples of 3
#    # and so in this case we just go to the next item in the loop
#    if i % 3 == 0:
#        continue
#    print("dealing with", i)    


# ### `next_start_codon` : searching a triple on one phase

# We can now write the code for `next_start_codon`:

# In[ ]:


# reminder : the value for the START codon
start_codon = "ATG"


# In[ ]:


# the function used when looking for coding regions
def next_start_codon(dna, start):
    """
    locates the next START codon from index start
    and on the same phase as start
    
    returns None when there is no further match
    """
    # starting at index start
    index = start
    # while we can find a START codon
    while True:
        # looking for a START from that position
        index = dna.find(start_codon, index)
        # nothing left 
        if index == -1:
            return None
        # if we are not on the same phase as start, we ignore that place
        if (index - start) % 3 != 0:
            # in this case we need to move forward a little,
            # otherwise we will stay here forever
            index += 3
            # and we proceed with the search 
            continue
        # here there is a match on the right phase, we can return this
        return index


# Let us convince ourselves that the function behaves as expected, with a small test that should cover most cases:

# In[ ]:


#dna = "ATGCGATGTATGCGTGCAGCTGCTAGCTCGTAATGTCGTCATGGATCATCGATCATGG"

#for phase in 0, 1, 2:
#    print("PHASE", phase)
#    next = phase
#    while next is not None:
#        next = next_start_codon(dna, next)
#        if next is not None:
#            print("found at index", next, dna[next:next+3])
#            next += 3


# ##### `next_stop_codon` : searching any of 3 triples on a phase

# Following a very similar appraoch, we can also now write `next_stop_codon`:

# In[ ]:


# the regular expressions module
import re
# reminder : the possible values for the STOP codon
# we use a logical OR `|` to search for either 'TAA' or 'TAG' or 'TGA'
re_stop = re.compile("TAA|TAG|TGA")


# In[ ]:


def next_stop_codon(dna, start):
    """
    locates next STOP codon, starting at index start
    and on the same phase as start

    returns None when no further match can be found
    """
    # we start at index start
    index = start
    # as long as necessary
    while True:
        # search a STOP from current index
        match = re_stop.search(dna, index)
        # nothing left to find
        if match is None:
            return None
        # if not on the same phase as start, discard this match
        index = match.start()
        if (index - start) % 3 != 0:
            # like above, we need to move forward a bit
            index += 3
            continue
        # we have a match on the right phase
        return index


# And here again, we can run a quick sweep for testing this function:

# In[ ]:


#print(dna)
#for phase in 0, 1, 2:
#    print("PHASE", phase)
#    next = phase
#    while next is not None:
#        next = next_stop_codon(dna, next)
#        if next is not None:
#            print("found at index", next, dna[next:next+3])
#            next += 3

