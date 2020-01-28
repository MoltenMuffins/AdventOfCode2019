# !/usr/bin/python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')


def opcode_add(index, intcode_list):
    # Function to execute when opcode 1 is encounted
    index1, index2, index3 = intcode_list[index+1:index+4]
    value1 = intcode_list[index1]
    value2 = intcode_list[index2]
    final_value = value1 + value2
    intcode_list[index3] = final_value
    # print('({} + {} = {})'.format(value1, value2, final_value))

def opcode_mul(index, intcode_list):
    # Function to execute when opcode 2 is encountered
    index1, index2, index3 = intcode_list[index+1:index+4]
    value1 = intcode_list[index1]
    value2 = intcode_list[index2]
    final_value = value1 * value2
    intcode_list[index3] = final_value
    # print('({} * {} = {})'.format(value1, value2, final_value))

def intcode_to_list(intcode_str:str):
    # Converts an intcode program string to a list
    str_list = intcode_str.split(',')
    return [int(x) for x in str_list]

def process_intcode_list(intcode_list:list):
    # Excites an intcode program list and
    # returns the program final state
    index = 0 # Instruction pointer
    completed = False
    while completed is not True:
        digit = intcode_list[index]
        if digit == 1:
            opcode_add(index, intcode_list)
            index += 4
        elif digit == 2:
            opcode_mul(index, intcode_list)
            index += 4
        elif digit == 99:
            completed = True
            break
        else:
            index += 1

    return intcode_list

def pprint_intcode_list(intcode_list:list):
    # Utility function to pretty-print
    # intcode programs as per the puzzle
    # documentation
    index = 0
    final_index = len(intcode_list)
    completed = False
    while completed is not True:
        if index == final_index:
            break
        digit = intcode_list[index]
        if digit == 1:
            print(*intcode_list[index:index+4])
            index += 4
        elif digit == 2:
            print(*intcode_list[index:index+4])
            index += 4
        elif digit == 99:
            print(intcode_list[index])
            index += 1
        else:
            index += 1

    return intcode_list

if __name__ == "__main__":
    total_fuel_requirement = 0
    with open(puzzle_input_path) as f:
        intcode_program_list = f.readlines()

    for program in intcode_program_list:
        intcode_list = intcode_to_list(program)
        # First we apply the changes to the puzzle input according
        # to the instructions in the puzzle
        intcode_list[1] = 12
        intcode_list[2] = 2

        # We then run the program to process
        # the intcode program
        final_state = process_intcode_list(intcode_list)
        print('The program final state is:')
        pprint_intcode_list(final_state)

        print('The new value of position 0 is {}'.format(final_state[0]))


