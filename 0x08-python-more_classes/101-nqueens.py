#!/usr/bin/python3
"""
Module to solve the N-queens problem and print solutions.

The N queens puzzle is the challenge of
placing N non-attacking queens on an N×N chessboard.
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at the given position on the board.

    Args:
        board (list): The chessboard represented as a 2D list.
        row (int): The row index to check.
        col (int): The column index to check.
        n (int): The size of the board.

    Returns:
        bool: True if safe, False otherwise.
    """
    # Check if there is a queen in the same row to the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n, solutions):
    """
    Recursively solve the N-queens problem and store solutions.

    Args:
        board (list): The chessboard represented as a 2D list.
        col (int): The current column being considered.
        n (int): The size of the board.
        solutions (list): A list to store solutions.
    """
    if col >= n:
        solution = [[i, row.index(1)] for i, row in enumerate(board)]
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n, solutions)
            board[i][col] = 0


def print_solutions(solutions):
    """
    Print the list of solutions.

    Args:
        solutions (list): A list of solutions.
    """
    for solution in solutions:
        print(solution)


def nqueens(N):
    """
    Solve the N-queens problem for the given N.

    Args:
        N (str): The size of the chessboard.

    Raises:
        SystemExit: If the input is not valid.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
