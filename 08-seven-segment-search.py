import os
import statistics

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')


class SegmentDisplay:

    def __init__(self):
        self.segment_digit = {
            'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4,
            'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9
        }

    def load_display(self):
        with open(PUZZLE_INPUT, 'r') as f:
            for line in f.read().splitlines():
                line = line.split()
                yield line[:10], line[11:] 

    def solution_one(self):
        count = 0
        for signal, output in self.load_display():
            for segment in output:
                if len(segment) in (2, 4, 3, 7):
                    count += 1
        return count

    def get_diff(self, segment_one, segment_two):
        diff = set(segment_one) ^ set(segment_two)
        if len(diff) == 1:
            return list(diff)[0]
        return diff

    def decode(self, signal):
        key = {}
        len_index = {i: [] for i in range(2, 8)}
        for i in range(len(signal)):
            len_index[len(signal[i])].append(i)
        
        key['a'] = self.get_diff(signal[len_index[2][0]], signal[len_index[3][0]])
        # Get difference between 1 (2, 3, 5) --> number of differences between 1 and 3 is 3
        for i in len_index[5]:
            if len(self.get_diff(signal[len_index[2][0]], signal[i])) == 3:
                # len(Difference) between 3 and 9 is 1 (b)
                for j in len_index[6]:
                    diff = self.get_diff(signal[i], signal[j])
                    if len(diff) == 1:
                        key['b'] = diff
                        for l in self.get_diff(signal[i], signal[len_index[4][0]]):
                            if l not in (key['a'], key['b']):
                                key['g'] = l

        for l in self.get_diff(signal[len_index[4][0]], signal[len_index[2][0]]):
            if l != key['b']:
                key['d'] = l

        known_set = set(key.values())
        for i in len_index[5]:
            diff = known_set ^ set(signal[i])
            if len(diff) == 1:
                key['f'] = list(diff)[0]

        key['c'] = self.get_diff(signal[len_index[2][0]], key['f'])
        key['e'] = list(set(signal[len_index[7][0]]) ^ set(key.values()))[0]
        return {y: x for (x, y) in key.items()}

    def solution_two(self):
        total = 0
        for signal, output in self.load_display():
            key = self.decode(signal)
            display = 0
            for i, segment in enumerate(reversed(output)):
                num = []
                for char in segment:
                    num.append(key[char])
                display += self.segment_digit[''.join(sorted(num))] * (10**i)
            total += display
        return total