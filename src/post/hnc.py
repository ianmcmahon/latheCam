from functools import partial
from itertools import imap

_author__ = 'imcmahon'


class HNC (object):

    def __init__(self):
        self.blocks = []
        self.w = self.blocks.append

        self.feedRate = 0


    def __iter__ (self):
        return iter(self.blocks)

    def feed(self, f):
        self.w("F%s" % (f, ))

    def _move(self, code, **axes):
        self.w("%s %s" % (code, ' '.join(imap('='.join, imap(partial(imap, str), axes.iteritems())))))

    def rapidTo(self, **axes):
        self._move("G0", **axes)

    def slope(self, **axes):
        self._move("G1", **axes)


