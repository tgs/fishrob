"""
Fishrob - a partial implementation of Rob Pike's Structural Regexps.

http://doc.cat-v.org/bell_labs/structural_regexps/se.pdf

by Thomas Grenfell Smith
"""
from __future__ import print_function
import re

#
# Fishrob : A pike is a fish, and... yeah.
#

def fishrob(string):
    return _Fishrob([string])


class _Fishrob(object):
    def __init__(self, iterable):
        self._parts = iterable

    def p(self):
        "Iterate and print each chunk, not adding a new line"
        for part in self._parts:
            print(part, end='')

    def pl(self):
        "Iterate and print each chunk, adding a newline between each"
        for part in self._parts:
            print(part)

    def x(self, pattern, flags=0):
        "Break each chunk into bits: the substrings that match the pattern"
        pat = re.compile(pattern, flags)

        def extract(text):
            for match in pat.finditer(text):
                yield match.group(0)

        return self.mapiter(extract)

    def g(self, pattern, flags=0):
        "Filter chunks, keeping only those that match the pattern"
        pat = re.compile(pattern, flags)

        return self.filter(pat.search)

    def filter(self, pred):
        "Keep only some chunks"
        return _Fishrob(part for part in self._parts if pred(part))

    def map(self, func):
        "Transform the current text using a function"
        return _Fishrob(func(part) for part in self._parts)

    def mapiter(self, func):
        "Break the current text into parts using a function"
        def gen():
            for part in self._parts:
                for chunk in func(part):
                    yield chunk

        return _Fishrob(gen())

    def __iter__(self):
        return iter(self._parts)

    def each(self, routine):
        "Iterate and apply routine to each chunk"
        for part in self._parts:
            routine(part)


# TODO:
# Operators from the paper: y, v, c
#
# Would it work??: .balanced(start, end) - match balanced parens or brackets
# (at the current level, skipping nested ones?).
#
# Would be nice to make a more obvious distinction between methods that remain
# lazy vs. those that activate the iteration.  Capitalization?  In some other
# language, the ones with side-effects could have exclamation points or
# something.
