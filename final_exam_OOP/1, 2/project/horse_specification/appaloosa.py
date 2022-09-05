from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    maximum_speed = 120
    horse_breed = "Appaloosa"
    increase_speed_when_train = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed += self.increase_speed_when_train
        if self.speed > self.maximum_speed:
            self.speed = self.maximum_speed
