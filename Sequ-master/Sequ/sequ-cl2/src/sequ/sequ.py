#!/usr/bin/python
#Copyright © 2013 James Beedy
class Sequ(object):

    def __init__(self, minimum, maximum, incrementer=None):

        self.minimum = minimum
        self.maximum = maximum
        if not incrementer:
            incrementer = 1
        self.incrementer = incrementer


    def sequ_ret(self):
        return range(int(float(self.minimum)), int(float(self.maximum)) + 1, int(float(self.incrementer)))