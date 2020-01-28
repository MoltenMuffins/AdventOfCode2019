# !/usr/bin/python
from solution_part1 import (puzzle_input_path,
                            intcode_to_list,
                            process_intcode_list,
                            intcode_to_list)

def init_program(noun, verb, program):
    program_cpy = program.copy()
    program_cpy[1] = noun
    program_cpy[2] = verb
    return program_cpy

def brute_force(program, output):
    for noun in range(100):
        for verb in range(100):
            # Replace values at addresses 1 and 2 as per
            # puzzle instructions
            cur_program = init_program(noun, verb, program)
            # We then run the program for the current
            # noun, verb pair
            try:
                final_state = process_intcode_list(cur_program)
                if final_state[0] == output:
                    print('{}, {} produces the desired output {}'.format(noun,verb,desired_output))
                    return noun, verb          
            except IndexError:
                continue
    print('Unable to find a suitable noun, verb pair.')
    return False

if __name__ == "__main__":
    # Read and preprocess the raw textfile
    with open(puzzle_input_path) as f:
        intcode_program_list = f.readlines()

    program = intcode_program_list[0]
    intcode_list = intcode_to_list(program)
    
    # Iterate through possible values of nouns and verbs
    # until we obtain the pair that produces the output we want
    desired_output = 19690720
    noun, verb = brute_force(intcode_list, desired_output)

    # Run the winning pair through the checksum
    answer = (100 * noun) + verb
    print('The answer for part two of the puzzle is {}'.format(answer))



    