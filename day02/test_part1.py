# !/usr/bin/python
from solution_part1 import (intcode_to_list,
                            process_intcode_list,
                            intcode_to_list)

test_cases = {
    "1,0,0,0,99" : "2,0,0,0,99",
    "2,3,0,3,99" : "2,3,0,6,99",
    "2,4,4,5,99,0" : "2,4,4,5,99,9801",
    "1,1,1,4,99,5,6,0,99" : "30,1,1,4,2,5,6,0,99"
}

def check_cases():
    for i, items in enumerate(test_cases.items()):
        print('Testing Case {}'.format(i))
        key, value = items
        input_list = intcode_to_list(key)
        final_state = process_intcode_list(input_list)
        print(final_state)
        test_state = intcode_to_list(value)
        assert final_state == test_state
        print('===================')
    print('👍')

if __name__ == "__main__":
    check_cases()