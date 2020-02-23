# !/usr/bin/python
from intcode_computer import IntcodeComputer, intcode_to_list

test_cases = {
    "1,0,0,0,99" : "2,0,0,0,99",
    "2,3,0,3,99" : "2,3,0,6,99",
    "2,4,4,5,99,0" : "2,4,4,5,99,9801",
    "1,1,1,4,99,5,6,0,99" : "30,1,1,4,2,5,6,0,99"
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