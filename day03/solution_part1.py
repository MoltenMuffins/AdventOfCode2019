# !/usr/bin/python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')

def draw_step(direction:str):
    x_displacement = 0
    y_displacement = 0

    if direction == 'U':
        y_displacement += 1
    elif direction == 'D':
        y_displacement -= 1
    elif direction == 'R':
        x_displacement += 1
    elif direction == 'L':
        x_displacement -= 1
    else:
        print('`direction` can only be one of the following: {U, D, L, R}')
    return x_displacement, y_displacement

def path_parser(wire_path:list):
    # We define the path the wire takes
    # as a list of coordinates in gridspace
    coordinates = [(0, 0)]
    for step in wire_path:
        direction = step[0]
        magnitude = int(step[1:])

        # The pairs of new points is obtained by
        # atomically adding displacements
        for _ in range(magnitude):
            x_delta, y_delta = draw_step(direction)
            previous_pair = coordinates[-1]
            x_coord = (previous_pair[0] + x_delta)
            y_coord = (previous_pair[1] + y_delta)
            coordinates.append((x_coord, y_coord))
    return coordinates

def find_intersections(path1, path2):
    # Returns a list of tuples
    # indicating coordinates where
    # the wires cross, inclusive of the
    # origin point 
    intersections = [(0, 0)]
    for x1, y1 in path1:
        for x2, y2 in path2:
            if x1 == x2 and y1 == y2:
                intersections.append((x1, y1))
    return intersections

def shortest_distance(coordinate_list):
    # Returns the shortest non-zero
    # manhattan distance from the point
    # of origin, given a list of coordinates
    distance_list = [abs(x) + abs(y) for x, y in coordinate_list]
    distance_list = [x for x in distance_list if x != 0]
    return min(distance_list)

if __name__ == "__main__":
    with open(puzzle_input_path) as f:
        wire_paths = f.readlines()

    direction_list_1 = wire_paths[0].split(',')
    direction_list_2 = wire_paths[1].split(',')

    wire_path_1 = path_parser(direction_list_1)
    wire_path_2 = path_parser(direction_list_2)

    intersections = find_intersections(wire_path_1, wire_path_2)
    print(shortest_distance(intersections))