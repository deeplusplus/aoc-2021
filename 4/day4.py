from BingoCell import BingoCell
from BingoBoard import BingoBoard


def main():
    file = open('day4input.txt', 'r')
    lines = file.readlines()

    call_numbers = [char.strip() for char in lines[0].split(',')]

    #make bingo cells then make board
    board_cells = []
    for line in lines[2:]:
        row = []
        for char in line.split():
            row.append(BingoCell((int(char.strip()), False)))
        board_cells.append(row)

    board = BingoBoard(board_cells)


    for number in call_numbers:
        board.mark_number(int(number))        

    board.print_board()
    print(board.is_winning_board())

if __name__ == "__main__":
    main()