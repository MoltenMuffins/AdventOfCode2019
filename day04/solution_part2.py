# !/usr/bin/python
from solution_part1 import get_range

def check_increasing_digits(number:int):
    digits = [int(x) for x in str(number)]
    previous_digit = digits[0]
    for n in digits[1:]:
        # Check if digits are equal or increasing
        if n < previous_digit:
            return False
        else:
            previous_digit = n
    return True

def check_for_pair(number:int):
    consec_list = [1]
    digits = [int(x) for x in str(number)]
    previous_digit = digits[0] 
    for n in digits[1:]:
        if n == previous_digit:
            consec_list[-1] += 1
        else:
            consec_list.append(1)
        previous_digit = n
    if 2 in consec_list:
        return True
    else:
        return False

def get_passwords(lower_bound, upper_bound):
    password_list = []
    for number in range(lower_bound, upper_bound+1):
        if check_increasing_digits(number) and check_for_pair(number):
            password_list.append(number)
    return password_list

if __name__ == "__main__":
    lower, upper = get_range()
    passwords = get_passwords(lower, upper)
    num_passwords = len(passwords)
    statement = 'There are {} passwords in the puzzle input that meet the critera.'
    print(statement.format(num_passwords))
