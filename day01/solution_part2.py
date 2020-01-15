# !/usr/bin/python
from solution_part1 import get_fuel_required, puzzle_input_path

def fuel_for_fuel(fuel_required:int):
    total_additional_fuel = 0
    current_fuel = fuel_required
    while current_fuel > 0:
        current_fuel = get_fuel_required(current_fuel)
        if current_fuel <= 0:
            break
        total_additional_fuel += current_fuel
    return total_additional_fuel

if __name__ == "__main__":
    total_fuel_requirement = 0
    with open(puzzle_input_path) as modules:
        for module in modules:
            mass = int(module)
            fuel_required = get_fuel_required(mass)
            additional_fuel = fuel_for_fuel(fuel_required)
            total_fuel_requirement += (fuel_required + additional_fuel)
    
    print('Total Fuel Required is {}'.format(total_fuel_requirement))