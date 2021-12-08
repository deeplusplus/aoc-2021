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

    # for point_pair in point_pairs:
    for point_pair in point_pairs:
        if point_pair[0][0] == point_pair[1][0] or point_pair[0][1] == point_pair[1][1]:
            points_to_fill = LineInterpolationService.calculate_intermediate_tuples(point_pair)
            for point in points_to_fill:
                point_space.plot_point(point)            


    point_space.print_graph()
    print(point_space.count_of_intersections())



if __name__ == "__main__":
    main()