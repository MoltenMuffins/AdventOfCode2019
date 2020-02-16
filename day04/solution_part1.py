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

def check_criteria(number:int):
    double_digit = False

    digits = [int(x) for x in str(number)]
    previous_digit = digits[0]
    for n in digits[1:]:
        # Check if digits are equal or increasing
        if n < previous_digit:
            return False
        # Check for the existence of double digits
        elif n == previous_digit:
            double_digit = True
        previous_digit = n
    return double_digit

def get_passwords(lower_bound, upper_bound):
    password_list = []
    for number in range(lower_bound, upper_bound+1):
        if check_criteria(number):
            password_list.append(number)
    return password_list

if __name__ == "__main__":
    lower, upper = get_range()
    passwords = get_passwords(lower, upper)
    num_passwords = len(passwords)
    statement = 'There are {} passwords in the puzzle input that meet the critera.'
    print(statement.format(num_passwords))
