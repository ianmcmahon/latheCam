from functools import partial
from itertools import imap
import itertools
from types import MethodType

from modal import Modal
from register import Register

__author__ = 'imcmahon'

class Sub (object):
    """Container object to maintain state of a subroutine number"""
    def __init__(self, sub_number, post):
        self.sub_number = sub_number
        self.post = post


def endwhile(self):
    self.post.w("O%s endwhile" % (self.sub_number,))

def enddowhile(self):
    self.post.w("O%s while %s" % (self.sub_number, self.clause))

duckpunch = lambda obj, name, func: setattr(obj, name, MethodType(func, obj))


class Post (Modal, Register):
    def __init__(self):
        super(Post, self).__init__()
        self.blocks = []
        self.w = self.blocks.append

        self.feedRate = 0

        self.sub_iter = itertools.count(100) # subs start at 100 by convention and will increment by 1


    def __iter__ (self):
        return iter(self.blocks)

    def native(self, block):
        self.w(block)

    def feed(self, f):
        self.w("F%s" % (f, ))

    def _move(self, code, **axes):
        self.w("%s %s" % (code, ' '.join(imap(''.join, imap(partial(imap, str), axes.iteritems())))))

    def rapidTo(self, **axes):
        self._move("G0", **axes)

    def slope(self, **axes):
        self._move("G1", **axes)

    def open_sub(self):
        return Sub(self.sub_iter.next(), self)

    def owhile(self, w_clause):
        sub = self.open_sub()
        self.w("O%s while %s" % (sub.sub_number, w_clause))
        duckpunch(sub, 'close', endwhile)
        return sub

    def odowhile(self, w_clause):
        sub = self.open_sub()
        self.w("O%s do" % (sub.sub_number,))
        sub.clause = w_clause
        duckpunch(sub, 'close', enddowhile)
        return sub


