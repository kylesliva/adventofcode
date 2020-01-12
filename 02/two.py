#!/usr/bin/env python3

import logging
import sys
import pytest

#enable logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
#logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s')

def main():
    programs = readFile(sys.argv[1])
    logging.debug(programs)
    print(runCode(programs))



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
    if path == "input.txt":
        logging.info("main input detected")
        logging.debug(results[0])
        results[0] = changeVerbs(12, 2, results[0])

    return results

def changeVerbs(noun, verb, program):
    program[1] = noun
    program[2] = verb 

    return program

# runs intcode machine until desired result is found
def findOutput(noun, verb, program):
    program[1] = noun
    program[2] = verb 

    return (noun, verb)
    
# goes through all program strings
def runCode(programs):
    outputs = []
    for program in programs:
        processIntcode(program)
        outputs.append(program)

    return outputs

# processes intcode        
def processIntcode(program):
    #initialize as first char
    position = 0 

    print("processing intcode...")
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

    logging.debug("processing complete")
    return program
    
# see how hard it is to put test cases in another file
# tests intcode compiler
def testIntcode():
    programs = readFile('test-strings.txt')

    assert runCode(programs) == [[2, 0, 0, 0, 99], [2, 3, 0, 6, 99], [2, 4, 4, 5, 99, 9801], [30, 1, 1, 4, 2, 5, 6, 0, 99]]

if __name__ == '__main__':
    main()
