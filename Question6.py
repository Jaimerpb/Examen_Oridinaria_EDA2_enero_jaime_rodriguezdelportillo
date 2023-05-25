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


n = 4
solutions = n_pokeballs_solution(n)

print("Soluciones distintas:", len(solutions))
print("Todas las soluciones:")
for solution in solutions:
    print_solution([solution])
    print("")

print("Una solución:")
print_solution([solutions[0]])
