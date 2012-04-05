from itertools import ifilter

__author__ = 'imcmahon'

class Register (object):
    def __init__(self):
        print "register init"
        self.register_range = range(31,5000)
        self.borrowed_registers = []
        self.w = None

    def borrow_register(self, assign=None):
        reg = ifilter(lambda v: v not in self.borrowed_registers, self.register_range).next()
        self.borrowed_registers.append(reg)
        if assign is not None:
            self.assign_register(reg, assign)
        return reg

    def return_register(self, reg):
        self.borrowed_registers.remove(reg)

    def assign_register(self, reg, value):
        self.w("#%s %s" % (reg,value))