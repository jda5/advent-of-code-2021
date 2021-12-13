import os

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')


with open(PUZZLE_INPUT, 'r') as f:
    puzzle_input = f.read().splitlines()
    i = puzzle_input.index('')
    coordinates, instructions = puzzle_input[:i], puzzle_input[i+1:]
    coordinates = [(int(x[0]), int(x[1])) for x in map(lambda x: x.split(','), coordinates)]


def get_fold_line(instruction):
    axis, value = instruction.split('=')
    return axis[-1], int(value)

def fold_paper(coordinates, axis, value):
    new_coordinates = set()
    for x, y in coordinates:
        if axis == 'x':
            if x > value:
                new_coordinates.add((2*value - x, y))
            else:
                new_coordinates.add((x, y))
        else:
            if y > value:
                new_coordinates.add((x, 2*value - y))
            else:
                new_coordinates.add((x, y))
    return new_coordinates

def view_paper(coordinates):
    max_row = max(coordinates, key=lambda x: x[0])[0]
    max_col = max(coordinates, key=lambda x: x[1])[1]
    paper = [[' ' for _ in range(max_row + 1)] for _ in range(max_col + 1)]
    for row, col in coordinates:
        paper[col][row] = '#'
    for row in paper:
        print(''.join(row))

def solution_one():
    axis, value = get_fold_line(instructions[0])
    return len(fold_paper(coordinates, axis, value))
    
def solution_two(coordinates):
    for instruction in instructions:
        axis, value = get_fold_line(instruction)
        coordinates = fold_paper(coordinates, axis, value)
    view_paper(coordinates)
