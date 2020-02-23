# !/usr/bin/python
from solution_part1 import puzzle_input_path
from intcode_computer import IntcodeComputer

def brute_force(program:str, output:int):
    for noun in range(100):
        for verb in range(100):
            # Instantiate intcode computer
            computer = IntcodeComputer(program)
            # Replace values at addresses 1 and 2 as per
            # puzzle instructions
            computer.edit_input(1, noun)
            computer.edit_input(2, verb)
            # We then run the program for the current
            # noun, verb pair
            try:
                computer.compute()
                if computer.final_state[0] == output:
                    print('{}, {} produces the desired output {}'.format(noun, verb, desired_output))
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
    
    # Iterate through possible values of nouns and verbs
    # until we obtain the pair that produces the output we want
    desired_output = 19690720
    noun, verb = brute_force(program, desired_output)

    # Run the winning pair through the checksum
    answer = (100 * noun) + verb
    print('The answer for part two of the puzzle is {}'.format(answer))



    