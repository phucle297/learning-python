class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    # def __init__(self, name, max_speed, mileage):
    #     super().__init__(name,max_speed,mileage)
    pass

bus = Bus('bus',100,10000)
print(bus.__dict__)