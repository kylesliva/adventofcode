#!/usr/bin/env python3

import sys
import logging
import pprint as p
import pytest

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

'''
todo
* add in exception handling
* more testing

'''


def main():
    print("reading masses file")
    # read input
    masses = readMass(sys.argv[1])
    # computed fuel, filled in below
    fuel = []

    for mass in masses:
        fuel.append(computeFuel(mass))
    logging.debug(f"fuel: {p.pformat(fuel)}")

    totalFuel = sum(fuel)

    print(f"total fuel required: {totalFuel}")

# reads masses to a list
def readMass(path):
    masses = []
    with open(path, 'r') as file:
        masses = file.readlines()
    logging.debug(f"**** MASSES ****\n{p.pformat(masses)}")

    return masses

# never used
def testReadMass():
    pass

def computeFuel(mass):
    mass = mass / 3
    mass = int(mass)
    mass = mass - 2
    logging.debug(f"fuel: {mass}")

    # does it until mass is zero or less
    if mass <= 0:
        return 0
    return mass + computeFuel(mass) 

def testNegativeFuel():
    testMasses = [14, 1969, 100756]
    results = []

    for mass in testMasses:
        logging.debug(f"MASS: {mass}")
        logging.debug(f"COMPUTED MASS: {computeFuel(mass)}")
        results.append(computeFuel(mass))
    logging.debug(results)

    assert results == [2, 966, 50346]

if __name__ == '__main__':
    main()
