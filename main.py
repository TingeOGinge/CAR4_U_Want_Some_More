from Plane import Plane
from Algorithms import *
from random import *
from data_parsing import *
import string
from string import *

#------------------------------------------------------------------------------#
#                            ALGORITHM CALLS                                   #
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#                       FIRST COME FIRST SERVED                                #
#------------------------------------------------------------------------------#

def fcfs(planeList):
    firstComeFirstServeScheduling(planeList, len(planeList))

#------------------------------------------------------------------------------#
#                               PRIORITY                                       #
#------------------------------------------------------------------------------#

def priority(planeList):
    planeListPriority = priorityScheduling(planeList)
    printScheduleOrder(planeListPriority, "Priority")
    printResults(planeListPriority, len(planeList))

#------------------------------------------------------------------------------#
#                         SHORTEST JOB FIRST                                   #
#------------------------------------------------------------------------------#

def sjf(planeList):
    planeListSJF = shortestJobFirstNp(planeList)
    printScheduleOrder(planeListSJF, "Shortest Job First")
    printResults(planeListSJF, len(planeListSJF))

#------------------------------------------------------------------------------#
#                     SHORTEST JOB FIRST + PRIORITY                            #
#------------------------------------------------------------------------------#

def sjfpr_hybrid(planeList):
    planeListHybrid = shortestJobFirstNp(planeList)
    planeListHybrid = priorityScheduling(planeListHybrid)
    printScheduleOrder(planeListHybrid, "SJF + Priority")
    printResults(planeListHybrid, len(planeListHybrid))

#------------------------------------------------------------------------------#
#                     HIGHEST RESPONSE RATIO NEXT                              #
#------------------------------------------------------------------------------#

def highestrrn(planeList):
    planeListHRRN = highestResponseRatioNext(planeList)
    printScheduleOrder(planeListHRRN, "Highest Response Ratio Next")
    printResults(planeListHRRN, len(planeListHRRN))

#------------------------------------------------------------------------------#
#                        TESTING DATA GENERATION:                              #
#------------------------------------------------------------------------------#

# List generation for Large Plane Data Sets
def largePlanesTestData():
    largePlaneList = []
    for i in range(int(input("How Many Large Planes?: "))):
        largePlaneList.append(randBigPlane())
    return largePlaneList

# List generations for Small Plane Data Sets
def smallPlanesTestData():
    smallPlaneList = []
    for i in range(int(input("How Many Small Planes?: "))):
        smallPlaneList.append(randSmallPlane())
    return smallPlaneList

#------------------------------------------------------------------------------#
#                                   MAIN:                                      #
#------------------------------------------------------------------------------#

def main():

    # highestrrn(largePlanesTestData())
    
    # fcfs(largePlanesTestData())
    highestrrn(largePlanesTestData())

    # LIST OF EXAMPLE CALLS:
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
