from os import system, name
from time import sleep

global board


def main():
    init_board()


def init_board():
    global board
    count = 0
    board = []
    try:
        count = int(input("How many rows and columns should the board contain? (ex. '6')"))
    except:
        print("Enter a valid number")
        exit(0)

    for column in range(0, count):
        column = []
        for item in range(0, count):
            column.append("o")
        board.append(column)

    show_board()
    init_user_choice()
    start_simulation()


def show_board():
    row_nr = 0
    for r in board:
        col_nr = 0
        line = "|"
        for c in r:
            line = line + board[row_nr][col_nr] + "|"
            col_nr += 1
        row_nr += 1
        print(line)


def init_user_choice():
    clear()
    is_changing = True
    pos = [0, 0]
    while is_changing:
        clear()
        print("You are here: +\nTo navigate use WASD\nTo revive press x, to kill press o\nExit with c")
        old_value = board[pos[0]][pos[1]]
        old_pos = [pos[0], pos[1]]
        board[pos[0]][pos[1]] = "+"
        show_board()
        direction = input()
        if (direction == "a") & (pos[1] > 0):
            pos[1] = pos[1] - 1
        elif (direction == "w") & (pos[0] > 0):
            pos[0] = pos[0] - 1
        elif (direction == "d") & (pos[1] < len(board) - 1):
            pos[1] = pos[1] + 1
        elif (direction == "s") & (pos[0] < len(board) - 1):
            pos[0] = pos[0] + 1
        elif direction == "c":
            is_changing = False
        elif direction == "x":
            old_value = "x"
        elif direction == "o":
            old_value = "o"
        board[old_pos[0]][old_pos[1]] = old_value


def start_simulation():
    iteration = 1
    while True:
        try:
            clear()
            print("Iteration: "+str(iteration))
            # iterate through cells
            cell_value = ""
            row_nr = 0
            for row in board:
                col_nr = 0
                for col in row:
                    cell_value = board[row_nr][col_nr]
                    neighbours = count_neighbours(row_nr, col_nr)
                    if (neighbours > 2) & (neighbours < 3) & (cell_value == "o"):
                        board[row_nr][col_nr] = "x"
                    if (neighbours < 2) & (neighbours > 3) & (cell_value == "x"):
                        board[row_nr][col_nr] = "o"
                    col_nr += 1
                row_nr += 1
            show_board()
            iteration += 1
            sleep(1)
        except KeyboardInterrupt:
            exit(0)


# TODO: This function is returning too low values
def count_neighbours(row_nr, col_nr):
    count = 0
    length = len(board) - 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(i != 0) & (j != 0):
                r = row_nr + i
                c = col_nr + j
                if (r >= 0) & (r <= length) & (c >= 0) & (c <= length):
                    if board[r][c] == "x":
                        count += 1
    return count


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == '__main__':
    main()
