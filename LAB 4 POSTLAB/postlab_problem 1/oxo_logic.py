import random
import oxo_data

class Game:
    def __init__(self):
        self.board = list(" " * 9)

    def save(self):
        oxo_data.saveGame(self.board)

    def restore():
        try:
            self.board = oxo_data.restoreGame()
            if len(self.board) == 9:
                return game
        except IOError:
            self.board = list(" " * 9)
            return self.board

    def generate_move(self):
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        if options:
            return random.choice(options)
        return -1

    def is_winning_move(self, player):
        marks = 'X' if player == 'user' else 'O'
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))

        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == marks * 3:
                return True
        return False

    def user_move(self, cell):
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        self.board[cell] = 'X'
        if self.is_winning_move('user'):
            return 'X'
        return ""

    def computer_move(self):
        cell = self.generate_move()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self.is_winning_move('computer'):
            return 'O'
        return ""

    def test(self):
        result = ""
        while not result:
            print(self.board)
            try:
                result = self.user_move(self.generate_move())
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computer_move()
                
            if not result:
                continue
            elif result == 'D':
                print("It's a draw")
            else:
                print("Winner is:", result)
            print(self.board)

if __name__ == "__main__":
    game = Game()
    game.test()
