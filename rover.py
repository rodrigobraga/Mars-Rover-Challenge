# coding: utf-8

"""
Mars Rover embedded software.
"""

import logging
from enum import Enum


logger = logging.getLogger('MarsRover')


class Heading(Enum):
    N = 1
    E = 2
    S = 3
    W = 4


class Command(Enum):
    L = 1
    R = 2
    M = 3


class Plateau(object):
    """
    Basic representation to help with coordinates validation.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.axis_x_extension = range(self.x + 1)
        self.axis_y_extension = range(self.y + 1)

    def validate(self, x, y):
        """
        Verifies if coordinates are inside the limits.
        """
        return x in self.axis_x_extension and y in self.axis_y_extension


class Rover(object):
    """
    Automated vehicle used to explore the red planet.
    """
    def __init__(self, x, y, heading, plateau):
        self.x = x
        self.y = y
        self.heading = heading
        self.plateau = plateau

    def __str__(self):
        return '{0} {1} {2}'.format(
            self.x, self.y, self.heading.name)

    def _get_coordinates(self):
        return (self.x, self.y,)

    coordinates = property(_get_coordinates, doc="get current coordinates")

    def _turn_left(self):
        heading = self.heading.value - 1

        if heading < Heading.N.value:
            heading = Heading.W.value

        self.heading = Heading(heading)

    def _turn_right(self):
        heading = self.heading.value + 1

        if heading > Heading.W.value:
            heading = Heading.N.value

        self.heading = Heading(heading)

    def _move_forward(self):
        if self.heading is Heading.N:
            self.y += 1

        if self.heading is Heading.E:
            self.x += 1

        if self.heading is Heading.S:
            self.y -= 1

        if self.heading is Heading.W:
            self.x -= 1

        if not self.plateau.validate(self.x, self.y):
            logger.warning(
                'Do you can go beyond the borders? '
                'Maybe you need to talk with mission control.')

    def execute(self, command):
        if not isinstance(command, Command):
            raise ValueError(
                'You need talk martian or the command will be ignored.')

        if command is Command.L:
            self._turn_left()

        if command is Command.R:
            self._turn_right()

        if command is Command.M:
            self._move_forward()
