#!/usr/bin/env python3
#
# perg.py: Generates a stream of strings (roughly) uniformly sampled
# from the set of strings matching a given regex
#
# anrosent (anson.rosenthal@gmail.com)
import string
from re import sre_parse

# Parse the regex so we can traverse the tree
def parse(s):
    return sre_parse.parse(s)

# Regex parse node names that we can sample
SAMPLERS = {"literal", "branch", "in", "range", "category", "max_repeat", 
            "any", "subpattern", "min_repeat", 'groupref'}

# Predefined character categories
# TODO: add 'category_not_XXX' support
# TODO: add whitespace support
CATEGORIES = { 'category_digit' : string.digits, 'category_word': string.ascii_letters }
