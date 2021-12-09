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


class HeightMap:

    def __init__(self, _map):
        self._map = _map

    def on_map(self, x, y):
        return 0 <= x < len(self._map[0]) and 0 <= y < len(self._map)

    def get_points(self):
        for y in range(len(self._map)):
            for x in range(len(self._map[0])):
                yield y, x

    def get_adjacent(self, x, y):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if self.on_map(x + dx, y + dy):
                yield y + dy, x + dx

    def is_low_point(self, x, y):
        point = self._map[y][x]
        for dy, dx in self.get_adjacent(x, y):
            if self._map[dy][dx] <= point:
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
            for dy, dx in self.get_adjacent(x, y):
                if self._map[dy][dx] < 9:
                    if ((dy), (dx)) not in visited:
                        points.append((dy, dx))
        return len(visited)

    def solution_two(self):
        top_three = [0, 0, 0]
        for y, x in self.get_points():
            if self.is_low_point(x, y):
                basin_size = self.traverse_basin(x, y)
                index_min = min(range(len(top_three)), key=top_three.__getitem__)
                if basin_size > top_three[index_min]:
                    top_three[index_min] = basin_size
        return prod(top_three)
