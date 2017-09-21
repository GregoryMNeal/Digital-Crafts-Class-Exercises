class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.make, self.model, self.year)

# You can set the attributes of an object when the object is instantiated
# by passing parameters when it is created.  These parameters are used
# in the constructor method (__init__) to set the attributes at the time
# of object creation.
#  For example:  car = Vehicle('Ford', 'F150', '2012')
car = Vehicle('Ford', 'F150', '2012')

car.print_info()

# You can directly access the attributes for object with the following
# syntax:  objectname.attributename, e.g. car.make
car.make = 'Harley-Davidson'
car.model = 'FXSB Breakout'
car.year = '2014'

# You can invoke a behavior of an object by referencing the behavior
# (method/function) with the following syntax:
#  objectname.method()
car.print_info()
