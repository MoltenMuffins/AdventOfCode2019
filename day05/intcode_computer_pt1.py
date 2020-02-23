# Part 1:
# We redefine instruction functions from Day 2 Part 1's solution to support immediate mode

def intcode_to_list(intcode_str:str):
    # Converts an intcode program string to a list
    str_list = intcode_str.split(',')
    return [int(x) for x in str_list]

class IntcodeComputer(object):
    def __init__(self, program:str):
        self.intcode_list = intcode_to_list(program)
        self.final_state = 'Computation not yet executed'
        self.output_value = None

    def get_value(self, parameter, mode='0'):
        if mode == 1:
            return parameter
        else:
            # mode == 0
            # Position mode
            return self.intcode_list[parameter]

    def opcode_add(self, para1, para2, para3, mode1, mode2, mode3):
        # Function to execute when opcode 1 is encounted
        value1 = self.get_value(para1, mode1)
        value2 = self.get_value(para2, mode2)

        final_value = value1 + value2

        # Write to intcode_list via position
        _ = mode3
        self.intcode_list[para3] = final_value

        # Move pointer by 4 steps
        return 4

    def opcode_mul(self, para1, para2, para3, mode1, mode2, mode3):
        # Function to execute when opcode 2 is encountered
        value1 = self.get_value(para1, mode1)
        value2 = self.get_value(para2, mode2)

        final_value = value1 * value2

        # Write to intcode_list via position
        _ = mode3
        self.intcode_list[para3] = final_value

        # Move pointer by 4 steps
        return 4

    def opcode_input(self, para, mode):
        # Function to execute when opcode 3 is encountered
        _ = mode
        
        try:
            integer = self.input_value
        except ValueError:
            prompt = 'Input value not instantiated. Please Enter input (int):'
            integer = int(input(prompt))

        # Write to intcode_list via position
        self.intcode_list[para] = integer

        # Move pointer by 2 steps
        return 2

    def opcode_output(self, para, mode):
        # Function to execute when opcode 4 is encountered
        # Returns a value
        self.output_value = self.get_value(para, mode)

        # Move pointer by 2 steps
        return 2

    def opcode_stop(self):
        return False

    # Now we define utility functions and variables
    def instruction_parser(self, index):
        instruction = self.intcode_list[index]
        code = str(instruction)

        opcode = int(code[-2:])
        param_modes = code[:-2]

        if opcode == 99:
            return self.opcode_stop()

        opcode_meta = {
        1: (self.opcode_add, 3),
        2: (self.opcode_mul, 3),
        3: (self.opcode_input, 1),
        4: (self.opcode_output, 1),
        }

        # Obtain the opcode function and parameter count
        # from the opcode_meta dictionary
        opcode_fn, arg_count = opcode_meta[opcode]

        # Obtain opcode parameters according to the
        # parameter count via list slicing
        params = self.intcode_list[index+1:index+1+arg_count]

        # Obtain parameter modes
        param_modes = '0'*(arg_count-len(param_modes)) + param_modes
        modes = [int(mode) for mode in reversed(param_modes)]

        move_pointer = opcode_fn(*params, *modes)
        return move_pointer

    def process_intcode_list(self):
        # Executes an intcode program list and
        # returns the program final state
        index = 0 # Instruction pointer
        completed = False
        while completed is not True:
            step = self.instruction_parser(index)
            if step:
                index += step
            else:
                completed = True
                break

        return self.intcode_list

    def compute(self, input_value:int=0):
        self.input_value = input_value
        self.final_state = self.process_intcode_list()