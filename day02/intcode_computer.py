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

class IntcodeComputer(object):
    def __init__(self, program:str):
        self.intcode_list = intcode_to_list(program)
        self.final_state = 'Computation not yet executed'

    def edit_input(self, index:int, value:int):
        self.intcode_list[index] = value

    def compute(self):
        self.final_state = process_intcode_list(self.intcode_list)
        
    def print_output(self):
        print('The program final state is:')
        print(self.final_state)

    def pprint_output(self):
        print('The program final state is:')
        pprint_intcode_list(self.final_state)

    def print_position_0(self):
        print('The new value of position 0 is {}'.format(self.final_state[0]))
