def solve_n_queens(n):
    board = [-1] * n  # board[i] stores the column of the queen in row i

    def is_safe(row, col):
        for r in range(row):
            if board[r] == col or \
               abs(board[r] - col) == abs(r - row):
                return False
        return True

    def solve(row):
        if row == n:
            print_solution()
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)

    def print_solution():
        for row in range(n):
            line = ['.'] * n
            line[board[row]] = 'Q'
            print(''.join(line))
        print()

    solve(0)

# Example: Solve for 4 queens
solve_n_queens(8)
