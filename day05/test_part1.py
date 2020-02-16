# !/usr/bin/python
from solution_part1 import (intcode_to_list,
                            process_intcode_list)

test_cases = {
    "1002,4,3,4,33" : "1002,4,3,4,99",
    "1101,100,-1,4,0" : "1101,100,-1,4,99"
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
