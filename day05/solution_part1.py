# !/usr/bin/python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')

# We redefine instruction functions from day02p1 solution
# that we'll extend on for this puzzle

def opcode_add(index, intcode_list):
    # Function to execute when opcode 1 is encounted
    index1, index2, index3 = intcode_list[index+1:index+4]
    value1 = intcode_list[index1]
    value2 = intcode_list[index2]
    final_value = value1 + value2
    intcode_list[index3] = final_value

def opcode_mul(index, intcode_list):
    # Function to execute when opcode 2 is encountered
    index1, index2, index3 = intcode_list[index+1:index+4]
    value1 = intcode_list[index1]
    value2 = intcode_list[index2]
    final_value = value1 * value2
    intcode_list[index3] = final_value

# We now define the functions to execute the new instructions
def opcode_cp(index, intcode_list):
    # Function to execute when opcode 3 is encountered
    integer = int(input('Enter input: '))
    intcode_list[index] = integer

def opcode_output(index, intcode_list):
    # Function to execute when opcode 4 is encountered
    # Returns a value at a given index of the intcode list
    return intcode_list[index]

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