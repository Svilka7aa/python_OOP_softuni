from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    BOOKS_LIMIT = 100
    BOOKS_AVAILABILITY = {}
    TOTAL_SOLD = 0
    BOOK_TITLE = "Harry Potter"
    NOT_AVAILABLE_BOOK = "Not Available"
    NUMBER_ADDED_BOOKS = 3

    def setUp(self) -> None:
        self.bookstore = Bookstore(self.BOOKS_LIMIT)

    def test_init_receive_proper_values(self):
        self.assertEqual(self.BOOKS_LIMIT, self.bookstore.books_limit)
        self.assertEqual(self.BOOKS_AVAILABILITY, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(self.TOTAL_SOLD, self.bookstore.total_sold_books)

    def test_books_limit_setter_raises_error_if_book_limit_equals_zero(self):
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = 0
        self.assertEqual(f"Books limit of 0 is not valid", str(error.exception))

    def test_books_limit_setter_raises_error_if_book_is_lower_than_zero(self):
        not_valid_books_limit = -1
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = not_valid_books_limit
        self.assertEqual(f"Books limit of {not_valid_books_limit} is not valid", str(error.exception))

    def test_len_count_books_returns_proper_number(self):
        self.BOOKS_AVAILABILITY["Harry Potter 1"] = self.NUMBER_ADDED_BOOKS
        self.BOOKS_AVAILABILITY["Game Of Thrones"] = self.NUMBER_ADDED_BOOKS
        self.bookstore.availability_in_store_by_book_titles = self.BOOKS_AVAILABILITY
        result = self.bookstore.__len__()
        expected = self.BOOKS_AVAILABILITY["Harry Potter 1"] + self.BOOKS_AVAILABILITY["Game Of Thrones"]
        self.assertEqual(expected, result)

    def test_receive_book_if_books_limit_not_enough_raise_error(self):
        self.bookstore.books_limit = 1
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book(self.BOOK_TITLE, self.NUMBER_ADDED_BOOKS)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_receive_book_adds_book_to_the_dict(self):
        self.bookstore.receive_book(self.BOOK_TITLE, self.NUMBER_ADDED_BOOKS)
        result = self.bookstore.availability_in_store_by_book_titles
        expected = {self.BOOK_TITLE: self.NUMBER_ADDED_BOOKS}
        books_dict = {self.BOOK_TITLE: self.NUMBER_ADDED_BOOKS}
        self.assertEqual(books_dict, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(expected, result)

    def test_receive_book_returns_proper_message(self):
        total_number = 0
        result = self.bookstore.receive_book(self.BOOK_TITLE, self.NUMBER_ADDED_BOOKS)
        for number in self.bookstore.availability_in_store_by_book_titles.values():
            total_number += number
        expected = f"{total_number} copies of {self.BOOK_TITLE} are available in the bookstore."
        self.assertEqual(expected, result)

    def test_sell_book_if_book_title_not_in_books(self):
        self.bookstore.receive_book(self.BOOK_TITLE, self.NUMBER_ADDED_BOOKS)
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book(self.NOT_AVAILABLE_BOOK, self.NUMBER_ADDED_BOOKS)
        self.assertEqual(f"Book {self.NOT_AVAILABLE_BOOK} doesn't exist!", str(error.exception))

    def test_sell_book_if_not_enough_books(self):
        self.bookstore.receive_book(self.BOOK_TITLE, self.NUMBER_ADDED_BOOKS)
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book(self.BOOK_TITLE, self.NUMBER_ADDED_BOOKS + 1)
        result = f"{self.BOOK_TITLE} has not enough copies to sell. Left: {self.NUMBER_ADDED_BOOKS}"
        self.assertEqual(result, str(error.exception))

    def test_sell_book_if_sell_is_successfully(self):
        self.bookstore.receive_book(self.BOOK_TITLE, self.NUMBER_ADDED_BOOKS)
        result = self.bookstore.sell_book(self.BOOK_TITLE, self.NUMBER_ADDED_BOOKS - 1)
        self.TOTAL_SOLD += self.NUMBER_ADDED_BOOKS - 1
        expected = f"Sold {self.NUMBER_ADDED_BOOKS - 1} copies of {self.BOOK_TITLE}"
        self.assertEqual(expected, result)

    def test_str_returns_proper_string(self):
        self.bookstore.receive_book(self.BOOK_TITLE, self.NUMBER_ADDED_BOOKS)
        result = self.bookstore.__str__()
        number_books = 0
        for value in self.bookstore.availability_in_store_by_book_titles.values():
            number_books += value

        expected = f"Total sold books: {self.bookstore.total_sold_books}" + "\n"
        expected += f'Current availability: {number_books}' + "\n"
        for book_title, number_of_copies in self.bookstore.availability_in_store_by_book_titles.items():
            expected += f" - {book_title}: {number_of_copies} copies" + "\n"

        self.assertEqual(expected.strip(), result)


if __name__ == "__main__":
    main()
