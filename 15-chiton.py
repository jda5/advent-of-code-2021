import os
from collections import defaultdict


FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')


with open(PUZZLE_INPUT, 'r') as f:
    cave = f.read().splitlines()
    cave = [[int(x) for x in row] for row in cave]

def in_cave(i, j, graph):
    return 0 <= i < len(graph) and 0 <= j < len(graph[0]) 

def get_neighbours(i, j, graph):
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if in_cave(i + dx, j + dy, graph):
            yield i + dx, j + dy

def dijkstra(graph):
    distance = [[float('inf') for _ in range(len(graph[0]))] for _ in range(len(graph))]
    distance[0][0] = 0
    queue = {(i, j) for i in range(len(graph)) for j in range(len(graph[0]))}
    while len(queue) > 0:
        i, j = min(queue, key=lambda x: distance[x[0]][x[1]])
        queue.remove((i, j))
        for dx, dy in get_neighbours(i, j, graph):
            alt = distance[i][j] + graph[dx][dy]
            if alt < distance[dx][dy]:
                distance[dx][dy] = alt
    return distance

def solution_one(graph):
    distances = dijkstra(graph)
    return distances[-1][-1]

def solution_two():
    extended_cave = []
    for i in range(5):
        for row in cave:
            new_row = []
            for elem in row:
                new_elem = i + elem
                if new_elem > 9:
                    new_elem = new_elem % 9
                new_row.append(new_elem)
            extended_cave.append(new_row)
    full_cave = []
    for row in extended_cave:
        new_row = []
        for i in range(5):
            for elem in row:
                new_elem = i + elem
                if new_elem > 9:
                    new_elem = new_elem % 9
                new_row.append(new_elem)
        full_cave.append(new_row)
    return solution_one(full_cave)

print(solution_two())