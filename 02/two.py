#!/usr/bin/env python3

import logging
import sys
import pytest

#enable logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

def main():
    programs = readFile(sys.argv[1])
    logging.debug(programs)
    runCode(programs)

# reads input file and returns string(s) of programs
def readFile(path):
    program = []
    with open(path, 'r') as file:
        program_string = file.readlines()
        logging.debug(program_string)
        program = program_string
        logging.debug(program)

    # remove errant newline chars
    program = [line.rstrip('\n') for line in program]
        
    return program

# goes through all program strings
def runCode(programs):
    num = -1
    index = 0
    for program in programs:
        logging.debug(f"program: {program}")
        program = program.split(',')
        logging.debug(f"split program: {program}")
        # need to enumerate
        for i, code in enumerate(program):
            logging.debug(f"i: {i}, code: {code}")

# processes intcode        
def processIntcode(program):
    try:
        if program[0] == 1:
            # add
            pass
        if program[0] == 2:
            # multiply
            pass
        if program[0] == 99:
            # end 
            pass
    except Exception as e:
        print("error: program must be a list of ints")

if __name__ == '__main__':
    main()
