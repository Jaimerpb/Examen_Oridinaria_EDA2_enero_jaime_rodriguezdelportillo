def depth_first_search(possible_board, diagonal_right_collisions, diagonal_left_collisions, boards, n):
    row = len(possible_board)

    if row == n:
        boards.append(possible_board.copy())
        return

    for col in range(n):
        if (
            col in possible_board
            or row - col in diagonal_right_collisions
            or row + col in diagonal_left_collisions
        ):
            continue

        depth_first_search(
            possible_board + [col],
            diagonal_right_collisions + [row - col],
            diagonal_left_collisions + [row + col],
            boards,
            n,
        )


def n_pokeballs_solution(n):
    boards = []
    depth_first_search([], [], [], boards, n)

    return boards


def print_solution(solution):
    for board in solution:
        for row in board:
            print(". " * row + "P " + ". " * (len(board) - 1 - row))
        print("")


pokeballs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]

for n in pokeballs:
    print(f"--- Solutions for {n} pokeballs ---")
    solution = n_pokeballs_solution(n)
    print_solution(solution)
    print(f"Total solutions: {len(solution)}")
    print("===============================")
