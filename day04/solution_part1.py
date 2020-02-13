# !/usr/bin/python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')

def get_range():
    with open(puzzle_input_path) as f:
        range_string = f.readlines()[0]
    ranges = range_string.split('-')
    lower_bound = int(ranges[0])
    upper_bound = int(ranges[1])
    return lower_bound, upper_bound

def check_for_double(value:int):
    # Check for the existence of two adjacent digits
    number = str(value)
    previous_digit = number[0]
    for n in number[1:]:
        if n == previous_digit:
            return True
        else:
            previous_digit = n
    return False

def check_increasing_digits(number:int):
    digits = [int(x) for x in str(number)]
        # Check for the existence of two adjacent digits
    previous_digit = digits[0]
    for n in digits[1:]:
        if n < previous_digit:
            return False
        else:
            previous_digit = n
    return True

def get_passwords(lower_bound, upper_bound):
    password_list = []
    for number in range(lower_bound, upper_bound+1):
        if check_increasing_digits(number) and check_for_double(number):
            password_list.append(number)
    return password_list

if __name__ == "__main__":
    lower, upper = get_range()
    passwords = get_passwords(lower, upper)
    num_passwords = len(passwords)
    statement = 'There are {} passwords in the puzzle input that meet the critera.'
    print(statement.format(num_passwords))
