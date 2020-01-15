# !/usr/bin/python
from solution_part1 import get_fuel_required

def check_cases(cases:dict):
    for key, value in cases.items():
        assert get_fuel_required(key) == value
    print('👍')

test_cases = {
    12: 2,
    14: 2,
    1969: 654,
    100756: 33583
}

if __name__ == "__main__":
    check_cases(test_cases)
