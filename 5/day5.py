from LineInterpolationService import LineInterpolationService
from PointSpace import PointSpace

def main():
    file = open('day5input.txt', 'r')
    lines = file.readlines()
    point_pairs = []

    for line in lines:
        point_pairs.append([(int(pair.strip().split(",")[0]), int(pair.strip().split(",")[1])) for pair in line.split("->")])
    
    x_y_max = LineInterpolationService.get_max_x_and_y(point_pairs)

    point_space = PointSpace(x_y_max)

    print(point_pairs[0])

    points_to_fill = LineInterpolationService.extract_line_tuples(point_pairs[0], point_pairs[1])
    for point in points_to_fill:
        point_space.plot_point(point)

    point_space.print_graph()



if __name__ == "__main__":
    main()