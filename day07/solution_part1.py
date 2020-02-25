# !/usr/bin/python
import os
import sys
import itertools
sys.path.append('')
from day05.intcode_computer_pt2 import IntcodeComputer

dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')

class Amplifier():
    def __init__(self, intcode_str):
        self.amp_control_soft = IntcodeComputer(intcode_str)
    
    def run(self, phase_setting, input_signal):
        input_values = [phase_setting, input_signal]
        self.amp_control_soft.compute(input_values)
        return self.amp_control_soft.output_value

def get_permutations():
    phases = [x for x in range(5)]
    return itertools.permutations(phases)

if __name__ == "__main__":
    with open(puzzle_input_path) as f:
        intcode_program = f.readlines()[0]

    amp = Amplifier(intcode_program)

    result_list = []
    for permutation in get_permutations():
        # Instantiate input signal
        signal = 0
        for setting in permutation:
            signal = amp.run(setting, signal)
        result_list.append(signal)
    
    statement = 'The highest signal that can be sent to the thrusters is {}'
    print(statement.format(max(result_list)))