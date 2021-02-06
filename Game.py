from Maze import MazeGame, Direction

if __name__ == '__main__':
    print('*'*21)
    print('*** The Maze Game ***')
    print('*' * 21)

    maze_obj = MazeGame().createMaze()
    maze_rooms = []

    for room_number in range(5):
        try:
            room = maze_obj.roomNo(room_number)
            print(f'Maze has room number {0}',room._roomNumber)
            print('Entering in the room')
            room.Enter()

            maze_rooms.append(room)

            for i in range(4):
                side = room.getSide(i)
                print(f' Room: {0} Direction: {1} Type: {2}',room_number,Direction[i],isinstance(side))
                print(f"Trying to enter to {0}",Direction[i])
                side.Enter()

                if 'Door' in side.__class__:
                    door = side

        except KeyError:
            print(f"The room {0} doesn't exists ",room_number)

        len_rooms = len(maze_rooms)
        print(f"There are {0} rooms",len_rooms)
