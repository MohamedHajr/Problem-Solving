# Globals for the bearings
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def advance(self):
        x, y = self.coordinates
        self.coordinates = {
            EAST: (x + 1, y),
            NORTH: (x, y + 1),
            WEST: (x - 1, y),
            SOUTH: (x, y - 1)
        }[self.bearing]

    def simulate(self, simulation_string):
        for instruction in simulation_string:
            {'L': self.turn_left,
             'R': self.turn_right,
             'A': self.advance
             }[instruction]()
