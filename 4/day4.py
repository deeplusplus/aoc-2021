from BingoCell import BingoCell
from BingoBoard import BingoBoard


def main():
    file = open('day4input.txt', 'r')
    lines = file.readlines()

    #make list of list of bingo cells
    board_cells = []
    for line in lines:
        row = []
        for char in line.split():
            row.append(BingoCell((int(char.strip()), False)))
        board_cells.append(row)

    board = BingoBoard(board_cells)
    board.print_board()

if __name__ == "__main__":
    main()