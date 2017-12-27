# import needed modules
# TODO: make names PEP-8
import sys
import argparse
import os
from texttable import Texttable
from time import sleep
# define global variables
Cells = []              # collection of all Cells
row_align = []          # centres all Cell
dtype = []              # defines every Cell as string
new_Cells = []
generation = 0


def checkNearbyCells(cell, length):
    living_cells = 0
    #print(cell)
    x = 0
    y = 0
    for hor in [-1, 0, 1]:
        for ver in [-1, 0, 1]:
            if hor == 0 and ver == 0:
                continue
            x = cell[0] + hor
            y = cell[1] + ver
            #print x
            #print y
            if x >= length:
                # 7 + 1 = 8 w.A.
                x = 0
            elif x < 0:
                x = length - 1
                # 8 - 1 = 7
            if y >= length:
                y = 0
            elif y < 0:
                y = length - 1

            # print cell
            #print (str(x)+'\n'+str(y))
            #raw_input('...')
            if Cells[x][y] == 'X':
                living_cells += 1
        #print str(living_cells)+':::',
    # TODO: make a solution for the IndexError failure
    # TODO: shorten!
    #print(living_cells)
    return living_cells


def rebuildTemplate():
    global generation
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
    os.system('clear')
    generation += 1
    print(table.draw())
    print (generation)

def changeState(maxLength):
    # function for building customized field
    exitpress = False
    currentCell = [0,0] # [x-value, y-value]
    oldState = 'O'      # reset to State after ? {Query}
    Cells[0][0] = '?'   # top-left corner as start point
    rebuildTemplate()   # create new frame
    while exitpress == False:   # ability to improve grid as long as the user plays
        cursor = raw_input('\nW A S D to move\nE to revive cell\nX to exit configs\n')
        # decide based on user input

        # move up
        if (cursor[0] == 'w') and (currentCell[0] > - maxLength):
            Cells[currentCell[0]][currentCell[1]] = oldState
            currentCell[0] = int(currentCell[0]) - 1
        # move down
        elif (cursor[0] == 's') and (currentCell[0] < maxLength -1):
            Cells[currentCell[0]][currentCell[1]] = oldState
            currentCell[0] = int(currentCell[0]) + 1
        # move left
        elif (cursor[0] == 'a') and (currentCell[1] > - maxLength):
            Cells[currentCell[0]][currentCell[1]] = oldState
            currentCell[1] = int(currentCell[1]) - 1
        # move right
        elif (cursor[0] == 'd') and (currentCell[1] < maxLength -1):
            Cells[currentCell[0]][currentCell[1]] = oldState
            currentCell[1] = int(currentCell[1]) + 1
        # revive or kill cell
        elif (cursor[0] == 'e') and (oldState == 'O'):
            Cells[currentCell[0]][currentCell[1]] = 'X'
        elif (cursor[0] == 'e') and (oldState == 'X'):
                Cells[currentCell[0]][currentCell[1]] = 'O'
        # exit config
        elif cursor[0] == 'x':
            exitpress = True

        # clear console and re-print
        os.system('clear')
            #print(currentCell)
            #print(maxLength)

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
            cell_part.append('O')
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
            global Cells
            global new_Cells
            new_Cells = Cells
            # check all rules
            for column_cell in range(maxLength):
                for row_cell in range(maxLength):
                    others = checkNearbyCells([column_cell, row_cell], maxLength)
                    if ((others < 2) or (others > 3)) and new_Cells[column_cell][row_cell] == 'X':
                        new_Cells[column_cell][row_cell] = 'O'
                    elif (others == 3) and (new_Cells[column_cell][row_cell] == 'O'):
                        new_Cells[column_cell][row_cell] = 'X'
            Cells = new_Cells
            #sleep(0.5)
            e = raw_input()
            rebuildTemplate()

            # break
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()
