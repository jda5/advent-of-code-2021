import os

FILENAME = os.path.splitext(__file__)
PUZZLE_INPUT = os.path.join('.', 'puzzle-inputs', f'{FILENAME[0]}.txt')

with open(PUZZLE_INPUT, 'r') as f:
    puzzle_input = f.read()


class Card:

    def __init__(self, board):
        self.board = board
        self.num_index = dict()
        self.index_board()

    def index_board(self):
        for i in range(5):
            for j in range(5):
                num = self.board[i][j]
                self.num_index[num] = (i, j)

    def mark_number(self, target):
        if target in self.num_index:
            i, j = self.num_index[target]
            self.board[i][j] = 'x'
            return i, j
        return

    def has_won(self, i, j):
        """
        Checks whether self.board[i] is a winning row and checks if self.baord[k][j] is 
        a winning column
        """
        completed = ['x',] * 5
        if self.board[i] == completed:
            return True
        col = [self.board[k][j] for k in range(5)]
        if col == completed:
            return True
        return False

    def sum_unmarked(self):
        res = 0
        for row in self.board:
            for num in row:
                if num != 'x':
                    res += int(num)
        return res


class Bingo:

    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input
        self.game_numbers = []
        self.cards = []
        self.load_game()

    def load_game(self):
        game = puzzle_input.split('\n\n')
        self.game_numbers = game[0].split(',')
        boards = game[1:]
        for board in boards:
            board = board.split()
            self.cards.append(Card([board[i:i+5] for i in range(0, 25, 5)]))

    def play_to_win(self):
        for num in self.game_numbers:
            for card in self.cards:
                coordinates = card.mark_number(num)
                if coordinates is not None:
                    i, j = coordinates
                    if card.has_won(i, j):
                        return card.sum_unmarked() * int(num)

    def play_to_lose(self):
        finished_cards = set()
        for num in self.game_numbers:
            for card_num, card in enumerate(self.cards):
                if card_num in finished_cards:
                    continue
                coordinates = card.mark_number(num)
                if coordinates is not None:
                    i, j = coordinates
                    if card.has_won(i, j):
                        if len(finished_cards) == len(self.cards) - 1:
                            return card.sum_unmarked() * int(num)
                        else:
                            finished_cards.add(card_num)


def solution_one():
    bingo = Bingo(puzzle_input)
    return bingo.play_to_win()


def solution_two():
    bingo = Bingo(puzzle_input)
    return bingo.play_to_lose()

