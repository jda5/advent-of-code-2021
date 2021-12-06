import os

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')

with open(PUZZLE_INPUT, 'r') as f:
    puzzle_input = f.read().split(',')

fishes = list(map(int, puzzle_input))


def count_fish(days):
    counter = [0 for _ in range(9)]
    for fish in fishes:
        counter[fish] += 1
        
    for _ in range(days):
        prev = 0
        for i in range(len(counter) - 1, -1, -1):
            temp = counter[i]
            counter[i] = prev
            prev = temp
        counter[-1] = prev
        counter[6] += prev
    return sum(counter)
