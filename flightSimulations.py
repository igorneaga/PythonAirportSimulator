'''
By Erik Ayavaca-Tirado
'''

import csv

# Holds all flight requests from the file
allFlights = []

# Going to be holding departed flights
departedFlights = []


def read_file(flightRequests):
    allFlights = []

    with open(flightRequests, 'rb') as f:
        file = csv.reader(f)
        _ = next(file)

        for row in file:
            newRow = [row[0], int(row[1]), int(row[2]), int(row[3]), 0, 0]
            allFlights.append(newRow)
    return(allFlights)

def printQueue(queue, currentTime):
    if len(queue) > 0:

print("\n=======================================================")
    print("The queue at Time: " + str(currentTime))
    if (currentTime >= queue[0][2]):

