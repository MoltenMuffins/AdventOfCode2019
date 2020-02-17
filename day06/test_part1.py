# !/usr/bin/python
from solution_part1 import (generate_orbit_map,
                            run_count_checksum)

orbit_map = [
    'COM)B',
    'B)C',
    'C)D',
    'D)E',
    'E)F',
    'B)G',
    'G)H',
    'D)I',
    'E)J',
    'J)K',
    'K)L'
]

test_cases = {
    42: orbit_map
}

def check_cases(cases:dict):
    for key, value in cases.items():
        orbits = generate_orbit_map(value)
        checksum = run_count_checksum(orbits)
        assert checksum == key
    print('👍')

if __name__ == "__main__":
    check_cases(test_cases)

    
