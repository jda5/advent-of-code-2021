import os

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')


class Octopus:

    def __init__(self, parent, energy, coordinates):
        self.parent = parent
        self.energy = energy
        self.coordinates = coordinates

    def increase_energy(self):
        self.energy += 1
        if self.energy == 10:
            self.parent.flash(self)
            

class Grid:

    def __init__(self):
        self.grid = self.load_grid()
        self.flashed = []

    def load_grid(self):
        grid = []
        with open(PUZZLE_INPUT, 'r') as f:
            for i, line in enumerate(f.read().splitlines()):
                row = []
                for j, char in enumerate(line):
                    row.append(Octopus(self, int(char), (i, j)))
                grid.append(row)
        return grid

    def on_grid(self, row, col):
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])

    def get_adjacent(self, row, col):
        for i, j in ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)):
            if self.on_grid(row + i, col + j):
                yield row + i, col + j

    def get_coordinates(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                yield row, col

    def flash(self, octopus):
        self.flashed.append(octopus)
        for row, col in self.get_adjacent(*octopus.coordinates):
            self.grid[row][col].increase_energy()

    def solution_one(self, steps=100):
        count_flashed = 0
        for _ in range(steps):
            for row, col in self.get_coordinates():
                self.grid[row][col].increase_energy()
            for octopus in self.flashed:
                octopus.energy = 0
            count_flashed += len(self.flashed)
            self.flashed = []
        return count_flashed

    def solution_two(self):
        step = 1
        while True:
            for row, col in self.get_coordinates():
                self.grid[row][col].increase_energy()
            if len(self.flashed) == 100:
                return step
            for octopus in self.flashed:
                octopus.energy = 0
            self.flashed = []
            step += 1