# !/usr/bin/python
from solution_part1 import get_fuel_required
from solution_part2 import fuel_for_fuel

def check_cases(cases:dict):
    for key, value in cases.items():
        #subtract fuel required for module
        adj_key = get_fuel_required(key)
        assert (fuel_for_fuel(adj_key) + adj_key) == value
    print('👍')

test_cases = {
    14: 2,
    1969: 966,
    100756: 50346
}

if __name__ == "__main__":
    check_cases(test_cases)