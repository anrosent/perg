#!/usr/bin/env python3
#
# RESAMPLE.py: Generates a stream of strings (roughly) uniformly sampled
# from the set of strings matching a given regex
#
# anrosent (anson.rosenthal@gmail.com)

import sys, string
from random import randint, choice
from re import sre_parse

# Parse the regex so we can traverse the tree
def parse(s):
    return sre_parse.parse(s)

# Predefined character categories
CATEGORIES = { 'category_digit' : string.digits, 'category_word': string.ascii_letters + string.punctuation }

# Sampler function in case we run into an unknown type tag
UNK = lambda x: ''



# Component Sampler functions

# Trival sample from literally matching strings
def sample_literal(x): return chr(x)

# Sample from on of the predefined character categories
def sample_category(c):
    return choice(CATEGORIES[c])

# Sample from a range of ASCII values 
# e.g. a-z, A-Z, 0-9
def sample_range(rg):
    s, e = rg
    return chr(randint(s, e))

# Sample from one of the regexes in the matching set
def sample_branch(bs):
    return sample(choice(bs))

# Sample from the set of matching characters 
def sample_in(opts):
    return sample_single(choice(opts))


# Sample bounded repititions of given regex
#FIXME: geometric dist for big max repeat
def sample_max_repeat(node):

    # Unpack start, end of repitition interval and regex to repeat
    s, e, d = node
    return ''.join(sample(d) for _ in range(randint(s, min(e, 25))))

# NOTE: considered equivalent to sampling from greedy repeat matcher.
# May or may not be completely equivalent
def sample_min_repeat(node):
    return sample_max_repeat(node)

# Match any character
def sample_any(d):
    return choice(string.printable)

# FIXME: subpatterns only used for grouping now - no lookahead or negative matching
def sample_subpattern(p):
    t, d = p
    return sample(d)


# Mapping from regex node type tag to sampler function
SAMPLERS = {                                \
        "literal"    : sample_literal,      \
        "branch"     : sample_branch,       \
        "in"         : sample_in,           \
        "range"      : sample_range,        \
        "category"   : sample_category,     \
        "max_repeat" : sample_max_repeat ,      \
        "any"        : sample_any,          \
        "subpattern" : sample_subpattern,   \
        "min_repeat" : sample_min_repeat
}

# Recursive Sampling functions 

# Sample a single node in the regex
def sample_single(node):

    # Unpack node type and data
    t, data = node

    # Use sampler specified by node type on data
    return SAMPLERS.get(t, UNK)(data)

# Generates one sample from the uniform distribution on the set of strings matching
# the regex whose parse tree is given as argument
def sample(parsed):
    return ''.join(map(sample_single, parsed))



# A generator of roughly uniform samples from the set of strings matching the regex
# NOTE: haven't proven to myself that output is actually uniform in all cases, 
# i.e. whether the entire set is actually generable, so I'll say roughly for now.
def sampler(s):
    tree = parse(s)
    while True:
        yield sample(tree)
    
# TODO: better CLI
if __name__ == '__main__':  
    # Get regex to sample from as 1st arg
    regex = sys.argv[1].replace('\\\\', '\\') 

    # Make sample generator and sample forever
    my_sampler = sampler(regex)

    # TODO: add -n flag
    for _ in range(10):
        print(next(my_sampler))
