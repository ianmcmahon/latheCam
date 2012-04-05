from draw import *

__author__ = 'imcmahon'

class Move(object):
    def __init__(self, type, **kwargs):
        self.type = type
        self.coords = kwargs

    def __repr__(self):
        return "move"

    def color(self):
        if self.type == 0:
            return "red"
        if self.type in (1, 2,3):
            return "black"

    def shape(self):
        if self.type in (0,1):
            return "line"
        if self.type in (2,3):
            return "arc"

    def start_end(self, start):
        if start is None:
            start = self.coords
        end = dict(start, **self.coords)
        list = []
        list.append(start['Z'])
        list.append(start['X'])
        list.append(end['Z'])
        list.append(end['X'])
        return tuple(list)


moves = []

moves.append(Move(0, X=1, Z=2))
moves.append(Move(1, X=.5, Z=1.5))
moves.append(Move(1, Z=0.5))

draw.draw_moves(moves)

