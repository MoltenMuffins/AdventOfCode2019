# !/usr/bin/python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')

def get_displacement(direction:str, magnitude:int):
    x_displacement = 0
    y_displacement = 0

    if direction == 'U':
        y_displacement += magnitude
    elif direction == 'D':
        y_displacement -= magnitude
    elif direction == 'R':
        x_displacement += magnitude
    elif direction == 'L':
        x_displacement -= magnitude
    else:
        print('`direction` can only be one of the following: {U, D, L, R}')
    return x_displacement, y_displacement

def path_parser(wire_path:list):
    x_coord = 0
    y_coord = 0
    for step in wire_path:
        direction = step[0]
        magnitude = int(step[1:])
        x_delta, y_delta = get_displacement(direction, magnitude)
        x_coord += x_delta
        y_coord += y_delta
    return x_coord, y_coord

if __name__ == "__main__":
    with open(puzzle_input_path) as f:
        wire_paths = f.readlines()

    wire_path_1 = wire_paths[0].split(',')
    wire_path_2 = wire_paths[1].split(',')