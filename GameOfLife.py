import sys
import argparse
import os
from texttable import Texttable
Cells = []
row_align = []
dtype = []

class Cell:
    x = 0
    y = 0
    alive = False

    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive


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

def changeState(template, maxLength):
    exitpress = False
    currentCell = [0,0,0] #[x-value, y-value, awoken]
    Cells[0][0] = '?'
    rebuildTemplate()
    while exitpress == False:
        Cells[currentCell[0]][currentCell[1]]= '0'

        cursor = raw_input('\nW A S D to move, E to revive cell\n')
        if (cursor == 'w') and (currentCell[0] > -maxLength):
            currentCell[0] = int(currentCell[0]) - 1
        elif (cursor == 's') and (currentCell[0] < maxLength -1):
            currentCell[0] = int(currentCell[0]) + 1
        elif (cursor == 'a') and (currentCell[1] > - maxLength):
            currentCell[1] = int(currentCell[1]) - 1
        elif (cursor == 'd') and (currentCell[1] < maxLength -1):
            currentCell[1] = int(currentCell[1]) + 1
        elif (cursor == 'e') and (currentCell[2] == False):
            currentCell[2] = True
            Cells[currentCell[0]][currentCell[1]] = '1'
        os.system('clear')
        print currentCell
        print maxLength
        Cells[currentCell[0]][currentCell[1]] = '?'
        rebuildTemplate()


def buildEmptyTemplate(maxLength):
    print maxLength
    for x in range(maxLength):
        row_align.append('c')
        dtype.append('s')
        cell_part = []
        for item in range(maxLength):
            cell_part.append('0')
        Cells.append(cell_part)
    #row_align = ['c', 'c', 'c', 'c']
    #print(row_align)



def main():
    parser = argparse.ArgumentParser('Canways Game of Life!')
    parser.add_argument('-f', metavar='NUMBER', help='Number of fields in Row and Column',\
                        type=int)
    args = parser.parse_args()
    maxLength = int(args.f)
    try:
        template = buildEmptyTemplate(maxLength)
        game = changeState(template, maxLength)
        while True:
            playRound()
            changeStates()
            break
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()