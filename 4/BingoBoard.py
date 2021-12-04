from typing import List
from BingoCell import BingoCell


class BingoBoard:

    def __init__(self, cell_lists: List[List[BingoCell]]) -> None:
        self.cell_rows = cell_lists

    def mark_number(self, value: int) -> None:
        for row in self.cell_rows:
            for cell in row:
                if cell.value() == value:
                    cell.mark_cell()

    def is_winning_board(self) -> bool:

        # Check for horizontal win condition
        for row in self.cell_rows:
            row_winner = row[0].is_marked() and row[1].is_marked() and row[2].is_marked() \
                 and row[3].is_marked() and row[4].is_marked()
            if row_winner:
                return True

        #Check for vertical win condition
        for index in range(0, 5):
            col_winner = 0
            for row in self.cell_rows:
                col_winner += 1 if row[index].is_marked() else 0
            if col_winner == 5:
                return True
        return False

    def unmarked_sum(self) -> int:
        sum = 0
        for row in self.cell_rows:
            for cell in row:
                if not cell.is_marked():
                    sum += cell.value
        return sum

    def board_score(self, last_called_number: int) -> int:
        return self.unmarked_sum() * last_called_number

    def print_board(self) -> None:
        lines = []
        for row in self.cell_rows:
            line_string = ""
            for cell in row:
                accent = "*" if cell.is_marked() else ""
                line_string += str(cell.value()) + accent + " "
            lines.append(line_string)

        for line in lines:
            print(line)