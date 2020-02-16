# !/usr/bin/python
from solution_part1 import check_criteria

test_cases = {
    111111: True,
    223450: False,
    123789: False
}

def validate_number(value):
    if check_criteria(value):
        return True
    return False

def check_cases():
    for key, value in test_cases.items():
        assert value == validate_number(key)
    print('👍')

if __name__ == "__main__":
    check_cases()