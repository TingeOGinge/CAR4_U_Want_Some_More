def findWaitingTime(planeList, n, waitingTimes, turnAroundTimes):
    waitingTimes[0] = 0
    
    for i in range(1, n):
        waitingTimes[i] = planeList[i - 1].turnAround + waitingTimes[i - 1]

def findTurnAroundtime(planeList, n, waitingTimes, turnAroundTimes):
    for i in range(n):
        turnAroundTimes[i] = planeList[i].turnAround + waitingTimes[i]

def findAverageTime(planeList, n):
    waitingTimes = [0] * n
    turnAroundTimes = [0] * n
    
    findWaitingTime(planeList, n, waitingTimes, turnAroundTimes)    
    findTurnAroundtime(planeList, n, waitingTimes, turnAroundTimes)
    headings = ["Planes", "Burst Time", "Wait Time", "Turn Around Time \n"]
    for h in headings:
        print("{0:18}".format(h), end="")
        
    totalWaitTime = 0
    totalTurnAroundTime = 0
    
    for i in range(n):
        totalWaitTime += waitingTimes[i]
        totalTurnAroundTime += turnAroundTimes[i]
        print("{0:18}{1:<18.1f}{2:<18.1f}{3:<18.1f}".format(planeList[i].id, 
                planeList[i].turnAround, waitingTimes[i], turnAroundTimes[i]))
    
def priorityScheduling(planeList, n):
    planeList = sorted(planeList, key = lambda planeList:planeList.priority,  
    reverse = True)
    print("Ordered via priority: ", end="")
    for plane in planeList:
        print("{0}, ".format(plane.id), end=" ")
    print("\n")
    findAverageTime(planeList, n)