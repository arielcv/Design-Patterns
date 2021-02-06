from enum import Enum

class MapSite():
    def Enter(self):
        raise NotImplementedError("Abstract Base Class method")

class Directions(Enum):
    North = 0
    East = 1
    South = 2
    West = 3

