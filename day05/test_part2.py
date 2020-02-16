# !/usr/bin/python
from solution_part2 import (intcode_to_list,
                            process_intcode_list)

test_cases = {
    "3,9,8,9,10,9,4,9,99,-1,8" : 'Check if input is equal to 8; output 1 (if it is) or 0 (if it is not)',
    "3,9,7,9,10,9,4,9,99,-1,8" : 'Check if input is less than 8; output 1 (if it is) or 0 (if it is not)',
    "3,3,1108,-1,8,3,4,3,99" : 'Check if input is equal to 8; output 1 (if it is) or 0 (if it is not)',
    "3,3,1107,-1,8,3,4,3,99" : 'Check if input is less than 8; output 1 (if it is) or 0 (if it is not)',
    "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9" : 'Output 0 if the input is zero or 1 if the input is non-zero',
    "3,3,1105,-1,9,1101,0,0,12,4,12,99,1" : 'Output 0 if the input is zero or 1 if the input is non-zero',
    "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99" : 'Output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8'
}

def check_cases():
    print('As the input opcode requires user input via `input()`, this unit test we requires user input')
    print('\n')
    for i, items in enumerate(test_cases.items()):
        print('Testing Case {}'.format(i))
        key, value = items
        print(value)
        input_list = intcode_to_list(key)
        final_state = process_intcode_list(input_list)
        print('===================')
    print('👍')

if __name__ == "__main__":
    check_cases()
