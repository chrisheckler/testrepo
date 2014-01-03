#!/usr/bin/python
#Copyright © 2013 James Beedy

"""
.. module:: sequ
   :platform: Unix
   :synopsis: Sequ-cl0.

.. moduleauthor:: James Beedy 


"""

class Sequ(object):
    """Sequ class.

    `This is the base class of Sequ, from which the following CLs will derive`.

    .. note::

       This is Sequ-cl0.

    """
    def __init__(self, minimum, maximum):
        """Sequ initializer.

        Args:
           minimum (Int): Minimum value of range.
           
           maximum (Int): Maximum value of range.

        """
        self.minimum = int(minimum)
        self.maximum = int(maximum)

    def sequ_ret(self):
        """This function does returns a list of integers seperated by the newline char.
        :param name: self.
        :type name: list.
        :param state: Current state to be in.
        :type state: bool.
        :returns:  list -- the return code.
        :raises: AttributeError, InputError, MaxOrMinError. 
        """
        return range(self.minimum, self.maximum + 1)
