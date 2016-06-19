# coding: utf-8

"""
Mission simulation.
"""

from rover import Plateau, Rover, Heading, Command


if __name__ == '__main__':
    instructions = open('instructions.txt', 'r')

    # Prepare the plateau to landings.
    data = instructions.readline().split()
    x, y = map(int, data)
    plateau = Plateau(x, y)

    # Deploy Rovers on the plateau.
    for data in instructions:
        x, y, heading = data.split()
        rover = Rover(int(x), int(y), getattr(Heading, heading), plateau)

        # Parse and run instructions.
        commands = instructions.readline().strip()
        for cmd in commands:
            command = getattr(Command, cmd)
            rover.execute(command)

        print(rover)

    instructions.close()
