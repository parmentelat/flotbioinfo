#!/usr/bin/env python
# coding: utf-8

# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>François Rechenmann &amp; Thierry Parmentelat</span>
# <span><img src="media/inria-25-alpha.png" /></span>
# </div>

# # Needleman and Wunsch algorithm

# ## Iterative form

# ### Cost functions

# Let us use same code for the cost functions, as the ones we had for the first, recursive, version of this algorithm:

# In[ ]:


# the simplest insertion cost function
def insertion_cost(base):
    return 1


# In[ ]:


# the simplest possible substitution cost
def substitution_cost(base1, base2):
    return 1 if base1 != base2 else 0


# ### Sweeping along diagonal lines

# Before we tackle the algorithm itself, let us see how to write a code that scans *along diagonal lines* as is described in the video.
# 
# For that, let us notice that all the dots on one diagonal line all satisfy $i + j = c$, and that when increasing the `c` constant we can browse all the diagonal lines.
# 
# ![Scanning along diagonal lines](media/diagonal.png)

# Here again, some care must be brought when studying limits: the maximum value for `c` is in our case the sum of the input strings lengths **inclusive**. Also bear in mind that `range(n)` spans only up to `n-1` inclusive, and this is why we use twice an expression like `range(n + 1)` in the code. 

# So we can scan all the $(i, j)$ couples for the whole rectangular array like this:

# In[ ]:


# the skeleton for a diagnoal scanning
def sweep(dna1, dna2):
    len1 = len(dna1)
    len2 = len(dna2)
    
    # we need to go up to len1 + len2 inclusive
    for c in range(len1 + len2 + 1):
        print(10*'*', "diagonal c =", c)
        # here again we want the dots on the 2 limits
        # and so we need to add 1 to c
        for i in range(c + 1):
            # given c, j is deduced from i 
            j = c - i
            # we only consider the dots in the rectangle
            # here again we want to keep the edges, hence '<=' 
            if 0 <= i <= len1 and 0 <= j <= len2:
                print(i, j)


# So for input values being respectively `ABC` and `AC` ![](media/nw-indices.png)

# In[ ]:


# here is how our sweeping goes 
#sweep("ABC", "AC")


# ### Double entry arrays

# In order to write the first phase of the algorithm, we only miss a small detail. First phase is about elaborating a double-entry array - that is to say, an array that has a value attached for each couple $(i, j)$. 
# 
# We have not yet maniuplated any such array in python, mostly because the language does not offer this capability, at least not in as a straightforward way as languages like C or C++.
# 
# There are several ways to achieve a close enough result. The first one is about using a list of lists. It is rather simple, and it looks like this:

# ##### A list of lists

# In[ ]:


# creating a double array as a list of lists
rectangle = [
    [0, 1, 2],
    [10, 11, 12],
]


# We already know how to deal with this object since it is a list, and so we can access its first level contents - a simple list - like this:

# In[ ]:


# one indexing level
#rectangle[1]


# which can be indexed itself again:

# In[ ]:


# two indexing levels
#rectangle[1][2]


# This first technique works well, and relies on a rather pleasant syntax. However, it requires some care for initialization. Here is one possible way to initialize it properly:

# In[ ]:


def init_costs(len1, len2):
    """
    Creates a list of len1 + 1 lists
    each having len2 + 1 elements 
    each initialized to 0
    """
    return [ [ 0 for j in range(len2 + 1)] for i in range(len1 + 1)]


# So if we use this with our sample input, we correctly obtain:

# In[ ]:


# using data from the figure
#len1 = 3
#len2 = 2

#costs = init_costs(len1, len2)

#print(costs)


# ##### Another method

# For those of you who would be curious to learn a bit more about python, we will see in the next (optional) notebook another appraoch to implement such double-entry arrays, based on a dictionary hashed on tuples. But for now let us see how to implement the first phase of Needleman and Wunsch.

# ### First phase

# We now have everything we need to write the iterative version of Needleman and Wunsch:

# In[ ]:


def phase1(dna1, dna2):
    """
    First phase of an iterative Needleman and Wunsch
    
    Computes the array of costs through a diagonal sweep

    We obtain an array of size
      [len(dna1) + 1] x [len(dna2) + 1]

    this data is returned by this function
    """
    # initializations
    len1 = len(dna1)
    len2 = len(dna2)
    # result array is initialized with zeros
    costs = init_costs(len1, len2)

    # diagonal sweep - like above
    for c in range(len1 + len2 + 1):
        for i in range(c + 1):
            # j is computed from c and j
            j = c - i
            # only dots within the rectangle are considered
            if 0 <= i <= len1 and 0 <= j <= len2:
                if i == 0 and j == 0:  # upper left corner
                    costs[i][j] = 0
                elif j == 0:           # on an edge : insertion 
                    costs[i][j] = costs[i-1][j] + insertion_cost(dna1[i-1])
                elif i == 0:           # the other edge : insertion
                    costs[i][j] = costs[i][j-1] + insertion_cost(dna2[j-1])
                else:                  # in the middle
                    costs[i][j] = min(
                        # substitution
                        costs[i-1][j-1] + substitution_cost(dna1[i-1], dna2[j-1]),
                        # insertion
                        costs[i][j-1] + insertion_cost(dna2[j-1]),
                       # insertion
                        costs[i-1][j] + insertion_cost(dna1[i-1]))
    # result is returned to caller
    return costs


# ### Distance

# Notice that the valuable result, in such a costs array, is the bottom right element; in order to access it, we can use a trick in python's indexing, which is that `array[-1]` returns last element in `array`:
# 

# In[ ]:


# a list
#l = [0, 12, 47]
#l[-1]


