# coding: utf-8

"""
Tests to Mars Rover.
"""

import unittest
import mock

from rover import Heading, Command, Plateau, Rover


class TestPlateau(unittest.TestCase):
    """
    Verifies if after landed, the rover can navigate on the plateau.
    """
    def setUp(self):
        self.plateau = Plateau(5, 5)

    def test_validate(self):
        self.assertTrue(self.plateau.validate(2, 2))


class TestRover(unittest.TestCase):
    """
    Verifies if after landed, the rover can navigate on the plateau.
    """
    def setUp(self):
        self.plateau = Plateau(5, 5)
        self.rover = Rover(1, 2, Heading.N, self.plateau)

    def test_get_str_representation(self):
        expected = '1 2 N'
        self.assertEqual(expected, str(self.rover))

    def test_turn_right(self):
        """
        Test a full turn to right when heading to north.
        """
        self.rover.execute(Command.R)
        self.assertEqual(self.rover.heading, Heading.E)

        self.rover.execute(Command.R)
        self.assertEqual(self.rover.heading, Heading.S)

        self.rover.execute(Command.R)
        self.assertEqual(self.rover.heading, Heading.W)

        self.rover.execute(Command.R)
        self.assertEqual(self.rover.heading, Heading.N)

    def test_turn_left(self):
        """
        Test a full turn to left when heading to north.
        """
        self.rover.execute(Command.L)
        self.assertEqual(self.rover.heading, Heading.W)

        self.rover.execute(Command.L)
        self.assertEqual(self.rover.heading, Heading.S)

        self.rover.execute(Command.L)
        self.assertEqual(self.rover.heading, Heading.E)

        self.rover.execute(Command.L)
        self.assertEqual(self.rover.heading, Heading.N)

    def test_move(self):
        """
        Test a move forward in all directions, starting from north.
        """
        self.rover.execute(Command.M)
        self.assertEqual((1, 3), self.rover.coordinates)

        self.rover.execute(Command.R)
        self.rover.execute(Command.M)
        self.assertEqual((2, 3), self.rover.coordinates)

        self.rover.execute(Command.R)
        self.rover.execute(Command.M)
        self.assertEqual((2, 2), self.rover.coordinates)

        self.rover.execute(Command.R)
        self.rover.execute(Command.M)
        self.assertEqual((1, 2), self.rover.coordinates)

    def test_execute_with_unknown_command(self):
        rover = Rover(1, 2, Heading.N, self.plateau)
        self.assertRaises(ValueError, rover.execute, True)

    @mock.patch('rover.logger.warning')
    def test_move_forward_to_beyond_the_borders(self, m_logger):
        """
        If Rover exceed a border, a warning is raised.
        """
        rover = Rover(0, 0, Heading.W, self.plateau)
        rover.execute(Command.M)

        m_logger.assert_called_once_with(
            'Do you can go beyond the borders? '
            'Maybe you need to talk with mission control.')


if __name__ == '__main__':
    unittest.main()
