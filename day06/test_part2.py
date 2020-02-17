# !/usr/bin/python
from solution_part1 import generate_orbit_map
from solution_part2 import get_num_transfers

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
    'K)L',
    'K)YOU',
    'I)SAN'
]

test_cases = {
    4: orbit_map
}

def check_cases(cases:dict):
    for key, value in cases.items():
        graph, _ = generate_orbit_map(value)
        num_transfers = get_num_transfers(graph)
        print(num_transfers)
        assert num_transfers == key
    print('👍')

if __name__ == "__main__":
    check_cases(test_cases)
