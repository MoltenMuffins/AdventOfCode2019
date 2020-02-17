# !/usr/bin/python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')

from solution_part1 import generate_orbit_map

# We modify traverse_graph to output a list of 
# related orbits instead of the number of orbits
def traverse_graph(entity:str, orbit_graph:dict):
    # Find the entity as a dictionary value and count the
    # number of reverse traversals until find a value
    # where "COM" is a key
    orbit_list = []
    satellite = entity
    complete = False
    while not complete:
        for key, value in orbit_graph.items():
            if satellite in value:
                orbit_list.append(satellite)
                if key == 'COM':
                    complete = True
                    break
                satellite = key
    return orbit_list

def get_num_transfers(orbit_graph:dict):
    # Convert lists to sets so we can use the symetric-difference
    # method
    santa_orbits = set(traverse_graph('SAN', orbit_graph))
    self_orbits = set(traverse_graph('YOU', orbit_graph))

    # The symmetric difference of the two sets gives us the path
    # between 'YOU' and 'SAN'
    sym_diff = santa_orbits.symmetric_difference(self_orbits)

    # Subtract 2 from the result to account for 'YOU' and 'SAN'
    # initial orbits
    return len(sym_diff) - 2 

if __name__ == "__main__":

    with open(puzzle_input_path) as universal_orbit_map:
        graph, _ = generate_orbit_map(universal_orbit_map)
        num_transfers = get_num_transfers(graph)
        statement = '{} orbital transfers are required'
        print(statement.format(num_transfers))