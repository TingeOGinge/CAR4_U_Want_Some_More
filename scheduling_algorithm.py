class Plane:
    def __init__(self, fuel, capacity, passengers, highPriority):
        this.fuel = fuel
        this.capacity = capacity
        this.passengers = passengers
        this.highPriorty = highPriority
        this.waitTime = 0.0

def main():
    LF333 = Plane(11.0, 20.0, 24, false)
    LF233 = Plane(9.0, 21.0, 2, false)
    LF133 = Plane(7.0, 23.0, 12, false)
    BB456 = Plane(310.0, 400.0, 234, true)
    HL666 = Plane(510.0, 550, 275, true)
    
    planeList = [LF333, LF233, BB456, HL666]
    
    priorityScheduling(planeList)
    
    
def priorityScheduling(planeList):
    planeList = sorted(planeList, key = lambda planeList:planeList[2])
    print(String(planeList))
    for plane in planeList:
        findWaitTime(plane)
        findTurnAroundTime(plane)
    findAvgTime(planeList)
        

def findWaitTime(plane):
    pass


def findTurnAroundTime(plane):
    pass


def findAvgTime(planeList):
    pass


