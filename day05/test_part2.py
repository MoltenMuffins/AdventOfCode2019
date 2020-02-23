# !/usr/bin/python
from intcode_computer_pt2 import IntcodeComputer

test_cases = {
    # Check if input is equal to 8; output 1 (if it is) or 0 (if it is not)
    1: ("3,9,8,9,10,9,4,9,99,-1,8", 8, 1),
    2: ("3,9,8,9,10,9,4,9,99,-1,8", 100, 0),
    # Check if input is less than 8; output 1 (if it is) or 0 (if it is not)
    3: ("3,9,7,9,10,9,4,9,99,-1,8", 7, 1),
    4: ("3,9,7,9,10,9,4,9,99,-1,8", 10, 0),
    # Check if input is equal to 8; output 1 (if it is) or 0 (if it is not)
    5: ("3,3,1108,-1,8,3,4,3,99", 8, 1),
    6: ("3,3,1108,-1,8,3,4,3,99", 7, 0),
    # Check if input is less than 8; output 1 (if it is) or 0 (if it is not)
    7: ("3,3,1107,-1,8,3,4,3,99", 7, 1),
    8: ("3,3,1107,-1,8,3,4,3,99", 9, 0), 
    # Output 0 if the input is zero or 1 if the input is non-zero
    9: ("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", 0, 0),
    10: ("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", 100, 1),
    # Output 0 if the input is zero or 1 if the input is non-zero
    11: ("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", 0, 0), 
    12: ("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", 12, 1),
    # Output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8
    13: ("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", 7, 999),
    14: ("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", 8, 1000),
    15: ("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", 9, 1001)
}

def check_cases():
    for i, (_, values) in enumerate(test_cases.items()):
        print('Testing Case {}'.format(i))
        program, input_value, expected_output = values
        # Instantiate intcode computer
        computer = IntcodeComputer(program)

        # Run intcode computer with given input
        computer.compute(input_value)
        print(computer.final_state)
        assert computer.output_value == expected_output
        print('===================')
    print('👍')

if __name__ == "__main__":
    check_cases()
