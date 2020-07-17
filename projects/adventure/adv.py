from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Queue
from graph import Graph
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
print(f"Room graph: {room_graph}")

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print(f"Player current room: {player.current_room}")
print(f"Player current room: {player.current_room}")

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

reverseDir = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# Keep track of path segments for traveling back
reversePath = [None]

#Room graph I am building
rooms = {}

#Dictionary to iterate through exits
roomsdict = {}

# visited = [False] * (len(roomGraph)+1)

#Add room zero to graph & dictionary
rooms[0] = player.current_room.get_exits()
roomsdict[0] = player.current_room.get_exits()

#get graph to same length as roomGraph - to ensure all rooms visited
while len(rooms) < len(room_graph)-1:
    if player.current_room.id not in rooms:
        #Add room to graph
        rooms[player.current_room.id] = player.current_room.get_exits()
        print(f"Rooms: {rooms[player.current_room.id]}")
        roomsdict[player.current_room.id] = player.current_room.get_exits()
        print(f"RoomsDict: {roomsdict[player.current_room.id]}")
        #Get last direction traveled
        lastDirection = reversePath[-1]
        print(f"Last Direction: {lastDirection}")
        #Remove last exit from exits to explore - make dead ends
        roomsdict[player.current_room.id].remove(lastDirection)

    # Hit dead end room, turn around
    while len(roomsdict[player.current_room.id]) < 1: 
        reverse = reversePath.pop()
        traversal_path.append(reverse)
        player.travel(reverse)

    #First available exit in room
    exit_dir = roomsdict[player.current_room.id].pop(0)
    #Add to traversal list
    traversal_path.append(exit_dir)
    # Add reverse direction to reverse path
    reversePath.append(reverseDir[exit_dir])
    # travel
    player.travel(exit_dir)

    #To get last room
    if len(room_graph) - len(rooms) ==1:
        rooms[player.current_room.id] = player.current_room.get_exits()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
