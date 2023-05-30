# Easy 1603. Design Parking System
# Design a parking system for a parking lot.
# The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.
# Implement the ParkingSystem class:
# ParkingSystem(int big, int medium, int small)
# Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
#
# bool addCar(int carType)
# Checks whether there is a parking space of carType for the car that wants to get into the parking lot.
# carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively.
# A car can only park in a parking space of its carType.
# If there is no space available, return false, else park the car in that size space and return true.

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big, self.medium, self.small = big, medium, small

    CAR_TYPES = {1: 'big', 2: 'medium', 3: 'small'}

    def addCar(self, carType):
        name = ParkingSystem.CAR_TYPES[carType]
        val = getattr(self, name)
        if val <= 0: return False
        setattr(self, name, val-1)
        return True

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = [0, big, medium, small]

    def addCar(self, carType):
        self.slots[carType] -= 1
        return self.slots[carType] >= 0

ps = ParkingSystem(big=1, medium=1, small=0)
print(ps.addCar(carType=1))
print(ps.addCar(carType=2))
print(ps.addCar(carType=3))
print(ps.addCar(carType=1))