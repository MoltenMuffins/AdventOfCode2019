# !/usr/bin/python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')

# We redefine instruction functions from day02p1 solution
# to support immediate mode

def get_value(intcode_list, parameter, mode='0'):
    if mode == '1':
        return parameter
    else:
        # mode == '0'
        # Position mode
        return intcode_list[parameter]

def opcode_add(intcode_list, para1, para2, para3, mode_1, mode_2, mode_3):
    # Function to execute when opcode 1 is encounted
    value1 = get_value(intcode_list, para1, mode_1)
    value2 = get_value(intcode_list, para2, mode_2)

    final_value = value1 + value2

    # Write to intcode_list via position
    _ = mode_3
    intcode_list[para3] = final_value

def opcode_mul(intcode_list, para1, para2, para3, mode_1, mode_2, mode_3):
    # Function to execute when opcode 2 is encountered
    value1 = get_value(intcode_list, para1, mode_1)
    value2 = get_value(intcode_list, para2, mode_2)

    final_value = value1 * value2

    # Write to intcode_list via position
    _ = mode_3
    intcode_list[para3] = final_value

def opcode_input(intcode_list, para, mode):
    # Function to execute when opcode 3 is encountered
    _ = mode
    # integer = int(input('Please Enter input (int): '))
    integer = 1

    # Write to intcode_list via position
    intcode_list[para] = integer

def opcode_output(intcode_list, para, mode):
    # Function to execute when opcode 4 is encountered
    # Returns a value at a given index of the intcode list
    if mode == '0':
        # Get value fia position
        print(intcode_list[para])
    else:
        # Return value
        print(para)

def opcode_stop():
    return False

# Now we define utility functions and variables

def instruction_parser(index, intcode_list):
    instruction = intcode_list[index]
    code = str(instruction)

    opcode = int(code[-2:])
    param_modes = code[:-2]

    if opcode == '99':
        return opcode_stop()

    opcode_meta = {
        1: (opcode_add, 3),
        2: (opcode_mul, 3),
        3: (opcode_input, 1),
        4: (opcode_output, 1),
    }

    # Obtain the opcode function and parameter count
    # from the opcode_meta dictionary
    opcode_fn, arg_count = opcode_meta[opcode]

    # Obtain opcode parameters according to the
    # parameter count via list slicing
    params = intcode_list[index+1:index+1+arg_count]

    # Obtain parameter modes
    param_modes = '0'*(arg_count-len(param_modes)) + param_modes
    modes = [int(mode) for mode in param_modes]

    opcode_fn(intcode_list, *params, *modes)
    return arg_count + 1

def intcode_to_list(intcode_str:str):
    # Converts an intcode program string to a list
    str_list = intcode_str.split(',')
    return [int(x) for x in str_list]

def process_intcode_list(intcode_list:list):
    # Executes an intcode program list and
    # returns the program final state
    index = 0 # Instruction pointer
    completed = False
    while completed is not True:
        step = instruction_parser(index, intcode_list)
        if step:
            index += step
        else:
            completed = True
            break

    return intcode_list

if __name__ == "__main__":
    total_fuel_requirement = 0
    with open(puzzle_input_path) as f:
        intcode_program_list = f.readlines()

    for program in intcode_program_list:
        intcode_list = intcode_to_list(program)

        final_state = process_intcode_list(intcode_list)
