import os

PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', '01-sonar-sweep.txt')

with open(PUZZLE_INPUT, 'r') as f:
    puzzle_input = f.read().splitlines() 

puzzle_input = list(map(int, puzzle_input))


def solution_one():
    res = 0
    prev_depth = puzzle_input[0]
    for depth in puzzle_input[1:]:
        if depth > prev_depth:
            res += 1
        prev_depth = depth
    return res

def solution_two():
    res = 0
    prev_window = sum(puzzle_input[:3])
    for i in range(2, len(puzzle_input) - 1):
        window = sum([puzzle_input[i-1], puzzle_input[i], puzzle_input[i+1]])
        if window > prev_window:
            res += 1
        prev_window = window
    return res

print(solution_two())