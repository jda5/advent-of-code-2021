import os
from collections import defaultdict


FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')

pair_map = {}

with open(PUZZLE_INPUT, 'r') as f:
    puzzle_input = f.read().splitlines()
    template = puzzle_input[0]
    for line in puzzle_input[2:]:
        key, value = line.split(" -> ")
        pair_map[key] = (key[0] + value, value + key[1])

def count_characters(template, steps=10):
    pair_count = defaultdict(lambda: 0)
    for i in range(0, len(template) - 1):
        pair_count[template[i:i+2]] += 1
    for _ in range(steps):
        temp = defaultdict(lambda: 0)
        for pair, value in pair_count.items():
            if pair in pair_map:
                a, b = pair_map[pair]
                temp[a] += value
                temp[b] += value
            else:
                temp[pair] += value
        pair_count = temp
    char_count = defaultdict(lambda: 0)
    for pair, value in pair_count.items():
        for char in pair:
            char_count[char] += value
    max_letter = max(char_count, key=char_count.get)
    min_letter = min(char_count, key=char_count.get)
    return (char_count[max_letter] - char_count[min_letter]) // 2