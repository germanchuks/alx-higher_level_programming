#!/usr/bin/python3
import sys


def is_safe(board, current_row, current_col):
    """
    Check if it's safe to place a queen at the given position on the
    chessboard.

    Args:
        board (list): The current state of the chessboard.
        current_row (int): The row where we want to place a queen.
        current_col (int): The column where we want to place a queen.

    Returns:
        bool: True if it's safe to place a queen; False otherwise.
    """
    for i in range(current_row):
        if board[i] == current_col or \
          board[i] - i == current_col - current_row or \
           board[i] + i == current_col + current_row:
            return (False)
    return (True)


def solve_nqueens(n):
    """
    Find all solutions to the N Queens puzzle for a given board size.

    Args:
        n (int): The size of the chessboard (N × N).

    Returns:
        list: A list of solutions, where each solution is a list of queen
        positions.
    """
    def solve(board, current_row):
        if current_row == n:
            result.append(board[:])
            return
        for current_col in range(n):
            if is_safe(board, current_row, current_col):
                board[current_row] = current_col
                solve(board, current_row + 1)

    result = []
    solve([-1] * n, 0)
    return (result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solve_nqueens(N)
    for solution in solutions:
        print([[i, j] for i, j in enumerate(solution)])
