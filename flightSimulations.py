'''
By Erik Ayavaca-Tirado
'''

import csv

# Holds all flight requests from the file
allFlights = []

# Going to be holding departed flights
departedFlights = []


def read_file(flightRequests):  # Function that will read in the file
    allFlights = []  # Flight request are held in this

    with open(flightRequests, 'rb') as f:
        file = csv.reader(f)
        _ = next(file)  # removes cvs header

        for row in file:
            # Converts submission time, request start , and requested duration from strings into integers
            newRow = [row[0], int(row[1]), int(row[2]), int(row[3]), 0, 0]

            allFlights.append(newRow)
    return(allFlights)


# prints flights that are currently in the queue
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


# This function is going to be removing and adding flights from the queue. Basically like how the airport functions
def simulate_airport(allFlights):
    queue = []  # queue used for flight request
    currentTime = 0
    queueCount = 0

    # will continue running program if the queue count is less than number of flights or if the queue is not empty
    for i in range(len(allFlights)):
        if currentTime == allFlights[i][1]:
            queue.append(allFlights[i])
            queueCount += 1

    # sort queue based on requested departured time
    queue = sorted(queue, key=lambda x: x[2])

    # Still need a way to sort out the actual departure times

    # remove flights that have already departed from the queue
    if len(queue) > 0:
        if queue[0][5] <= currentTime:
            departedFlights.append(queue[0])
            del queue[0]

    printQueue(queue, currentTime)



if __name__ == "__main__":
    __test__main__()

