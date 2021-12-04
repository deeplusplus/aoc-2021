class BingoCell:

    def __init__(self, cell_tuple: tuple) -> None:
        self.cell_tuple = cell_tuple

    def value(self) -> int:
        return self.cell_tuple[0]

    def mark_cell(self) -> None:
        self.cell_tuple = (self.cell_tuple[0], True)

    def is_marked(self) -> bool:
        return self.cell_tuple[1]