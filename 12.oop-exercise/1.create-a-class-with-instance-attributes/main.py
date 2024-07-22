class Vehicle:
    def __init__(self, max_speed, mileage)->None:
        self.max_speed = max_speed
        self.mileage = mileage
    def __str__(self) -> str:
        return f"max_speed: {self.max_speed}, mileage: {self.mileage}"

bike = Vehicle(100,10000)
print(bike)