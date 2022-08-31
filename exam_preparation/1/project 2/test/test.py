from unittest import TestCase

from project.movie import Movie


class TestMovie(TestCase):
    NAME = "The Shutter Island"
    YEAR = 2010
    RATING = 8
    MIN_YEAR = 1887

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_movie_init(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_raises_error_with_empty_string(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_year_setter_raises_error_with_year_lt_min_year(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = self.MIN_YEAR - 10
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor_append_name_does_not_exists(self):
        first = "Pesho"
        second = "Georgi"

        self.movie.add_actor(first)
        self.movie.add_actor(second)

        self.assertEqual([first, second], self.movie.actors)

    def test_add_actors_returns_error_message_with_duplicated_name(self):
        name = "Georgi"
        self.movie.actors = [name]
        result = self.movie.add_actor(name)

        self.assertEqual(f"{name} is already added in the list of actors!", result)
        self.assertEqual([name], self.movie.actors)

    def test_gt_returns_true_when_first_movie_has_grater_rating(self):
        another_movie_name = "The Matrix"
        another_movie = Movie(another_movie_name, 1999, self.RATING - 1)

        first_result = self.movie > another_movie
        second_result = another_movie > self.movie
        expected = f'"{self.movie.name}" is better than "{another_movie_name}"'
        self.assertEqual(expected, first_result)
        self.assertEqual(expected, second_result)

    def test_repr_Returns_proper_String(self):
        actors = ["Georgi", "Paulina"]
        self.movie.actors = actors

        actual_result = repr(self.movie)
        expected = f"Name: {self.NAME}\n" \
                   f"Year of Release: {self.YEAR}\n" \
                   f"Rating: {self.RATING:.2f}\n" \
                   f"Cast: {', '.join(actors)}"

        self.assertEqual(actual_result, expected)


