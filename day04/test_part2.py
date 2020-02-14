# !/usr/bin/python
from solution_part2 import check_increasing_digits, check_for_pair

test_cases = {
    112233: True,
    123444: False,
    111122: True
}

def validate_number(value):
    if check_increasing_digits(value) and check_for_pair(value):
        return True
    return False

def check_cases():
    for key, value in test_cases.items():
        assert value == validate_number(key)
    print('👍')

if __name__ == "__main__":
    check_cases()