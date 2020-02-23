# !/usr/bin/python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')

from intcode_computer_pt1 import IntcodeComputer

if __name__ == "__main__":
    with open(puzzle_input_path) as f:
        intcode_program_list = f.readlines()

    for program in intcode_program_list:
        input_value = 1
        computer = IntcodeComputer(program)
        computer.compute(input_value)
        print('The resultant diagnostic code for an input value of '
              '{} is {}'.format(input_value, computer.output_value))