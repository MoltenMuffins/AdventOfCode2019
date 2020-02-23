# !/usr/bin/python
import os
from solution_part1 import (draw_step,
                            path_parser,
                            puzzle_input_path)

def find_intersections_count(path1, path2, early=False):
    # Returns a list of tuples
    # indicating coordinates where
    # the wires cross, inclusive of the
    # origin point 
    intersection_counts = []
    for n1, (x1, y1) in enumerate(path1):
        for n2, (x2, y2) in enumerate(path2):
            if x1 == x2 and y1 == y2:
                intersection_counts.append(n1+n2)
                if early and len(intersection_counts)==2:
                    break
    return intersection_counts

if __name__ == "__main__":
    with open(puzzle_input_path) as f:
        wire_paths = f.readlines()

    direction_list_1 = wire_paths[0].split(',')
    direction_list_2 = wire_paths[1].split(',')

    wire_path_1 = path_parser(direction_list_1)
    wire_path_2 = path_parser(direction_list_2)

    intersection_distances = find_intersections_count(wire_path_1, wire_path_2, early=True)
    intersection_distances.remove(0)

    result = 'The fewest combined steps the wires must take to reach an intersection is {} steps'
    print(result.format(min(intersection_distances)))