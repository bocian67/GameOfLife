import sys
import argparse
import os
from texttable import Texttable
Cells = [['+', '0', '0', '0'], ['0', '+', '0', '0'], ['0', '0', '+', '0'], ['0', '0', '0', '+']]
table = Texttable()


def changeStates():
    pass


def playRound():
    columnCol = []
    for column in Cells:
        columnCol.append(column)
    table.add_rows(columnCol)
    print(table.draw())


def buildEmptyTemplate(length):
    row_align = []
    for x in range(length):
        row_align.append('c')
    #row_align = ['c', 'c', 'c', 'c']
    table.set_cols_align(row_align)
    table.set_cols_valign(row_align)


def main():
    parser = argparse.ArgumentParser('Canways Game of Life!')
    parser.add_argument('-f', metavar='NUMBER', help='Number of fields in Row and Column',\
                        type=int)
    args = parser.parse_args()
    try:
        buildEmptyTemplate(int(args.f))
        while True:
            playRound()
            changeStates()
            break
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()