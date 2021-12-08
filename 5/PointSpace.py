from typing import Dict


class PointSpace:
    
    def __init__(self, x_y_maxes: tuple) -> None:
        self.point_dict = {}
        self.x_max = x_y_maxes[0]
        self.y_max = x_y_maxes[1]

        for x in range(0, self.x_max + 1):
            for y in range(0, self.y_max + 1):
                self.point_dict[(x, y)] = 0
        

    def plot_point(self, point_tuple) -> None:
            self.point_dict[point_tuple] += 1

    def print_graph(self):
        for x in range(0, self.x_max + 1):
            printed_line = ""
            for y in range(0, self.y_max + 1):
                added_char = "-"
                if self.point_dict[(x, y)] != 0:
                    added_char = str(self.point_dict[(x, y)])                    
                printed_line += added_char
            print(printed_line)

    def count_of_intersections(self):
        count = 0
        for values in self.point_dict.values():
            if values > 1:
                count += 1
        return count