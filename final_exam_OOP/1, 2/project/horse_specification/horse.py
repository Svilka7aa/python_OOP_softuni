from abc import ABC, abstractmethod


class Horse(ABC):
    maximum_speed = 0

    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_take = False

    @abstractmethod
    def train(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.maximum_speed:
            raise ValueError("Horse speed is too high!")
        self.__speed = value
