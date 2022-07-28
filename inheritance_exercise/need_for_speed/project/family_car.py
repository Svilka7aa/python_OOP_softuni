from project.car import Car


class FamilyCar(Car):
    def __init__(self, fuel, hors_power):
        super().__init__(fuel, hors_power)