'''
By Erik Ayavaca-Tirado

'''

import sys
import flightSimulations


if __name__ == "__main__":
    flights = flightSimulations.read_file(sys.argv[1])
    flightSimulations.simulate_airport(flights)
    flightSimulations.takeOffPrint(flights)

