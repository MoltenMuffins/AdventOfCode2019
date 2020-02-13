# !/usr/bin/python
from solution_part1 import (draw_step,
                            path_parser,
                            find_intersections,
                            shortest_distance)

test_1 = ('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83')
test_2 = ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')

test_cases = {
    159: test_1,
    135: test_2
}

def manhattan_distance(value):
    direction_list_1 = value[0].split(',')
    direction_list_2 = value[1].split(',')

    wire_path_1 = path_parser(direction_list_1)
    wire_path_2 = path_parser(direction_list_2)

    intersections = find_intersections(wire_path_1, wire_path_2)
    return shortest_distance(intersections)

def check_cases():
    for key, value in test_cases.items():
        assert key == manhattan_distance(value)
    print('👍')

if __name__ == "__main__":
    check_cases()