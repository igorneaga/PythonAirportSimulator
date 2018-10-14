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
        print("Currently Departing: " + str(queue[0][0]) + " (started at " + str(queue[0][4]) + ")")
        print("Waiting: ")
        for i in range(1, len(queue)):
            print(str(queue[i][0]) + " (Scheduled for " + str(queue[i][4]) + ")")

        else:
        print("Currently Departing: No flights are curentlt departing ")
        print("Waiting: ")
        for i in range(1, len(queue)):
            print(str(queue[i][0]) + " (Scheduled for " + str(queue[i][4]) + ")")

    else:
        print("\n=======================================================")
        print("The queue at Time: " + str(currentTime))
        print("Currently Departing: No flights are curentlt departing ")
        print("Waiting: ")




