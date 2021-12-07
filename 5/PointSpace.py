from typing import Dict


class PointSpace:
    
    def __init__(self, x_y_maxes: tuple) -> None:
        self.point_dict = {}
        self.x_max = x_y_maxes[0]
        self.y_max = x_y_maxes[1]

        for x in range(0, self.x_max):
            for y in range(0, self.y_max):
                self.point_dict[(x, y)] = 0
        

    def plot_point(self, point_tuple) -> None:
            self.point_dict[point_tuple] += 1

    def print_graph(self):
        for x in range(0, self.x_max):
            printed_line = ""
            for y in range(0, self.y_max):
                printed_line += "-" if self.point_dict[(x, y)] == 0 else self.point_dict[(x, y)]
            print(printed_line)