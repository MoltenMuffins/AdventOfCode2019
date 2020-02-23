# !/usr/bin/python
from solution_part1 import puzzle_input_path
from intcode_computer_pt2 import IntcodeComputer

if __name__ == "__main__":
    total_fuel_requirement = 0
    with open(puzzle_input_path) as f:
        intcode_program_list = f.readlines()

    for program in intcode_program_list:
        input_value = 5
        computer = IntcodeComputer(program)
        computer.compute(input_value)
        print('The resultant diagnostic code for system ID '
              '{} is {}'.format(input_value, computer.output_value))

