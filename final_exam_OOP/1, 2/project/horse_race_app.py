from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = None
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            horse = Thoroughbred(horse_name, horse_speed)
        if horse.name in self.horses:
            return f"Horse {horse_name} has been already added!"
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        existing_jockey = [j.name for j in self.jockeys if j.name == jockey_name]
        if existing_jockey:
            raise f"Jockey {jockey_name} has been already added!"
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in self.horse_races:
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = [j for j in self.jockeys if j.name == jockey_name]
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horse = [h for h in self.horses if h.horse_breed == horse_type]
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey[0].horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey[0].horse = horse[0]
        return f"Jockey {jockey_name} will ride the horse {horse[0].name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        races = [r for r in self.horse_races if r.race_type == race_type]
        if not races:
            raise Exception(f"Race {race_type} could not be found!")

        jockeys = [j for j in self.jockeys if j.name == jockey_name]
        if not jockeys:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey = jockeys[0]
        race = races[0]
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        races = [r for r in self.horse_races if r.race_type == race_type]
        if not races:
            raise Exception(f"Race {race_type} could not be found!")
        race = races[0]
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None
        max_speed = 0

        for jockey in race.jockeys:
            if max_speed < jockey.horse.speed:
                max_speed = jockey.horse.speed
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {max_speed}km/h is" \
               f" {winner.name}! Winner's horse: {winner.horse.name}."
