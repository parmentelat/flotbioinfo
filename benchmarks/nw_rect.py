# coding: utf-8

def insertion_cost(base):
    return 1

def substitution_cost(base1, base2):
    return 1 if base1 != base2 else 0

def init_costs(len1, len2):
    return [ [ 0 for j in xrange(len2 + 1)] for i in xrange(len1 + 1)]

def phase1(dna1, dna2):
    len1 = len(dna1)
    len2 = len(dna2)
    costs = init_costs(len1, len2)

    for c in xrange(len1 + len2 + 1):
        inf = max(0, c - len2)
        sup = min(c, len1)
        for i in xrange(inf, sup+1):
            j = c - i
#            print("i=", i, "j=", j)
            if i == 0 and j == 0:
                costs[i][j] = 0
            elif j == 0:
                costs[i][j] = costs[i-1][j] + insertion_cost(dna1[i-1])
            elif i == 0:
                costs[i][j] = costs[i][j-1] + insertion_cost(dna2[j-1])
            else:
                costs[i][j] = min(
                    costs[i-1][j-1] + substitution_cost(dna1[i-1], dna2[j-1]),
                    costs[i][j-1] + insertion_cost(dna2[j-1]),
                    costs[i-1][j] + insertion_cost(dna1[i-1]))
    return costs

def distance(dna1, dna2):
    return phase1(dna1, dna2)[-1][-1]

import sys
def main():
    if len(sys.argv) == 1:
        dimension = 2000
    else:
        dimension = int(sys.argv[1])
    a = dimension * 'a'
    b = dimension * 'b'
    print(distance(a, b))

main()
