import os
import re

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')


class VentScanner:

    def __init__(self):
        self.vents = dict()

    def get_coordinates(self):
        with open(PUZZLE_INPUT, 'r') as file:
             for row in file:
                re_coordinates = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", row)
                yield tuple(map(int, re_coordinates.groups()))

    def mark_vent(self, x, y):
        if (x, y) not in self.vents:
            self.vents[(x, y)] = 1
        else:
            self.vents[(x, y)] += 1

    def map_vertical(self, x1, y1, x2, y2):
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            self.mark_vent(x1, y)

    def map_horizontal(self, x1, y1, x2, y2):
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            self.mark_vent(x, y1)

    def map_diagonal(self, x1, y1, x2, y2, gradient):
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        for i in range(x2 - x1 + 1):
            self.mark_vent(x1 + i, y1 + (i * gradient))

    def count_overlap(self):
        num_overlap = 0
        for value in self.vents.values():
            if value > 1:
                num_overlap += 1
        return num_overlap

    def solution_one(self):
        for x1, y1, x2, y2 in self.get_coordinates():
            if x1 == x2:
                self.map_vertical(x1, y1, x2, y2)
            if y1 == y2:
                self.map_horizontal(x1, y1, x2, y2)
        return self.count_overlap()

    def solution_two(self):
        for x1, y1, x2, y2 in self.get_coordinates():
            if x1 == x2:
                self.map_vertical(x1, y1, x2, y2)
            if y1 == y2:
                self.map_horizontal(x1, y1, x2, y2)
            try:
                gradient = (y2 - y1) / (x2 - x1)
            except ZeroDivisionError:
                continue
            if abs(gradient) == 1:
                self.map_diagonal(x1, y1, x2, y2, gradient)
        return self.count_overlap()
