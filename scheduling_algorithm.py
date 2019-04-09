class Plane:
    def __init__(self, id, fuel, capacity, passengers, priority):
        self.id = id
        self.fuel = fuel
        self.capacity = capacity
        self.passengers = passengers
        self.turnAround = (capacity - fuel) + (passengers * 2)
        self.priority = priority
        self.waitTime = 0.0
        
    def info(self):
        breakdown = "ID: {0}".format(id) \
            + "Fuel: {0:.2f} \n".format(self.fuel) \
            + "Capacity: {0:.2f} \n".format(self.capacity) \
            + "Passengers: {0:.2f} \n".format(self.passengers) \
            + "Turn Around: {0:f} \n".format(self.turnAround) \
            + "High Priority: {0} \n".format(self.priority) \
            + "Current wait time: {0:.2f} \n".format(self.waitTime) 
        return breakdown

#-------------------------------------------------------------------------------

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
    
def main():
    LF333 = Plane("LF333", 11.0, 20.0, 24, 0)
    LF233 = Plane("LF233", 9.0, 21.0, 2, 0)
    LF133 = Plane("LF133", 7.0, 23.0, 12, 0)
    BB456 = Plane("BB456", 310.0, 400.0, 234, 1)
    HL666 = Plane("HL666", 510.0, 550, 275, 1)
    
    planeList = [LF333, LF233, LF133, BB456, HL666]
    n = len(planeList)
    
    priorityScheduling(planeList, n)
    
main()
    
    
    
# my assumption is that total process time can be calculated by adding together 
# passengers * 2 (unboarding and boarding) and capacity - fuel
# I then replicated the algorithm online using these figures. If you fun this 
# file in pyzo you should see a nicely formatted output    
    
    













