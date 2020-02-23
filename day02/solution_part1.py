# !/usr/bin/python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')

from intcode_computer import IntcodeComputer

if __name__ == "__main__":
    total_fuel_requirement = 0
    with open(puzzle_input_path) as f:
        intcode_program_list = f.readlines()

    for program in intcode_program_list:
        print('Running Intcode Computer...')
        computer = IntcodeComputer(program)

        # First we apply the changes to the puzzle input according
        # to the instructions in the puzzle
        computer.edit_input(1, 12)
        computer.edit_input(2, 2)

        # We then run the program to process
        # the intcode program
        computer.compute()
        computer.pprint_output()
        computer.print_position_0()

