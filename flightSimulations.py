import csv
# import sys

'''
By Erik Ayavaca-Tirado
In this class there will be 4 functions that will do the following:
1. read in a file
2. hold the items from the file that will be used in a different function and also printout the queue at each time
3. Simulate an actual airport , so adding/removing planes based on request time. (this will be the priority queue)
4. print out the the queue
'''


# Holds all flight requests from the file
allFlights = []

# Going to be holding departed flights
departedFlights = []


def read_file(flightRequests):  # Function that will read in the file
    '''

    :param flightRequests:
    :return:

    '''
    allFlights = []  # Flight request are held in this

    with open(flightRequests, 'rt') as f:
        file = csv.reader(f)
        _ = next(file)  # removes cvs header

        for row in file:
            # Converts submission time, request start , and requested duration from strings into integers
            newRow = [row[0], int(row[1]), int(row[2]), int(row[3]), 0, 0]

            allFlights.append(newRow)
    return(allFlights)


# prints flights that are currently in the queue
def printQueue(queue, currentTime):
    '''

    :param queue:
    :param currentTime:
    :return:
    '''
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
    '''

    :param allFlights:
    :return:
    '''
    queue = []  # queue used for flight request
    currentTime = 0
    queueCount = 0

    # will continue running program if the queue count is less than number of flights or if the queue is not empty
    while queueCount < len(allFlights) or len(queue) >= 0:
        for i in range(len(allFlights)):
            if currentTime == allFlights[i][1]:
                queue.append(allFlights[i])
                queueCount += 1

    # sort queue based on requested departure time
        queue = sorted(queue, key=lambda x: x[2])

    # Still need a way to sort out the actual departure times. Done with this.

    # updating the start and end times for the flights in the queue
        for i in range(len(queue)):
            if i == 0:  # 1st flight of the queue
                if queue[i][5] == 0:  # if 1st flight actual start time is equal to 0
                    queue[i][4] = queue[i][2]  # first flight actual start equals to requested start
                    queue[i][5] = ((queue[i][4] + queue[i][3]) - 1)   # first flight actual end time is equal to current

            if i > 0:  # all other flights in queue
                if queue[i-1][5] > queue[i][2]:  # if previous flight end time,less than current flight requested start
                    queue[i][4] = queue[i-1][5]  # current flight actual Start time equal to previous flight end time
                    queue[i][5] = (queue[i][4] + queue[i][3])  # Current Flight actual endtime = current flight

                else:
                    queue[i][4] = queue[i][2]  # curent flight actual start time = current flight flight request time
                    queue[i][5] = (queue[i][4] + queue[i][3])  # current flight actual time = current flight

    # remove flights that have already departed from the queue
        if len(queue) > 0:
            if queue[0][5] <= currentTime:
                departedFlights.append(queue[0])
                del queue[0]

        printQueue(queue, currentTime)

    # break out of the loop after flights have been queued and departed
        if len(queue) == 0 and queueCount >= len(allFlights):
            break

        currentTime += 1


def takeOffPrint(departedFlights):
    '''

    :param departedFlights:
    :return:
    '''

    print("\n=======================================================")
    print("Take off times: ")
    for i in range(len(departedFlights)):
        print(str(departedFlights[i][0]) + " (" + str(departedFlights[i][4]) + "-" + str(departedFlights[i][5]) + ")" )

# Testing purposes ignore below
 # if __name__ == "__main__":
     #__test__main__()
    # Flights = read_file('test.csv')
    # simulate_airport(Flights)
    # takeOffPrint(departedFlights)

