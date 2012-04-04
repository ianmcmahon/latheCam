from itertools import ifilter

__author__ = 'imcmahon'

class Register (object):
    def __init__(self):
        self.register_range = range(1,100)
        self.borrowed_registers = []

    def borrow_register(self):
        reg = ifilter(lambda v: v not in self.borrowed_registers, self.register_range).next()
        self.borrowed_registers.append(reg)
        return reg

    def return_register(self, reg):
        self.borrowed_registers.remove(reg)
