from typing import List
from bresenham import bresenham

class LineInterpolationService:
    
    @staticmethod
    def calculate_intermediate_tuples(point_pair: List[tuple]) -> List[tuple]:
        # print(point_pair[1][0], point_pair[1][1])
        # return list(bresenham(0, 9, 5, 9))
        return list(bresenham(point_pair[0][0], point_pair[0][1], point_pair[1][0], point_pair[1][1]))

    @staticmethod
    def get_max_x_and_y(point_pairs: List[tuple]) -> tuple:
        x_max = 0
        y_max = 0
        for point_pair in point_pairs:
            local_x_max = max(point_pair[0][0], point_pair[1][0])
            x_max = local_x_max if local_x_max > x_max else x_max

            local_y_max = max(point_pair[0][1], point_pair[1][1])
            y_max = local_y_max if local_y_max > y_max else y_max
        return (x_max + 1, y_max)
