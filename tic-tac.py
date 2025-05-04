import copy

class TicTacToe:
    def __init__(self):
        self.board = [[' ']*3 for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-'*5)

    def check_winner(self, board):
        lines = board + [list(col) for col in zip(*board)] + \
            [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
        for line in lines:
            if line[0] == line[1] == line[2] != ' ':
                return line[0]
        if all(cell != ' ' for row in board for cell in row):
            return 'D'  # Draw
        return None

    def get_moves(self, board):
        return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

    def heuristic(self, board):
        winner = self.check_winner(board)
        if winner == 'O':
            return 0
        elif winner == 'X':
            return 10
        elif winner == 'D':
            return 5
        return 1  # Not finished

    def best_move(self):
        best_score = float('inf')
        move = None
        for i, j in self.get_moves(self.board):
            new_board = copy.deepcopy(self.board)
            new_board[i][j] = 'O'
            score = self.heuristic(new_board)
            if score < best_score:
                best_score = score
                move = (i, j)
        return move

    def play(self):
        while True:
            self.print_board()
            if self.current_player == 'X':
                row, col = map(int, input("Enter row and col (0-2): ").split())
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'X'
                    self.current_player = 'O'
            else:
                print("AI is thinking...")
                move = self.best_move()
                if move:
                    self.board[move[0]][move[1]] = 'O'
                self.current_player = 'X'

            winner = self.check_winner(self.board)
            if winner:
                self.print_board()
                if winner == 'D':
                    print("It's a draw!")
                else:
                    print(f"{winner} wins!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
