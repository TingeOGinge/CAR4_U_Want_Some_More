import random
from random import randint
import string
import csv
from Plane import Plane

# Random data generation for larger planes
def randBigPlane():
    randID = ''.join(random.choice(string.ascii_uppercase) for i in range(2)) + str(randint(100,999))
    fuel = randint(300, 550)
    capacity = fuel + randint(10, 100)
    passengers = randint(200, 300)
    return Plane(randID, fuel, capacity, passengers, 1)

# Random data generation for smaller planes
def randSmallPlane():
    randID = ''.join(random.choice(string.ascii_uppercase) for i in range(2)) + str(randint(100,999))
    fuel = randint(5, 15)
    capacity = fuel + randint(5, 15)
    passengers = randint(2, 25)
    return Plane(randID, fuel, capacity, passengers, 0)

# File write for random plane test data
def fileWrite():

    file = open("test.txt","w")
    for i in range(50):
        file.write(str(randSmallPlane())+'\n')
    file.close()

# File read for random plane test data
def fileRead():
    test = []
    for line in open('test.txt', 'r').readlines():
        test.append(line.strip())
        print(line)
        Plane(line)

fileWrite()
fileRead()
