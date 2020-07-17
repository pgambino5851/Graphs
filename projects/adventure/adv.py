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
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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
traversal_path = ['n', 'n']
# graph = Graph()
# q = Queue()
# q.enqueue([player.current_room])

# exits = player.current_room.get_exits()
# visited = {}
# # print(f"Current exits: {exits}")
# while q.size() > 0:
#     current_path = q.dequeue()
#     player.current_room = current_path[-1]
#     if player.current_room not in visited:
#        visited[player.current_room] = current_path 

#        exits = player.current_room.get_exits()
#        for exit in exits:
#            traversal_path.append(exit)

#            q.enqueue(player.current_room.get_room_in_direction(exit))

# while len(exits) > 0:
#     path = exits.pop(0)
#     print(f"Current path: {path}")




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
