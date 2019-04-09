class Plane:
    def __init__(self, fuel, capacity, passengers, highPriority):
        self.fuel = fuel
        self.capacity = capacity
        self.passengers = passengers
        self.inAndOutTime = self.passengers * 2
        self.highPriorty = highPriority
        self.waitTime = 0.0

        # Land
        def land(self):           
            if self.highPriorty:
                return 1
            else
                return 2

        # # Refuel
        # 
        # def refuel(self):
        #     pass

        #One ladder for priority shared if not in use
        

        #One ladder dedicated to small aircraft 
        #FCFS
                
        # Depart
        def depart(self):
            return 1

def main():
    #small planes average 12.3 fuelling requirements
    LF333 = Plane(11.0, 20.0, 24, False)
    LF233 = Plane(9.0, 21.0, 2, False)
    LF133 = Plane(7.0, 23.0, 12, False)
    #large planes average 65
    BB456 = Plane(310.0, 400.0, 234, True)
    HL666 = Plane(510.0, 550, 275, True) 
    
    planeList = [LF333, LF233, BB456, HL666]
    
