# import needed modules
import sys
import argparse
import os
from texttable import Texttable

# define global variables
Cells = []              # collection of all Cells
row_align = []          # centres all Cell
dtype = []              # defines every Cell as string


def changeStates():
    pass


def playRound():
    pass


def rebuildTemplate():
    table = Texttable()
    table.set_chars(['-', '|', '+', '-'])
    table.set_deco(Texttable.BORDER|\
    Texttable.HEADER|\
    Texttable.HLINES|\
    Texttable.VLINES)
    table.set_cols_dtype(dtype)
    table.set_cols_align(row_align)
    table.set_cols_valign(row_align)
    columnCol = []

    for column in Cells:
        columnCol.append(column)
    table.add_rows(columnCol)
    print(table.draw())


def changeState(maxLength):
    # function for building customized field
    exitpress = False
    currentCell = [0,0] # [x-value, y-value]
    oldState = '0'      # reset to State after ? {Query}
    Cells[0][0] = '?'   # top-left corner as start point
    rebuildTemplate()   # create new frame
    while exitpress == False:   # ability to improve grid as long as the user plays
        cursor = raw_input('\nW A S D to move\nE to revive cell\nX to exit configs\n')
        # decide based on user input
        # move up
        if (cursor == 'w') and (currentCell[0] > -maxLength):
            Cells[currentCell[0]][currentCell[1]] = oldState
            currentCell[0] = int(currentCell[0]) - 1
        # move down
        elif (cursor == 's') and (currentCell[0] < maxLength -1):
            Cells[currentCell[0]][currentCell[1]] = oldState
            currentCell[0] = int(currentCell[0]) + 1
        # move left
        elif (cursor == 'a') and (currentCell[1] > - maxLength):
            Cells[currentCell[0]][currentCell[1]] = oldState
            currentCell[1] = int(currentCell[1]) - 1
        # move right
        elif (cursor == 'd') and (currentCell[1] < maxLength -1):
            Cells[currentCell[0]][currentCell[1]] = oldState
            currentCell[1] = int(currentCell[1]) + 1
        # revive or kill cell
        elif (cursor == 'e') and (oldState == '0'):
            Cells[currentCell[0]][currentCell[1]] = 'X'
        elif (cursor == 'e') and (oldState == 'X'):
                Cells[currentCell[0]][currentCell[1]] = '0'
        # exit config
        elif cursor == 'x':
            exitpress = True

        # clear console and re-print
        os.system('clear')
        print(currentCell)
        print(maxLength)

        oldState = Cells[currentCell[0]][currentCell[1]]
        Cells[currentCell[0]][currentCell[1]] = '?'
        rebuildTemplate()


def buildEmptyTemplate(maxLength):
    # create as much cells as user inputs (IxI)
    for x in range(maxLength):
        # centers
        row_align.append('c')
        # defines as string
        dtype.append('s')
        # cell_part is Row
        cell_part = []
        for item in range(maxLength):
            cell_part.append('0')
        Cells.append(cell_part)


def main():
    # get field-number
    parser = argparse.ArgumentParser('Conways Game of Life!')
    parser.add_argument('-f', metavar='NUMBER', help='Number of fields in Row = Column',\
                        type=int)
    args = parser.parse_args()
    maxLength = int(args.f)
    try:
        # default-board
        buildEmptyTemplate(maxLength)
        # configure board
        changeState(maxLength)
        while True:
            # check all rules
            playRound()
            changeStates()
            # break
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()
