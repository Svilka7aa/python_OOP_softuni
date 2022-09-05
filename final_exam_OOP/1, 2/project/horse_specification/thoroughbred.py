from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    maximum_speed = 140
    horse_breed = "Thoroughbred"
    increase_speed_when_train = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed += self.increase_speed_when_train
        if self.speed > self.maximum_speed:
            self.speed = self.maximum_speed
