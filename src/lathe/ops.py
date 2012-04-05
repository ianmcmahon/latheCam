from post import HNC

__author__ = 'imcmahon'

class Ops (object):
    def __init__(self, post):
        self.post = post
        self.clearance = 0.025

    def rapid(self, kw):
        return self.post.rapidTo(**kw)

    def slope(self, kw):
        return self.post.slope(**kw)

    def od_rough(self, tool, stock_dia, finish_dia, z_start, z_end):
        c = self.clearance
        p = self.post

        move = dict

        #cur_dia = stock_dia

        moves = [move(X=stock_dia+c), move(Z=z_start+c)]
        map(self.rapid, moves)

        p.push_modal_feed_ipr()
        p.push_modal_css(100, 2500)

        iter = p.borrow_register(assign="1")

        sub = p.owhile("foo")


        sub.close()

        p.return_register(iter)

        p.pop_modal_feed()
        p.pop_modal_speed()


h = HNC()

o = Ops(h)

h.push_modal_feed_ipm()
h.push_modal_rpm()
o.od_rough(None, 1.0, .750, 0, -3)

for line in h:
    print line

