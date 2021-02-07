from Maze import MazeGame, Direction, Door, MazeFactory, EnchantedMazeFactory

if __name__ == '__main__':

    def find_maze_rooms(maze_obj):

        maze_rooms = []

        for room_number in range(5):
            try:
                room = maze_obj.roomNo(room_number)
                print(f'Maze has room number {room._roomNumber}',)
                print('Entering in the room')
                room.Enter()

                maze_rooms.append(room)

                for i in range(4):
                    side = room.getSide(i)
                    # print(f' Room: {0} Direction: {1} Type: {2}',room_number,Direction[i],isinstance(side))
                    print(f"Trying to enter to {Direction(i).name}")
                    side.Enter()

                    if isinstance(side, Door):
                        door = side

                        if not door._isOpen:
                            print("Opening the door")
                            door._isOpen = True
                            door.Enter()

                        otherRoom = door.otherSideFrom(room)
                        print(f"The other side of the room is Room {otherRoom._roomNumber}")


            except KeyError:
                print(f"The room {room_number} doesn't exists ")

        len_rooms = len(maze_rooms)
        print(f"There are {0} rooms",len_rooms)

    print('\n')
    print('*' * 21)
    print('*** The Maze Game ***')
    print('*' * 21)
    print('\n')

    factory = MazeFactory
    print(MazeFactory)

    mazeObj = MazeGame().createMaze(factory)
    find_maze_rooms(mazeObj)

    print('\n')
    print('*' * 21)
    print('*** The Maze Game ***')
    print('*' * 21)
    print('\n')

    factory = EnchantedMazeFactory
    print(MazeFactory)

    mazeObj = MazeGame().createMaze(factory)
    find_maze_rooms(mazeObj)