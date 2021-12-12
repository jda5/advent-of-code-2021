import os

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')


class Caves:

    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.load_caves()
        self.path_count = 0

    def add_node(self, node):
        if node in self.nodes:
            return
        self.nodes.append(node)
        self.edges[node] = []

    def add_edge(self, source, destination):
        if source not in self.nodes:
            self.add_node(source)
        if destination not in self.nodes:
            self.add_node(destination)
        adjacent_nodes = self.edges[source]      # create a reference for the nodes adjacent to the source node
        if destination in adjacent_nodes:        # no need to do anything if the destination is already adjacent to the source node
            return
        adjacent_nodes.append(destination)

    def adjacent_nodes(self, node):
        return self.edges.get(node, [])

    def load_caves(self):
        with open(PUZZLE_INPUT, 'r') as f:
            for line in f.read().splitlines():
                source, destination = line.split('-')
                self.add_edge(source, destination)
                self.add_edge(destination, source)

    def find_paths(self, curr, path, small_visit):  # SOLUTION 2 --> For SOLUTION 1 remove all references to small_visit
        path = path + [curr]                        # Add current node to the path
        if curr == 'end':                           # This is our base case that will be reached eventually in the recursive calls if the path exists
            self.path_count += 1
            return
        for node in self.adjacent_nodes(curr):
            if node == 'start':
                continue
            if node.islower():
                if node in path:
                    if small_visit:
                        continue                    # Do not visit small caves twice
                    self.find_paths(node, path, True)
                    continue
            self.find_paths(node, path, small_visit)