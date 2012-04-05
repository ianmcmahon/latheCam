from Tkinter import *

__author__ = 'imcmahon'


def scale(translate=0, scale=1):
    def dec(f):
        def ex(*args, **kwargs):
            print args
            args2 = map(lambda x: x*scale, args)
            print args2
            #            print kwargs
            return f(args2, kwargs)
        return ex
    return dec


def draw_moves(moves):
    cur_loc = None
    for move in moves:
        color = move.color()
        func = getattr(w, "scale_%s" % (move.shape(),))
        start_end = move.start_end(cur_loc)
        func(*start_end, fill=color)
        if cur_loc is None:
            cur_loc = dict()
        cur_loc["Z"] = start_end[2]
        cur_loc["X"] = start_end[3]

master = Tk()

canvas_attributes = {"width":1000, "height":500}
w = Canvas(master, canvas_attributes)
w.pack()

w.scale_line = scale(translate=3, scale=100)(w.create_line)
w.scale_rect = scale(translate=3, scale=100)(w.create_rectangle)

mainloop()

