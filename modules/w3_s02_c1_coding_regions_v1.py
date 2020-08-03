#!/usr/bin/env python
# coding: utf-8

# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>François Rechenmann &amp; Thierry Parmentelat</span>
# <span><img src="media/inria-25-alpha.png" /></span>
# </div>

# # Searching coding regions on a phase

# In this notebook we will write a python implementation of the algorithm presented in the video, that searches a coding region in a DNA fragment. In this first version we will focus on a single phase. Remember there can be three phases on a DNA fragment, whether codons are made up from index 0, 1 or 2.

# ### Searching in DNA or in RNA

# In the videos, we have seen the *Start* and *Stop* codons as containing `U` - and not `T`. Let us first notice that it is of course equivalent to search for `AUG` in RNA or `ATG` in the corresponding DNA.
# 
# So for practical reasons, since the genetic material that we start from almost always are DNA, in all the notebooks this week we will look for codons with `T` and not `U`.

# ### Looking for markers

# Like in the video, we assume that we have use ready-to-use functions for locating *Start* and *Stop* sequences. For now we will import these function from another module, but no worries, in the next sequence we will study how to write these ourselves.

# In[ ]:


# importing searching functions from the next sequence
from w3_s03_c2_next_codon import next_start_codon, next_stop_codon


# Remember that:
# 
# * indices in python start at 0
# * the **Start** codon reads `ATG`
# * the **Stop** codons can be either `TAA` or `TAG` or `TGA`

# Besides, please be aware that the two functions that we have imported:
# 
# * expect in argument a string `dna` and a starting `index`
# * and return, either the index for the next occurrence from (including) `index` **and on the same phase**, or `None` if there is no further occurrence beyond `index`.
# 
# So for example:

# In[ ]:


# here we find START because the search starts at index 0
# and ATG is at index 6, and so on the same phase
#next_start_codon("CGTACGATG", 0)


# In[ ]:


# on the other hand here, nothing can be found 
# because the starting index is on a different phase 
# than the one where ATG is located
#next_start_codon("CGTACGATG", 1)


# ### The  `break` statement

# Our code is going to use the `break` statement, that allows to abruptly exit a loop, and so to move to the instruction right after the loop. This feature is often used in conjunction with and **endless loop**, like in this example:

# In[ ]:


# an apparently endless loop
#counter = 1
#while True:
#    # the counter is doubled
#    counter += counter
#    # once we reach 100, we get out of the loop
#    if counter >= 100:
#        break
#    print("counter = ", counter)
#print("after the loop")


# ### The algorithm

# With all this at aour disposal, we can write a function `coding_regions_one_phase` that works on a DNA fragment, and that implements the logic described in the video. Our function expects  the following arguments:
# 
# * a DNA fragment
# * start phase, expressed as an integer 0, 1 or 2
# * the minimal size between 2 **Stop**s; this last argument is optional, and when omitted it will be taken as 300, like in the course.
#   
# Which leads us to the following code:

# In[ ]:


# searching genes according to the heuristic detailed in the video
# on a single phase
# by default, minimal size is 300
def coding_regions_one_phase(dna, phase, minimal_length=300):
    # initializing index
    # remember that next_start_codon and next_stop_codon 
    # always remain on the same phase
    index = phase
    # we return results as a list of couples 
    # [start_gene, stop_gene]
    genes = []
    # stop1 if the stop "on the left hand side"
    # at this point, it is the first stop on the phase
    stop1 = next_stop_codon(dna, index)
    # if we have no stop at all in the sequence, we're done
    if not stop1:
        return genes
    # main loop
    while True:
        # look for next stop after stop1
        # which is the "right hand side" stop
        stop2 = next_stop_codon(dna, stop1 + 3)
        # if there is none, we are done
        if not stop2:
            return genes
        # also it needs to be far enough
        if stop2 - stop1 < minimal_length:
            # too short : we skip this fragment
            stop1 = stop2
            continue
        # at this point, we found an ORF, we just need to find the correct Start
        start = next_start_codon(dna, stop1)
        # if there is none, it means we will not find anything more
        # and so we are done
        if not start:
            return genes
        if stop2 - start < minimal_length:
            # if the region is too small, we ignore it
            pass
        else:
            # this time, we found a gene, we add it to the results
            genes.append( [start, stop2] )
        # we can move on to the next ORF
        stop1 = stop2


# ### On a real example

# Let use try this out on the DNA from [Bacillus subtilis](http://www.ebi.ac.uk/ena/data/view/CP010053) (key `CP010053`), that because of its size, we have preloaded:

# In[ ]:


#from samples import subtilis
#print("subtilis has {} bases".format(len(subtilis)))


# In[ ]:


# let us compute genes on phase 0
#genes = coding_regions_one_phase(subtilis, 0)
#print("We found {} genes on phase 0".format(len(genes)))


# ### A few statistics (optional)

# For those who are interested, and who have some additional knowledge of python, here are a few statistics on this result. 

# In[ ]:


# the array of the genes lengths
#array_of_lengths = [ y-x for x,y in genes ]

# total length of all found genes
#total_length = sum ( array_of_lengths )
# the average length of genes
#average_length = total_length / len(genes)
#print('average gene length', average_length)


# In[ ]:


# minimal and maximal size
#length_min = min ( array_of_lengths )
#length_max = max ( array_of_lengths )
#print("min = {}, max = {}".format(length_min, length_max))


# In[ ]:


# percentage of the coding region wrt total length
#print("Percentage of coding region", total_length/len(subtilis))


# ##### A histogram with gene lengths

# It is easy to represent how gene lengths are distributed, as follows. Again this is given as a way to tease your curiosity, feel free to share your thoughts and ideas in order to improve final layout:

# In[ ]:


# importing matplotlib
#import matplotlib.pyplot as plt
# display inside the notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# sizes
#import pylab
#pylab.rcParams['figure.figsize'] = 8., 8.


# In[ ]:


# a histogram of lengths
#plt.hist(array_of_lengths, bins=75)
#plt.axis([300, 7700, 0, 400])
#plt.show()


# ### Notice on style

# Let us end up with outlining that very many improvements are possible, as much about programing style as about performance. For example we could have defined a `Gene` class, and then we would have returned a list of `Gene` objects rather that a list of lists; or at least, we could have used tuples rather than lists. I will leave to you these improvements, but our predefined choice is to focus on the algorithms themselves and to use python at a level that is as simple as possible.
