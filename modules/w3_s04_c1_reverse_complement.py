#!/usr/bin/env python
# coding: utf-8

# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>François Rechenmann &amp; Thierry Parmentelat</span>
# <span><img src="media/inria-25-alpha.png" /></span>
# </div>

# # Computing the reverse complement sequence

# ### One nucleotide's `complement`

# In order to compute the reverse complement sequence for a DNA fragment, we start by defining a dictionary `complement` that maps one nucleotide to its complement:

# In[ ]:


# complement nucleotide
complement = {
    'A' : 'T',
    'C' : 'G',
    'G' : 'C',
    'T' : 'A',
}


# So for example:

# In[ ]:


#complement['A']


# ### The logic for our computation

# We can now compute the reverse complement sequence, and for that we will
# 
# * compute the **list** of complement nucleotides, in their initial order, using a comprehension;
# * reverse that list *in place* using the `reverse` method on lists;
# * finally translate this list back into a string.

# ### Digression: translate a list into a string

# For that last step, we will use a very common trick in python programs, based on the `join` method on strings. Here are a few examples:

# In[ ]:


# The join method on strings
#"+".join(["spam", "eggs", "bacon"])


# As can be seen, the string that is the subject of `join` (in the above case `"+"`) is used to join the various pieces sent as arguments.
# 
# So by extension, if `join` is sent on **an empty string**, then we de facto implement the conversion from a list to a string, like this:

# In[ ]:


#"".join(["s", "p", "a", "m"])


# ### Putting it together

# All these pieces acn be put together and lead us to the following code, for computing the reverse complement of a DNA fragment:

# In[ ]:


def reverse_complement(dna):
    """
    Computes reverse (first in, last out) complement (A->T, etc..)
    of a DNA fragment
    """
    # the list of complement nucleotides
    complements = [ complement[nucleo] for nucleo in dna]
    # reverse this list in place
    complements.reverse()
    # we just need to translate back into a string
    return "".join(complements)


# ### Examples

# Using the example from the video and related slides:

# In[ ]:


#from samples import sample_week3_sequence4
#print(sample_week3_sequence4)


# In[ ]:


# we get this
#reverse_complement(sample_week3_sequence4)


# Or again on a smaller input sample:

# In[ ]:


#reverse_complement("TAGCATCG")


# And now on a much larger sample, to get an idea of the algorithm's performance:

# In[ ]:


#from samples import subtilis
#print("subtilis has {} bases".format(len(subtilis)))


# In[ ]:


#i_subtilis = reverse_complement(subtilis)
# we only display the first 60 bases
#print(i_subtilis[:60])


# ### Involution

# When applied twice, the `reverse_complement` function should give us back our initial input - in pedantic language, this is called an involution. I will let you check this as an exercise:

# In[ ]:


# try to run reverse_complement twice in a row
# and check that you find the input back

