class Car:
    def __init__(self, capacity, speed, number):
        self.capacity = capacity
        self.speed = speed
        self.number = number

class RaceCar(Car):
    def __init__(self, speed, capacity = 0, number = None):
        self.speed = speed
        self.capacity = capacity
        self.number = number


c = Car(1000, 100, "a720po")
print(c.capacity, c.speed, c.number)
r = RaceCar(300)
print(r.capacity, r.speed, r.number)