from Plane import Plane
from Algorithms import *
from random import *
from data_parsing import *
import string 
from string import *

def fcfs(planeList):
    firstComeFirstServeScheduling(planeList, len(planeList))

def priority(planeList):
    planeListPriority = priorityScheduling(planeList) 
    printScheduleOrder(planeListPriority, "Priority")
    printResults(planeListPriority, len(planeList))
    
def sjfpr_hybrid(planeList):
    planeListHybrid = shortestJobFirstNp(planeList)
    planeListHybrid = priorityScheduling(planeListHybrid)
    printScheduleOrder(planeListHybrid, "SJF + Priority")
    printResults(planeListHybrid, len(planeListHybrid)) 

def highestrrn(planeList):
    planeListHRRN = highestResponseRatioNext2(planeList) 
    printScheduleOrder(planeListHRRN, "Highest Response Ratio Next")
    printResults(planeListHRRN, len(planeListHRRN))

def sjf(planeList):
    planeListSJF = shortestJobFirstNp(planeList)
    printScheduleOrder(planeListSJF, "Shortest Job First")
    printResults(planeListSJF, len(planeListSJF))
        
def main():
                  #ID,#fuel,#capacity,passengers,priority
    # LF333 = Plane("LF333", 11.0, 20.0, 24, 0)
    # LF233 = Plane("LF233", 9.0, 21.0, 2, 0)
    # LF133 = Plane("LF133", 7.0, 23.0, 12, 0)
    # BB456 = Plane("BB456", 310.0, 400.0, 234, 1)
    # HL666 = Plane("HL666", 510.0, 550, 275, 1)
    # 
    # planeList = [LF333, LF233, LF133, BB456, HL666]


    # List generation for Large Plane Data Sets
    largePlaneList = []
    
    for i in range(50):
        largePlaneList.append(randBigPlane())
        
    largePlaneList[0].arrivalTime = 0.0

    # List generations for Small Plane Data Sets
    smallPlaneList = []

    for i in range(50):
        smallPlaneList.append(randSmallPlane())  
         
    smallPlaneList[0].arrivalTime = 0.0
    completePlaneList = []

    for i in range(50):
        completePlaneList.append(randSmallPlane())
        completePlaneList.append(randBigPlane())
    
    sjf(smallPlaneList)    
    highestrrn(smallPlaneList)
    
    sjf(largePlaneList)
    highestrrn(largePlaneList)
    
    
    # fcfs(smallPlaneList)
    # shortestJobFirstNp(smallPlaneList)
    # highestrrn(smallPlaneList)
    # fcfs(largePlaneList)
    # shortestJobFirstNp(largePlaneList)
    # highestrrn(largePlaneList)
    
main()
    
    
    
# my assumption is that total process time can be calculated by adding together 
# passengers * 2 (unboarding and boarding) and capacity - fuel
# I then replicated the algorithm online using these figures. If you fun this 
# file in pyzo you should see a nicely formatted output    







