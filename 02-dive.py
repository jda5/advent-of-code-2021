import os
import re

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')

with open(PUZZLE_INPUT, 'r') as f:
    puzzle_input = f.read().splitlines() 


def solution_one():
    horizontal = 0
    depth = 0
    number = re.compile(r"\d+")
    for direction in puzzle_input:
        amount = int(number.search(direction).group())
        if direction[0] == "f":
            horizontal += amount
        elif direction[0] == "d":
            depth += amount
        else:
            depth -= amount
    return horizontal * depth


def solution_two():
    horizontal = 0
    aim = 0
    depth = 0
    number = re.compile(r"\d+")
    for direction in puzzle_input:
        amount = int(number.search(direction).group())
        if direction[0] == "f":
            horizontal += amount
            depth += aim * amount
        elif direction[0] == "d":
            aim += amount
        else:
            aim -= amount
    return horizontal * depth
