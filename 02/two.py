#!/usr/bin/env python3

import logging
import sys
import pytest
import copy as c

#enable logging
#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
#logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s')

def main():
    test_program = readFile(sys.argv[1])[0]
    loop_program = []
    logging.debug(f"test_program: {test_program}")
    # this only didn't work because you didn't clean the memory
    # current solution does a lot of unecessary io, check and see if there's a
    # way to clear memory without invoking readFile 99*99 times
    # this may be faster
    for noun in range(0,100):
        for verb in range(0,100):
            # this seems to be a better solution 
            # see https://realpython.com/copying-python-objects/
            loop_program = c.deepcopy(test_program)
            result = processIntcode(loop_program, noun, verb)[0]
            if result == 3790645:
                print(f"result: {result}\nnoun: {noun} verb: {verb}\nans: {(100 * noun) + verb}")
            if result == 19690720:
                print(f"result: {result}\nnoun: {noun} verb: {verb}\nans: {(100 * noun) + verb}")
# reads input file and returns list(s) of ints
def readFile(path):
    programs = []

    results = []
    with open(path, 'r') as file:
        programs_string = file.readlines()
        logging.debug(programs_string)
        programs = programs_string
        logging.debug(programs)

    # remove errant newline chars
    programs = [line.rstrip('\n') for line in programs]

    # converts all lists to lists of ints
    for program in programs:
        logging.debug(f"program: {program}")

        #splits str into array of one char strings
        program = program.split(',')

        #casts each char as int
        program = [int(stringInt) for stringInt in program]
        logging.debug(f"split program: {program}")
        results.append(program)

    logging.info(type(results[0]))

    return results

# processes intcode with inputs        
# merci, https://stackabuse.com/overloading-functions-and-operators-in-python/
def processIntcode(program, noun=None, verb=None):
    #initialize as first char
    position = 0 
    logging.debug(f"program type: {type(program)}\n{program}")

    if noun is not None and verb is not None:
        program[1] = noun
        program[2] = verb
        while program[position] != 99:
            opcode = program[position]
            pos1 = program[position + 1]
            pos2 = program[position + 2]
            output = program[position + 3]
            
            logging.debug(f"position: {position}")
            logging.debug(f"opcode: {opcode}")
            logging.debug(f"pos1: {pos1}")
            logging.debug(f"pos2: {pos2}")
            logging.debug(f"outp: {output}")

            if opcode == 1:
                # add
                logging.debug("add")
                program[output] = program[pos1] + program[pos2]
                position = position + 4
            if opcode == 2:
                # multiply
                logging.debug("mult")
                program[output] = program[pos1] * program[pos2]
                position = position + 4

        return program

    while program[position] != 99:
        opcode = program[position]
        pos1 = program[position + 1]
        pos2 = program[position + 2]
        output = program[position + 3]
        
        logging.debug(f"position: {position}")
        logging.debug(f"opcode: {opcode}")
        logging.debug(f"pos1: {pos1}")
        logging.debug(f"pos2: {pos2}")
        logging.debug(f"outp: {output}")

        if opcode == 1:
            # add
            logging.debug("add")
            program[output] = program[pos1] + program[pos2]
            position = position + 4
        if opcode == 2:
            # multiply
            logging.debug("mult")
            program[output] = program[pos1] * program[pos2]
            position = position + 4

    return program


# see how hard it is to put test cases in another file
# tests intcode compiler
def testIntcode():
    programs = readFile('test-strings.txt')

    test_results = [processIntcode(program) for program in programs]

    assert test_results == [[2, 0, 0, 0, 99], [2, 3, 0, 6, 99], [2, 4, 4, 5, 99, 9801], [30, 1, 1, 4, 2, 5, 6, 0, 99]]

if __name__ == '__main__':
    main()
