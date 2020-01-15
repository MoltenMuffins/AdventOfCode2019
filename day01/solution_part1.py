# !/usr/bin/python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')

def get_fuel_required(mass:int):
    # Fuel required to launch a given mass
    return (mass//3)-2

if __name__ == "__main__":
    total_fuel_requirement = 0
    with open(puzzle_input_path) as modules:
        for module in modules:
            mass = int(module)
            fuel_required = get_fuel_required(mass)
            total_fuel_requirement += fuel_required
    
    print('Total Fuel Required is {}'.format(total_fuel_requirement))