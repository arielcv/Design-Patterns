from enum import Enum

class MapSite():
    def Enter(self):
        raise NotImplementedError("Abstract Base Class method")

class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3


class Room(MapSite):
    def __init__(self, roomNo):
        self._sides = [MapSite] * 4
        self._roomNumber = int(roomNo)

    def getSide(self,direction):
        return self._sides[direction]

    def setSide(self,direction,mapSite):
        self._sides[direction] = mapSite

    def Enter(self):
        print(f'You have entered in the room number {str(self._roomNumber)}')

class Wall(MapSite):
    def Enter(self):
        print("You just ran into a wall...")

class Door(MapSite):
    def __init__(self, room1 = None, room2 = None):
        self.room1 = room1
        self.room2 = room2
        self._isOpen = False

    def otherSideFrom(self, Room: Room):
        print(f'This door is a side of Room {Room._roomNumber}')
        if Room._roomNumber == 1:
            otherRoom = self.room2
        else:
            otherRoom = self.room1
        return otherRoom

    def Enter(self):

        if self._isOpen:
            print("You have passed through this door")
        else:
            print("This door needs to be opened before you can pass through it")

class Maze():
    def __init__(self):
        self._rooms = {}

    def addRoom(self,room):
        self._rooms[room._roomNumber] = room

    def roomNo(self, roomNumber):
        return self._rooms[roomNumber]

class MazeGame():
    def createMaze(self):
        aMaze = Maze()
        r1 = Room(1)
        r2 = Room(2)
        theDoor = Door(r1,r2)

        aMaze.addRoom(r1)
        aMaze.addRoom(r2)

        r1.setSide(Direction.North.value, Wall())
        r1.setSide(Direction.East.value, theDoor)
        r1.setSide(Direction.South.value, Wall())
        r1.setSide(Direction.West.value, Wall())

        r2.setSide(Direction.North.value, Wall())
        r2.setSide(Direction.East.value, Wall())
        r2.setSide(Direction.South.value, Wall())
        r2.setSide(Direction.West.value, theDoor)

        return aMaze