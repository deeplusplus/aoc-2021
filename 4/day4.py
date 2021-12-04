from typing import List
from BingoCell import BingoCell
from BingoBoard import BingoBoard

#stole this from SO
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def board_from_lines(lines: List[str]) -> BingoBoard:
    board_cells = []
    row = []
    for line in lines:
        for char in line.split():
            row.append(BingoCell((int(char.strip()), False)))
        board_cells.append(row)
        row = []

    board = BingoBoard(board_cells)
    return board

def main():
    file = open('day4input.txt', 'r')
    lines = file.readlines()
    board_list = []

    call_numbers = [int(char.strip()) for char in lines[0].split(',')]

    filtered_lines = chunks([line for line in lines[2:] if not line.isspace()], 5)

    for board_lines in filtered_lines:
       board = board_from_lines(board_lines)
       board_list.append(board)

    for number in call_numbers:
        for board in board_list:
            board.mark_number(int(number))
            if board.is_winning_board():
                print("A BOARD WON!")
                board.print_board()
                print(board.score(number))
                return

if __name__ == "__main__":
    main()