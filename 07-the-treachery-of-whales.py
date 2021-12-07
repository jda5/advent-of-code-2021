import os
import statistics

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')

with open(PUZZLE_INPUT, 'r') as f:
    puzzle_input = f.read().split(',')

crabs = list(map(int, puzzle_input))


def solution_one():
    median = statistics.median(crabs)
    distance = 0
    for crab in crabs:
        distance += abs(crab - median)
    return distance

def sum_distance(items, center):
    distance = 0
    for item in items:
        for step in range(1, abs(item - center) + 1):
            distance += step
    return distance

def solution_two():
    lowest = float('inf')
    for center in range(max(crabs)):
        distance = sum_distance(crabs, center)
        if distance <= lowest:
            lowest = distance
        else:
            return lowest