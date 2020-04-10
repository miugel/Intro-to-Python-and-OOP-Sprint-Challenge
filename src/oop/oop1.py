# write classes for the following class hierarchy:

#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]

# each class can simply 'pass' for its body 
# the exercise is about setting up the hierarchy
# put a comment noting which class is the base class

# base class
class Vehicle:
    pass

class FlightVehicle(Vehicle):
    pass

class Starship(FlightVehicle):
    pass

class GroundVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass