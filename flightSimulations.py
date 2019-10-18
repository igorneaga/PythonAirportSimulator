import csv

'''
By Erik Ayavaca-Tirado
In this class there will be 4 functions that will do the following:
1. read in a file
2. hold the items from the file that will be used in a different function and also printout the queue at each time
3. Simulate an actual airport , so adding/removing planes based on request time. (this will be the priority queue)
4. print out the the queue

This is a python project I will be creating a program that will emulate an airport runway.
'''


class FlightSimulation:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.all_flight = list
        self.departed_flight = list

        self.main_logic()

    def main_logic(self):

        def read_file(flightRequests):  # Function that will read in the file
            '''
            This function will take in the file that is read in from the command prompt. This variable name is flightRequests.
            It will put the file data in to list named allFlights and then returns it ,so it may be used for the other functions
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
            return allFlights

        def printQueue(queue, currentTime):
            '''
            This function is printing out the flights that are currently in the queue as well as the time they were on the
            runway until they depart from the runway.
            :param queue: Keeps tracks of the flights
            :param currentTime: Keeps track of the time.
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
                    print("Currently Departing: No flights are currently departing ")
                    print("Waiting: ")
                for i in range(1, len(queue)):
                    print(str(queue[i][0]) + " (Scheduled for " + str(queue[i][4]) + ")")

            else:
                print("\n=======================================================")
                print("The queue at Time: " + str(currentTime))
                print("Currently Departing: No flights are currently departing ")
                print("Waiting: ")

        def simulate_airport(allFlights):
            '''
            This function is going to be removing and adding flights from the queue. Basically like how the airport functions.
            This functions is basically the priority queue.
            :param allFlights:
            :return:
            '''
            queue = []  # queue used for flight request
            departedFlights = []
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

                # updating the start and end times for the flights in the queue
                for i in range(len(queue)):
                    if i == 0:  # 1st flight of the queue
                        if queue[i][5] == 0:  # if 1st flight actual start time is equal to 0
                            queue[i][4] = queue[i][2]  # first flight actual start equals to requested start
                            queue[i][5] = ((queue[i][4] + queue[i][
                                3]) - 1)  # first flight actual end time is equal to current

                    if i > 0:  # all other flights in queue
                        if queue[i - 1][5] > queue[i][
                            2]:  # if previous flight end time,less than current flight requested start
                            queue[i][4] = queue[i - 1][
                                5]  # current flight actual Start time equal to previous flight end time
                            queue[i][5] = (queue[i][4] + queue[i][3])  # Current Flight actual endtime = current flight

                        else:
                            queue[i][4] = queue[i][
                                2]  # current flight actual start time = current flight flight request time
                            queue[i][5] = (queue[i][4] + queue[i][3])  # current flight actual time = current flight

                # remove flights that have already departed from the queue
                if len(queue) > 0:
                    if queue[0][5] <= currentTime:
                        departedFlights.append(queue[0])
                        del queue[0]

                printQueue(queue, currentTime)

                # break out of the loop after flights have been queued and departed
                if len(queue) == 0 and queueCount >= len(allFlights):
                    print("All flights have departed")
                    break

                currentTime += 1
            return departedFlights

        def takeOffPrint(departedFlights):
            '''
            In this function we are taking in the list of updated departed flights that were updated in the airport simulations
            function.
            :param departedFlights:
            :return:
            '''

            print("\n=======================================================")
            print("Actual take off times: ")
            for i in range(len(departedFlights)):
                print(str(departedFlights[i][0]) + " (" + str(departedFlights[i][4]) + "-" + str(
                    departedFlights[i][5]) + ")")

        self.all_flight = read_file(self.csv_file)
        self.departed_flight = simulate_airport(self.all_flight)
        takeOffPrint(self.all_flight)



