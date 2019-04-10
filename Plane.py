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
        breakdown = "ID: {0}".format(self.id) \
            + "Fuel: {0:.2f} \n".format(self.fuel) \
            + "Capacity: {0:.2f} \n".format(self.capacity) \
            + "Passengers: {0:.2f} \n".format(self.passengers) \
            + "Turn Around: {0:f} \n".format(self.turnAround) \
            + "High Priority: {0} \n".format(self.priority) \
            + "Wait Time: {0} \n".format(self.waitTime)
        return breakdown