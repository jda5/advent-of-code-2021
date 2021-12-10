import os

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')


class Syntax:

    def __init__(self):
        self.pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

    def load_input(self):
        with open(PUZZLE_INPUT, 'r') as f:
            for row in f.read().splitlines():
                yield row

    def is_corrupted(self, line):
        stack = []
        for char in line:
            if char in self.pairs:
                stack.append(char)
            else:
                bracket = stack.pop()
                if self.pairs[bracket] != char:
                    return (True, char)
        return (False, stack)

    def solution_one(self):
        error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
        score = 0
        for line in self.load_input():
            corrupted, char = self.is_corrupted(line)
            if corrupted:
                score += error_scores[char]
        return score

    def solution_two(self):
        complete_scores = {')': 1, ']': 2, '}': 3, '>': 4}
        line_scores = []
        for line in self.load_input():
            score = 0
            corrupted, stack = self.is_corrupted(line)
            if not corrupted:
                for bracket in reversed(stack):
                    score *= 5
                    score += complete_scores[self.pairs[bracket]]
                line_scores.append(score)
        line_scores.sort()
        return line_scores[len(line_scores) // 2]