# In[ ]:


# and so we can access the overall distance like this 
def distance(dna1, dna2):
    return phase1(dna1, dna2)[-1][-1]


# ### A few examples

# If we start with the same - small - examples as the ones we had used for the recursive version:

# In[ ]:


#phase1("ACTG", "ACTC")


# In[ ]:


#phase1("ACGTAGC", 
#       "ACTGTAGC")
#          ^           


# In[ ]:


#phase1("ACTGCCAAC", "ACTGCGCAAC")


# ### Performances

# With this iterative version, it is now possible to run that method on much bigger inputs:

# In[ ]:


#from samples import sample_week4_sequence9 as original
#print("original is {} long".format(len(original)))
#print("original[600]=", original[600])


# Let us now create artificial differences by inserting and changing slightly the original sample:

# In[ ]:


# we insert a 'C' at index 300,  and replace the 'A' at index 600 with a 'G'
#fake = original[:300] + 'C' + original[300:600] + 'G' + original[601:]
#
#costs = phase1(original, fake)
#print("We find distance", costs[-1][-1])


# As you can see, this algorithm already is more efficient; however as it is quadratic (we must compute around $n^2$ values) this input with about 800+ bases already leads us to a few seconds of computation. 

# ### Phase 2

# For the second phase, we are simply going to compute two strings of characters, that will let us outline the differences between the 2 input strings. Because in our context it it not too easy to use colours or other typographic means, we will print out something like this:
# 
# `ACCTC-TGTATCT*A*TTCGGCATCGATCAT`
# 
# `ACCTCGTGTATCT*C*TTCGGCATC-ATCAT`
# 
# So as can be seen on this example:
# 
#   * insertions are rendered with a '-' in the shorter string,
#   * and substitutions are rendered with a pair of `*` around the area of interest.

# We start with a utility function that adds special `*` characters around a character when needed (i.e. when the `same` parameter is false):

# In[ ]:


# a utility function that adds '*' around one character
# when 'same' est false
def outline(char, same=True):
    return char if same else "*{}*".format(char)


# Now we can write the code for `phase2`, a function that returns 2 character strings ready to be printed on top of one another. For efficiency reasons, we crop the result in two lists (`r1` and `r2`) that moreover are built from the end, due to the direction for the scan that starts from the end; `r1` and `r2` are properly reversed and translated into strings before they are returned to the caller:

# In[ ]:


# one possible way to write a phase2
def phase2(dna1, dna2, costs):
    """
    From two DNA strings, and their costs array as computed with phase1,
    we return 2 printable strings designed to be displayed on top of
    one another, so as to outline differences
    
    Insertions are marked with a -, and substitutions 
    are surrounded with a pair of * signs
    """
    # start from the bottom right corner
    i = len(dna1)
    j = len(dna2)
    # preliminary results, but as reversed lists
    r1 = []
    r2 = []
    ### scanning per se
    # we stop when i==0 AND j==0
    while i > 0 or j > 0:
        # current value
        c = costs[i][j]
        # if on an edge, we cannot use formulas that involve
        # i-1 ou j-1, we need to deal with these cases separately
        if i == 0:                  # edge = insertion
            r1.append("-")
            j -= 1
            r2.append(dna2[j])
        elif j == 0:                # edge = insertion
            i -= 1
            r1.append(dna1[i])
            r2.append("-")
        # in the middle, we look for the direction that the minimum comes out of
        elif c == costs[i-1][j-1] + substitution_cost(dna1[i-1], dna2[j-1]):  # substitution
            # is it a true substitution ? 
            same = dna1[i-1] == dna2[j-1]
            i -= 1
            r1.append(outline(dna1[i], same))
            j -= 1
            r2.append(outline(dna2[j], same))
        elif c == costs[i][j-1] + insertion_cost(dna2[j-1]):    # insertion
            r1.append('-')
            j -= 1
            r2.append(dna2[j])
        elif c == costs[i-1][j] + insertion_cost(dna1[i-1]):    # insertion
            i -= 1
            r1.append(dna1[i])
            r2.append('-')

    # at this point, we need to reverse the lists, and translate them into strings
    s1 = "".join(reversed(r1))
    s2 = "".join(reversed(r2))
    return s1, s2


# In[ ]:


# we can now write a convenience function
def needleman_wunsch(dna1, dna2):
    # compute costs with phase1
    costs = phase1(dna1, dna2)
    # compute distance
    d = costs[-1][-1]
    # run phase2
    s1, s2 = phase2(dna1, dna2, costs)
    # display result
    print("distance = ", d)
    print(s1)
    print(s2)


# In[ ]:


# and on an example this gives us
#sample1 = "ACCTCTGTATCTATTCGGCATCGATCAT"
#sample2 = "ACCTCGTGTATCTCTTCGGCATCATCAT"

#needleman_wunsch(sample1, sample2)


# You can also play with more substantial changes:

# In[ ]:


# from a 35-bases DNA
#sample3 = "ACCTCTGTATCGGCATCGATACGCAACGGTTCCGA"
#print("size sample3", len(sample3))


# In[ ]:


# we insert pieces at 2 locations
#sample4 = sample3[:10] + 'CTATTGC' + sample3[10:20] + 'CATTGCTTGG' + sample3[20:]
#print("size sample4", len(sample4))


# In[ ]:


# and our algorithm produces this
#needleman_wunsch(sample3, sample4)


# You can notice some fuzziness at the place where insertions occurred, but for the most part, common pieces are correctly identified.

# ## Going further

# In the next notebook, we will deepen this topic for those of you that are interested in 
# 
# * performance and scaling issues
# * another way to implement double-entry arrays, using a dictionary indexed by tuples.
