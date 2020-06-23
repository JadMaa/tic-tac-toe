# write your code here
def check_draw(matrix):
    return not any("_" in x for x in matrix) and not(check_win(matrix, 'X') or check_win(matrix, 'O'))


def check_win(matrix, player):
    for x in range(3):
        for y in range(3):
            if (matrix[x][0] == matrix[x][1] == matrix[x][2] == player) \
                    or (matrix[0][y] == matrix[1][y] == matrix[2][y] == player) \
                    or (matrix[0][0] == matrix[1][1] == matrix[2][2] == player) \
                    or (matrix[2][0] == matrix[1][1] == matrix[0][2] == player):
                return player
    return False


def initialize_board(symbols_list):
    matrix = []
    for i in range(len(symbols_list)):
        if i % 3 == 0:
            matrix.append([symbols_list[i], symbols_list[i + 1], symbols_list[i + 2]])
    return matrix


def print_board(matrix):
    print("-" * 9)
    for row in matrix:
        print("| " + " ".join(row) + " |")
    print("-" * 9)


def add_move(matrix, player):
    coord_is_valid = False
    matrix.reverse()

    while not coord_is_valid:
        print("Enter coordinates")
        coordinates = input().split()
        if not coordinates[0].isdigit() or not coordinates[1].isdigit():
            print("You should enter numbers!")
        elif not 1 <= int(coordinates[0]) <= 3 or not 1 <= int(coordinates[1]) <= 3:
            print("Coordinates should be from 1 to 3!")
        elif matrix[int(coordinates[1]) - 1][int(coordinates[0]) - 1] != '_':
            print("This cell is occupied! Choose another one!")
        else:
            coord_is_valid = True

    matrix[int(coordinates[1]) - 1][int(coordinates[0]) - 1] = player
    matrix.reverse()


is_draw = False
is_win = False
players = ['X', 'O']

symbols = 9 * "_"
tic_tac_toe_matrix = initialize_board(symbols)
print_board(tic_tac_toe_matrix)

while not is_win or not is_draw:
    for player in players:
        add_move(tic_tac_toe_matrix, player)
        print_board(tic_tac_toe_matrix)
        is_draw = check_draw(tic_tac_toe_matrix)
        is_win = check_win(tic_tac_toe_matrix, player)
        if is_win:
            print(player + " wins")
            exit()
        if is_draw:
            print("Draw")
            exit()
