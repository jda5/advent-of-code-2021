import os
from math import prod

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')


with open(PUZZLE_INPUT, 'r') as f:
    height_map = []
    for row in f.read().splitlines():
        r = []
        for elem in row:
            r.append(int(elem))
        height_map.append(r)


# x is col index
# y is row index

class HeightMap:

    def __init__(self, _map):
        self._map = _map

    def on_map(self, x, y):
        return 0 <= x < len(self._map[0]) and 0 <= y < len(self._map)

    def get_points(self):
        for y in range(len(self._map)):
            for x in range(len(self._map[0])):
                yield y, x

    def is_low_point(self, x, y):
        point = self._map[y][x]
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if self.on_map(x + dx, y + dy):
                if self._map[y + dy][x + dx] <= point:
                    return False
        return True

    def solution_one(self):
        risk_level = 0
        for y, x in self.get_points():
            if self.is_low_point(x, y):
                risk_level += 1 + self._map[y][x]
        return risk_level

    def traverse_basin(self, low_x, low_y):
        points = [(low_y, low_x)]
        visited = set()
        while len(points) > 0:
            y, x = points.pop()
            visited.add((y, x))
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if self.on_map(x + dx, y + dy):
                    if self._map[y + dy][x + dx] < 9:
                        if ((y + dy), (x + dx)) not in visited:
                            points.append((y + dy, x + dx))
        return len(visited)

    def solution_two(self):
        low_points = []
        for y, x in self.get_points():
            if self.is_low_point(x, y):
                low_points.append((y, x))

        sizes = []
        for y, x in low_points:
            sizes.append(self.traverse_basin(x, y))

        top_three = []
        for i in range(0, 3): 
            curr = 0
            for j in range(len(sizes)):     
                if sizes[j] > curr:
                    curr = sizes[j];
            sizes.remove(curr);
            top_three.append(curr)
        return prod(top_three)