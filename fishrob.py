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
        for part in self._parts:
            print(part, end='')

    def pl(self):
        for part in self._parts:
            print(part)

    def x(self, pattern, flags=0):
        pat = re.compile(pattern, flags)

        def gen():
            for part in self._parts:
                for match in pat.finditer(part):
                    yield match.group(0)

        return _Fishrob(gen())

    def g(self, pattern, flags=0):
        pat = re.compile(pattern, flags)

        def gen():
            for part in self._parts:
                if pat.search(part):
                    yield part

        return _Fishrob(gen())


# TODO:
# Operators from the paper: y, v, c
#
# .map() - remain lazy
# .each() - iterate, with side effects
#
# Would it work??: .balanced(start, end) - match balanced parens or brackets
# (at the current level, skipping nested ones?).
#
# Would be nice to make a more obvious distinction between methods that remain
# lazy vs. those that activate the iteration.  Capitalization?  In some other
# language, the ones with side-effects could have exclamation points or
# something.
