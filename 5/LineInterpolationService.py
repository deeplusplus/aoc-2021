from typing import List


class LineInterpolationService:
    
    @staticmethod
    def extract_line_tuples(line_begin: tuple, line_end: tuple) -> List[tuple]:
        x_range = range(line_begin[0][0], line_end[1][0])
        y_range = range(line_begin[0][1], line_end[1][1])
        line_points = []

        print("X Range: ", x_range)
        print("Y Range: ", y_range)
        for x_stop in x_range:
            for 
            line_points.append((x_range[stop], y_range[stop]))

        return line_points

    @staticmethod
    def get_max_x_and_y(point_pairs: List[tuple]) -> tuple:
        x_max = 0
        y_max = 0
        for point_pair in point_pairs:
            local_x_max = max(point_pair[0][0], point_pair[1][0])
            x_max = local_x_max if local_x_max > x_max else x_max

            local_y_max = max(point_pair[0][1], point_pair[1][1])
            y_max = local_y_max if local_y_max > y_max else y_max
        return (x_max, y_max)