import os

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')

with open(PUZZLE_INPUT, 'r') as f:
    puzzle_input = f.read().splitlines() 


def solution_one():
    bin_length = len(puzzle_input[0])
    hash_map = {i: 0 for i in range(bin_length)}
    # If the value of hash_map[i] is greater than len(puzzle_input)/2 then there are more 1s
    for binary_num in puzzle_input:
        for i in range(bin_length):
            hash_map[i] += int(binary_num[i])
    gamma = 0
    epsilon = 0
    for i in range(len(hash_map)):
        digit = 0 if hash_map[bin_length - 1 - i] < len(puzzle_input)/2 else 1
        gamma += digit * (2**i)
        epsilon += abs(digit - 1) * (2**i)
    return gamma * epsilon


def get_most_common_bit(input_nums, index):
    total = 0
    for binary_num in input_nums:
        total += int(binary_num[index])
    return '0' if total < len(input_nums)/2 else '1'

def get_rating(input_nums, oxygen):
    bin_length = len(input_nums[0])
    i = 0
    while len(input_nums) > 1 and i < bin_length:
        target_bit = get_most_common_bit(input_nums, i)
        if not oxygen:
            target_bit = '0' if target_bit == '1' else '1'
        j = 0
        while j < len(input_nums):
            if input_nums[j][i] == target_bit:
                j += 1
            else:
                del input_nums[j]
        i += 1
    return int(input_nums[0], 2)

def solution_two():
    return get_rating(puzzle_input.copy(), oxygen=True) * get_rating(puzzle_input.copy(), oxygen=False)