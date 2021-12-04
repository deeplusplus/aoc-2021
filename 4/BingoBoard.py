from typing import List
from BingoCell import BingoCell


class BingoBoard:

    def __init__(self, cell_lists: List[List[BingoCell]]) -> None:
        self.cell_lists = cell_lists

    def is_winning_board(self) -> bool:

        # Check for horizontal win condition
        for row in self.cell_lists:
            for row_cell in row:
                if not row_cell.is_marked():
                    break
                return True
        
        #Check for vertical win condition
        for index in range(0, 6):
            for row in self.cell_lists:
                if not row[index].is_marked():
                    break
                return True
        
        return False

    def unmarked_sum(self) -> int:
        sum = 0
        for row in self.cell_lists:
            for cell in row:
                if not cell.is_marked():
                    sum += cell.value
        return sum

    def board_score(self, last_called_number: int) -> int:
        return self.unmarked_sum() * last_called_number

    def print_board(self) -> None:
        lines = []
        for row in self.cell_lists:
            line_string = ""
            for cell in row:
                accent = "*" if cell.is_marked() else ""
                line_string += str(cell.value()) + accent + " "
            lines.append(line_string)

        for line in lines:
            print(line)