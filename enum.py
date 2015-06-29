import sys
import pdb

from itertools import product, chain
import perg



# Map to keep track of subpatterns we see
SUBPATTERNS = {}

# Map to keep track of where we are in enumerating the matches to the subpattern
# so we get correct backreferences
ENUM_SUBPATTERN_IX = {}

class EnumSubpatternIterator(object):

    def __init__(self, subpattern_id, items):
        self.subpattern_id = subpattern_id
        self.items = items
        self.ix = 0
        ENUM_SUBPATTERN_IX[self.subpattern_id] = 0

    def __next__(self):
        if self.ix == len(self.items):
            raise StopIteration

        res = self.items[self.ix]
        self.ix += 1
        ENUM_SUBPATTERN_IX[self.subpattern_id] = self.ix
        return res
        
    def __iter__(self):
        return self
    
    def __getitem__(self, ix):
        return self.items[ix]

class EnumBackreferenceIterator(object):

    def __init__(self, subpattern_id, items):
        self.subpattern_id = subpattern_id

    def __iter__(self):
        return iter([SUBPATTERNS[self.subpattern_id][ENUM_SUBPATTERN_IX[self.subpattern_id]]])



# Prompt so you don't crash your computer doing huge repeat pattern enumeration
def checkContinue(msg):
    res = ""
    while res.lower() not in ['y', 'n']:
        res = input(msg)
    if res.lower() == 'n':
        sys.exit(1)


def enum_literal(x): return chr(x)

def enum_category(c):
    return perg.CATEGORIES[c]

def enum_range(rg):
    s,e = rg
    return map(chr, range(s,e+1))

def enum_branch(bs):
    _, d = bs
    return chain(*map(enum_gen, d))

def enum_in(opts):
    return chain(*map(enum_single, opts))

def enum_max_repeat(node):
    s, e, d = node

    # Check yourself before you wreck yourself
    checkContinue("You asked for matches of up to %s repeats... Are you sure you want this? [y/n] " % e)
    matches = list(enum_gen(d))
    return chain(*(map(joiner, product(matches, repeat=repititions)) for repititions in range(s, e+1)))

def enum_min_repeat(node):
    return enum_max_repeat(node)

def enum_any(d):
    return string.printable
    
def enum_subpattern(p):
    subpattern_id, d = p
    patterns = list(enum_gen(d))

    '''
    if subpattern_id:
        subpat_iter = EnumSubpatternIterator(subpattern_id, patterns)
        SUBPATTERNS[subpattern_id] = subpat_iter
        return subpat_iter
    else:
        return patterns
        '''
    return patterns

def enum_groupref(ref):
    raise NotImplementedError
    #return SUBPATTERNS[ref][ENUM_SUBPATTERN_IX[ref]]

def joiner(t):
    #pdb.set_trace()
    return ''.join(t)

def enum_single(node):
    #pdb.set_trace()
    t, data = node
    return ENUM_TABLE[t](data)

def enum_gen(parsed):
    return map(joiner, product(*list(map(enum_single, parsed))))

ENUM_TABLE = {s: eval("enum_%s" % s) for s in perg.SAMPLERS}
