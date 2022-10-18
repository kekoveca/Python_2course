class Car:
    def __init__(self, capacity, speed, number):
        self.capacity = capacity
        self.speed = speed
        self.number = number

    def __repr__(self):
        return f"<Car capacity:{self.capacity} speed:{self.speed} number:{self.number}>"