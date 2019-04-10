from Plane import Plane
from Algorithms import *
from random import randrange
        
def main():
                  #ID,#fuel,#capacity,passengers,priority
    LF333 = Plane("LF333", 11.0, 20.0, 24, 0)
    LF233 = Plane("LF233", 9.0, 21.0, 2, 0)
    LF133 = Plane("LF133", 7.0, 23.0, 12, 0)
    BB456 = Plane("BB456", 310.0, 400.0, 234, 1)
    HL666 = Plane("HL666", 510.0, 550, 275, 1)
    
    smallPlaneList = [LF333, LF233, LF133]
    bigPlaneList = [BB456, HL666]
    
    aggregatePlaneList = []
    
    for i in range(5):
        smallPlaneTotal = randrange(7, 11)
        for j in range(smallPlaneTotal):
            index = randrange(0, len(smallPlaneList))
            aggregatePlaneList.append(smallPlaneList[index])
        index = randrange(0, len(bigPlaneList))
        aggregatePlaneList.append(bigPlaneList[index])
    
    
    
    # planeListPriority = priorityScheduling(planeList, len(planeList))
    # 
    # printScheduleOrder(planeListPriority, "Priority")
    # printResults(planeListPriority, len(planeList))
    # 
    planeListHybrid = shortestJobFirstNp(aggregatePlaneList, len(aggregatePlaneList))
    planeListHybrid = priorityScheduling(planeListHybrid, len(planeListHybrid))
    
    printScheduleOrder(planeListHybrid, "SJF + Priority")
    printResults(planeListHybrid, len(planeListHybrid))      
    
     
main()
    
    
    
# my assumption is that total process time can be calculated by adding together 
# passengers * 2 (unboarding and boarding) and capacity - fuel
# I then replicated the algorithm online using these figures. If you fun this 
# file in pyzo you should see a nicely formatted output    
    
    













