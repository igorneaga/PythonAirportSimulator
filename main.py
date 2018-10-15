'''
By Erik Ayavaca-Tirado
'''

import sys
import flightSimulations


def __test__main__():
    flights = flightSimulations.read_file(sys.argv[1])
    print(flights)

