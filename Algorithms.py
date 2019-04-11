#
# def findWaitingTime(planeList, n):
#     waitingTimes = [0] * n
#
#     for i in range(1, n):
#         waitingTimes[i] = planeList[i - 1].turnAround + waitingTimes[i - 1]
#     return waitingTimes

#------------------------------------------------------------------------------#
#                         WAIT TIME AND TURN AROUND:                           #
#------------------------------------------------------------------------------#

def findWaitingTime(planeList, n):
    planeList[0].waitTime = 0.0
    for i in range(1, n):
        planeList[i].waitTime = planeList[i - 1].turnAround + planeList[i - 1].waitTime
    return planeList

#
def findTurnAroundtime(planeList, n):
    turnAroundTimes = [0] * n
    for i in range(n):
        turnAroundTimes[i] = planeList[i].turnAround + planeList[i].waitTime
    return turnAroundTimes

#------------------------------------------------------------------------------#
#                         PRINT TABLE FORMATTING:                              #
#------------------------------------------------------------------------------#

# Table Formatting
def printResults(planeList, n):

    # waitingTimes = findWaitingTime(planeList, n)
    turnAroundTimes = findTurnAroundtime(planeList, n)
    #Table heading formatting
    headings = ["Planes", "Arrival (T)", "Fueling (T)", "Passenger I/O (T)", "Burst (T)", "Wait (T)", "Turn Around (T)", "Priority"]
    for h in headings:
        print("{0:<20}".format(h), end="")
    print("")

    totalWaitTime = 0
    totalTurnAroundTime = 0

    for i in range(n):
        totalWaitTime += planeList[i].waitTime
        totalTurnAroundTime += turnAroundTimes[i]
        #Table data formatting
        print("{0:20}{1:<20.3f}{2:<20.3f}{3:<20.3f}{4:<20.3f}{5:<20.3f}{6:<20.3f}{7:<20.3f}".format(
        planeList[i].id, planeList[i].arrival, (planeList[i].capacity - planeList[i].fuel),
        (planeList[i].passengers * 2 ), planeList[i].turnAround,
        planeList[i].waitTime, turnAroundTimes[i], planeList[i].priority))
    print("\nAverage waiting time = {0:.3f}".format(totalWaitTime / n))
    print("Average turn around time = {0:.3f} \n\n".format(totalTurnAroundTime / n))

# Printing the list of planes
def printScheduleOrder(planeList, scheduleType):
    print(planeList)
    print("Ordered via {0}: ".format(scheduleType))
    for plane in planeList:
        print(plane.info())
        # print("{0}: ".format(plane.id), end=" ")
    print("\n")


#------------------------------------------------------------------------------#
#                        SCHEDULING ALGORITHMS                                 #
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#                             COMPLETED:                                       #
#------------------------------------------------------------------------------#

# Scheduling Algorithms
def priorityScheduling(planeList):
    planeList = sorted(planeList, key = lambda planeList:planeList.priority,
                                                                reverse = True)
    findWaitingTime(planeList, len(planeList))
    return planeList

#shortcut to print
def firstComeFirstServeScheduling(planeList, n):
    planeList = findWaitingTime(planeList, len(planeList))
    printScheduleOrder(planeList, "FCFS")
    printResults(planeList, n)

#
def shortestJobFirstNp(planeList):
    planeList = sorted(planeList, key = lambda planeList:planeList.turnAround,
                                                                reverse = False)
    planeList = findWaitingTime(planeList, len(planeList))
    return planeList

#------------------------------------------------------------------------------#
#                             IN PROGRESS:                                     #
#------------------------------------------------------------------------------#

# Highest Response Ratio Next (HRRN)
# Non-preemptive
# Finds response ratio of all processes and selects one with the highest response ratio.
# Once selected, the process runs until completion
# Builds on SJN to mitigate starvation
# Jobs that have spent a long time waiting compete against those with short estimated run times
#
# Response Ratio:
# waiting time + estimated run time (burst time) / estimated run time (burst time) =
#   1 + waiting time / estimated run time (burst time)
#
# Performance:
# Shorter processes are favoured
# Aging without service increases ratio. Longer jobs can get past shorter jobs

# Highest Response Ration Next
# def highestResponseRatioNext(planeList):
#     waitingTimes = findWaitingTime(planeList, len(planeList), waitingTimes)
#
#     planeList = sorted(planeList, key lambda planeList:planeList.)

# Highest Response Ratio Next
def highestResponseRatioNext(planeList):
    # Step 1: Calculate clock time (firstProcess.turnAround + fP.arrival)
    # 2: Sort planes by arrival time
    # 3: pop.() the first process into the completed list (hrrnPlaneList)
    # 4: Now the fun part 
    # 5: The following processes continue until planeList is empty
    # 6: Loop through the planes calculating their wait time and adding them to the arrivedPlanes list 
    # 7: Sort arrived planes by HRRN with the largest value first 
    # 8: pop.() the first value into the hrrnPlaneList and repeat 
    hrrnPlaneList = []
    planeList = sorted(planeList, key = lambda planeList:planeList.arrival, 
                                                                reverse = False)
    
    clock = planeList[0].turnAround + planeList[0].arrival
    hrrnPlaneList.append(planeList.pop(0))
    
    arrivedPlanes = []
    while len(planeList) > 0:
        # Loop through plane list
        for i in range(len(planeList)):
            # print(len(planeList))
            # adding all planes that have arrived to arrival list 
            if planeList[i].arrival <= clock:
                planeList[i].waitTime = clock - planeList[i].arrival
                arrivedPlanes.append(planeList[i])
            # adding next process if gap occurs
            elif i == 0:
                clock = planeList[i].arrival + planeList[i].turnAround
                arrivedPlanes.append(planeList[i])
                break
            else: 
                break
        # Remove arrive planes from list
        del planeList[:i+1]
        # sort arrived planes by response ratio
        arrivedPlanes = sorted(arrivedPlanes, key = lambda arrivedPlanes: (
            (arrivedPlanes.waitTime + arrivedPlanes.turnAround) / 
            arrivedPlanes.turnAround), 
            reverse = True)
        # increment via previous process time
        clock += arrivedPlanes[0].turnAround
        # take value with hrr and add to hrrnPlaneList
        hrrnPlaneList.append(arrivedPlanes.pop(0))

    
    # arrivedPlanes = findWaitingTime(arrivedPlanes, len(arrivedPlanes)) # I know this line is wrong
    hrrnPlaneList.append(arrivedPlanes)
    print(len(hrrnPlaneList))
    
    return hrrnPlaneList
    
    

def highestResponseRatioNext2(planeList):
    planeList = findWaitingTime(planeList, len(planeList))
    planeList = sorted(planeList, key = lambda planeList:(
        planeList.waitTime + planeList.turnAround / planeList.turnAround),
                                                                reverse = False)
    return planeList

#------------------------------------------------------------------------------#
#                                TODO:                                         #
#------------------------------------------------------------------------------#

# Round Robin
def roundRobin(planeList):
    pass

# Shortest Remaining time
def shortestRemainingTime(planeList):
    pass

# Multilevel Feedback Queue Scheduling
def multilevelFeedbackQueueScheduling(planeList):
    pass

# Multilevel Queue Scheduling
def multilevelQueueScheduling(planeList):
    pass
