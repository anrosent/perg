#!/usr/bin/env python3
#
# perg.py: Generates a stream of strings (roughly) uniformly sampled
# from the set of strings matching a given regex
#
# anrosent (anson.rosenthal@gmail.com)
import perg
from random import choice, randint, random

# Repeat probability for samples on infinite repitition intervals
INF_REPEAT_P = 0.8


# Draws a sample from the geometric distribution on [start, inf) with success
# parameter p
def sample_geometric(p, start=0):
    ctr = start
    while random() < p:
        ctr += 1
    return ctr

# Trival sample from literally matching strings
def sample_literal(x): return chr(x)

# Sample from on of the predefined character categories
def sample_category(c):
    return choice(perg.CATEGORIES[c])


# Sample from a range of ASCII values 
# e.g. a-z, A-Z, 0-9
def sample_range(rg):
    s, e = rg
    return chr(randint(s, e+1))


# Sample from one of the regexes in the matching set
def sample_branch(bs):
    _, d = bs
    return sample(choice(d))


# Sample from the set of matching characters 
def sample_in(opts):
    return sample_single(choice(opts))


# Sample repitition interval for given regex
def sample_max_repeat(node):

    # Unpack start, end of repitition interval and regex to repeat
    s, e, d = node

    # If bounded repitition, sample uniformly
    if e < 4294967295:
        repititions = randint(s,e)
    else:
        
        # Interval is unbounded above, so sample geometric distribution
        repititions = sample_geometric(INF_REPEAT_P, s)

    return ''.join(sample(d) for _ in range(repititions))


# NOTE: considered equivalent to sampling from greedy repeat matcher.
# May or may not be completely equivalent
def sample_min_repeat(node):
    return sample_max_repeat(node)


# Match any character
def sample_any(d):
    return choice(string.printable)


# Sample from subpattern and cache for backreferences
# FIXME: still doesn't handle assert and assert_not subpatterns
def sample_subpattern(p):
    subpattern_id, d = p
   
    # Sample subpattern and cache
    sampled = sample(d)

    # Check if captured subpattern
    if subpattern_id:
        SUBPATTERNS[subpattern_id] = sampled

    return sampled 


# Lookup referenced group and sample from it
def sample_groupref(ref):
    return SUBPATTERNS[ref]


# Map to keep track of subpatterns we see
SUBPATTERNS = {}


# Sample a single node in the regex
def sample_single(node):

    # Unpack node type and data
    t, data = node

    # Use sampler specified by node type on data
    return SAMPLE_TABLE[t](data)


# Generates one sample from the (roughly) uniform distribution on the set of strings matching
# the regex whose parse tree is given as argument
def sample(parsed):
    return ''.join(map(sample_single, parsed))

SAMPLE_TABLE = {s: eval("sample_%s" % s) for s in perg.SAMPLERS}
