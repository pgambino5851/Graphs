
# Plan
## Translate the problem
# Nodes: People
## Edges: When a child has a parent
### Build our graph, or just define get_neighbors

## Choose algorithm
#### Either BFS or DFS
#### DFS
#### How would we know if DFS happened to be faster?

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph: 
    def __init__(self):
        self.vertices = {}

        def add_vertex(self, vertex):
            if vertex not in self.vertices:
                self.vertices[vertex] = set()

        def add_edge(self, v1, v2):
            self.vertices[v1].add(v2)
        
        def get_neighbors(self, vertex):
            return self.vertices[vertex]

graph = Graph()
def build_graph(ancestors):
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]

        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    return graph

def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)
    
    s = Stack()

    visited = set()

    s.push([starting_node])

    longest_path = {}
    aged_one = -1

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]

        if len(path) > len(longest_path) or (len(path) == len(longest_path) and current_node < aged_one ):
            longest_path = path

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)
    