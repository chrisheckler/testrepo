#!/usr/bin/python
#Copyright © 2013 James Beedy
class Sequ(object):
    def __init__(self, minimum, maximum):
        self.minimum = int(minimum)
        self.maximum = int(maximum)

    def sequ_ret(self):
        return range(self.minimum, self.maximum + 1)

