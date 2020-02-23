from intcode_computer_pt1 import IntcodeComputer as IntcodeComputer_old

# We extend the IntcodeComputer class to support the
# additional intcode operations
class IntcodeComputer(IntcodeComputer_old):
    def op_jump_true(self, para1, para2, mode1, mode2):
        value1 = self.get_value(para1, mode1)
        if value1 != 0:
            value2 = self.get_value(para2, mode2)
            # We need to change the value of the outer index
            return (value2,)
        else:
            # Otherwise, move pointer by 3 steps
            return 3

    def op_jump_false(self, para1, para2, mode1, mode2):
        value1 = self.get_value(para1, mode1)
        if value1 == 0:
            value2 = self.get_value(para2, mode2)
            # We need to change the value of the outer index
            return (value2,)
        else:
            # Otherwise, move pointer by 3 steps
            return 3

    def op_less_than(self, para1, para2, para3, mode1, mode2, mode3):
        value1 = self.get_value(para1, mode1)
        value2 = self.get_value(para2, mode2)

        _ = mode3
        if value1 < value2:
            self.intcode_list[para3] = 1
        else:
            self.intcode_list[para3] = 0

        # Move pointer by 4 steps
        return 4

    def op_equals(self, para1, para2, para3, mode1, mode2, mode3):
        value1 = self.get_value(para1, mode1)
        value2 = self.get_value(para2, mode2)

        _ = mode3
        if value1 == value2:
            self.intcode_list[para3] = 1
        else:
            self.intcode_list[para3] = 0

        # Move pointer by 4 steps
        return 4

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
            5: (self.op_jump_true, 2),
            6: (self.op_jump_false, 2),
            7: (self.op_less_than, 3),
            8: (self.op_equals, 3)
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
        if type(move_pointer) == tuple:
            return move_pointer[0]
        else:
            new_index = index + move_pointer
            return new_index

    def process_intcode_list(self):
        # Executes an intcode program list and
        # returns the program final state
        index = 0 # Instruction pointer
        completed = False
        while completed is not True:
            index = self.instruction_parser(index)
            if not index:
                completed = True
                break

        return self.intcode_list


