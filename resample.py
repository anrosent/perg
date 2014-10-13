#!/usr/bin/env python3

import sys, fileinput
from string import ascii_letters, digits
from random import randint, choice

#TODO exp distribution on unbounded repitition
#TODO OR
#TODO ANY
#TODO {n}, {n,m} repitition


class Regex_AST(object):
    
    def __init__(self, nodes):
        self.nodes = nodes

    def __str__(self):
        return str(self.nodes)

    def sampler(self):
        while True:
            yield ''.join(node.generate() for node in self.nodes)

class Regex_Node(object):
    
    def __str__(self):
        return "%s,%s:<%s>"%(self.name, self.params, self.body)

    def __repr__(self):
        return self.__str__()

    def generate(self):
        return ''.join(node.generate() for node in self.body)

class Multiple(Regex_Node):
    name = "Multiple"

    def __init__(self, params, node):
        self.params = params
        self.body = node

# TODO: give descriptive pattern name
class Star(Multiple):
    
    def __init__(self, node):
        super(Regex_Node)
        self.params = '*'
        self.body = node

    def generate(self,max_n=10):
        n = randint(0,max_n)
        return ''.join(self.body.generate() for i in range(n))

# TODO: give descriptive pattern name
class Plus(Multiple):
    
    def __init__(self, node):
        super(Regex_Node)
        self.params = '+'
        self.body = node
    
    def generate(self,max_n=10):
        n = randint(1,max_n)
        return ''.join(self.body.generate() for i in range(n))

class Maybe(Multiple):
    
    def __init__(self, node):
        super(Regex_Node)
        self.params = "?"
        self.body = node

    def generate(self):
        if choice([0,1]):
            return self.body.generate()
        else:
            return ''

# TODO: isn't parsed yet
class N_repeat(Multiple):
    
    def __init__(self, n, node):
        super(Regex_Node)
        self.params = '{%s}'%n
        self.body = [node]

# TODO: isn't parsed yet
class Range(Multiple):
    
    def __init__(self, n, m, node):
        super(Regex_Node)
        self.params = '{%s,%m}'%(n,m)
        self.body = [node]

class String(Regex_Node):
    params = ''

    def __init__(self, alphabet):
        super(Regex_Node)
        self.name = "String"
        self.alphabet = alphabet
        self.body = alphabet

    def  __repr__(self):
        return "String:%s"%self.alphabet

    def generate(self):
        return choice(self.alphabet)

class ParseError(Exception):
    
    def __init__(self, c, i):
        super("error at index %s, char %s"%(i,c))

keywords = {
            '*':Star,
            '+':Plus,
            '?':Maybe
           }


# TODO: super jank, do this the right way
def parse_regex(rgx):
    text = ''
    posn = 0
    nodes = []
    stream = enumerate(rgx)
    for i, c in stream:
        if c in keywords:
            if text:
                if len(text) > 2:
                    nodes.append(String(text[:-1]))
                node = String([text[-1]])
                node = keywords[c](node)
                text = ''
                nodes.append(node)
            elif nodes:
                nodes[-1] = keywords[c](nodes[-1])
            else:
                raise ParseError(c, i)
        else:
            if c == '\\':
                if text:
                    nodes.append(String([text]))
                    text = ''
                ix, c2 = stream.__next__()
                if c2 == 'd':
                    nodes.append(String(list(digits)))
                elif c2 == 'w':
                    nodes.append(String(list(ascii_letters)))
                text = ''
            else:
                text += c
    if text:
        nodes.append(String([text]))
    return Regex_AST(nodes)


# TODO: better cmdline usage, with:
#   - # samples parameter
#   - pass in pattern via stdin, file arg, or literal arg

if __name__ == '__main__':  
    line = ''.join(fileinput.input()).strip()
    re_ast = parse_regex(line)
    sampler = re_ast.sampler()
    for i in range(10):
        print(sampler.__next__())
