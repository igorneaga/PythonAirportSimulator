'''
By Erik Ayavaca-Tirado
This is the main were the call to the functions in the flightsSimulations class will be made to

'''

import sys
import flightSimulations


if __name__ == "__main__":
    flights = flightSimulations.read_file(sys.argv[1])
    flightSimulations.simulate_airport(flights)
    flightSimulations.takeOffPrint(flights)

