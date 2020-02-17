# !/usr/bin/python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
puzzle_input_path = os.path.join(dir_path, 'puzzle_input.txt')

# try not to cheat, but we can represent the orbits via a dict

def edge_parser(edge_str:str):
    edge_str = edge_str.strip('\n')
    node, neighbour = edge_str.split(')')
    return node, neighbour

def generate_orbit_map(edge_list):
    orbit_graph = {'COM':[]}
    entity_list = []

    for edge in edge_list:
        body, satellite = edge_parser(edge)
        entity_list.append(satellite)
        if body in orbit_graph:
            orbit_graph[body].append(satellite)
        else:
            orbit_graph[body] = [satellite]

    # Remove repeated entries in `entity_list` by
    # converting it to a set
    entity_set = set(entity_list)
    return orbit_graph, entity_set

def traverse_graph(entity:str, orbit_graph:dict):
    # Traverses the graph for a particular entity
    # in reverse until 'COM' is reached
    orbit_count = 0

    # This shouldn't happen but we check in case
    if entity == 'COM':
        return orbit_count

    # Start from a dictionary value and count the
    # number of reverse traversals
    satellite = entity
    complete = False
    while not complete:
        for key, value in orbit_graph.items():
            if satellite in value:
                orbit_count += 1
                if key == 'COM':
                    complete = True
                    break
                satellite = key
    return orbit_count


def run_count_checksum(orbits:tuple):
    graph, orbital_bodies = orbits
    orbit_count = 0
    for entity in orbital_bodies:
        orbit_count += traverse_graph(entity, graph)
    return orbit_count

if __name__ == "__main__":

    with open(puzzle_input_path) as universal_orbit_map:
        orbits = generate_orbit_map(universal_orbit_map)
        checksum_value = run_count_checksum(orbits)
        statement = ('The total number of direct and indirect'
                     ' orbits: {}')
        print(statement.format(checksum_value))