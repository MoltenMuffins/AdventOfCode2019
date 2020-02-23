# !/usr/bin/python
from intcode_computer_pt1 import IntcodeComputer, intcode_to_list

test_cases = {
    "1002,4,3,4,33" : "1002,4,3,4,99",
    "1101,100,-1,4,0" : "1101,100,-1,4,99"
}

def check_cases():
    for i, (key, value) in enumerate(test_cases.items()):
        print('Testing Case {}'.format(i))
        # Instantiate intcode computer
        computer = IntcodeComputer(key)
        # Run intcode computer
        computer.compute()
        print(computer.final_state)

        # Convert the expected output into a list so
        # that we can compare it to our intcode
        # computer's output
        test_state = intcode_to_list(value)
        assert computer.final_state == test_state
        print('===================')
    print('👍')

if __name__ == "__main__":
    check_cases()
