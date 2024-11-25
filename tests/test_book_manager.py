import os
import unittest

from books import Book, BookManager
from core.exceptions import BookNotFoundError


class TestBookManager(unittest.TestCase):
    TEST_DB_FILE: str = "test_books.json"

    def setUp(self) -> None:
        self.manager = BookManager(file_path=self.TEST_DB_FILE)
        if os.path.exists(self.TEST_DB_FILE):
            os.remove(self.TEST_DB_FILE)

    def tearDown(self) -> None:
        if os.path.exists(self.TEST_DB_FILE):
            os.remove(self.TEST_DB_FILE)

    def test_create_book(self) -> None:
        self.manager.create(
            title="Think Python",
            author="Allen B. Downey",
            year=2016,
        )

        books: list[Book] = self.manager.all()
        first_book, *_ = books

        self.assertEqual(len(books), 1)
        self.assertEqual(first_book.title, "Think Python")
        self.assertEqual(first_book.author, "Allen B. Downey")
        self.assertEqual(first_book.year, 2016)

    def test_get_books(self) -> None:
        self.manager.create(
            title="Introducing Python, 2nd Edition",
            author="Bill Lubanovic",
            year=2019,
        )
        self.manager.create(
            title="Python Crash Course, 3rd Edition",
            author="Eric Matthes",
            year=2023,
        )

        books_by_title: list[Book] = self.manager.get(
            title="Python",
            author=None,
            year=None,
        )
        books_by_author: list[Book] = self.manager.get(
            title=None,
            author="Eric",
            year=None,
        )
        books_by_year: list[Book] = self.manager.get(
            title=None,
            author=None,
            year=2019,
        )

        self.assertEqual(len(books_by_title), 2)
        self.assertEqual(len(books_by_author), 1)
        self.assertEqual(
            books_by_author[0].title,
            "Python Crash Course, 3rd Edition",
        )
        self.assertEqual(len(books_by_year), 1)
        self.assertEqual(
            books_by_year[0].title,
            "Introducing Python, 2nd Edition",
        )

    def test_update_book_status(self) -> None:
        self.manager.create(
            title="Think Python",
            author="Allen B. Downey",
            year=2016,
        )
        first_book, *_ = self.manager.all()

        self.manager.update(pk=first_book.id, new_status="выдана")
        updated_first_book, *_ = self.manager.all()

        self.assertEqual(updated_first_book.status, "выдана")

    def test_delete_book(self) -> None:
        self.manager.create(
            title="A byte of Python",
            author="Swaroop Chitlur",
            year=2013,
        )

        first_book, *_ = self.manager.all()
        self.manager.delete(pk=first_book.id)

        self.assertEqual(len(self.manager.all()), 0)

    def test_delete_non_exists_book(self) -> None:
        with self.assertRaises(BookNotFoundError):
            self.manager.delete(pk="this_book_doesnt_exists")

    def test_file_operations(self) -> None:
        self.manager.create(
            title="Think Python, first edition",
            author="Allen B. Downey",
            year=2012,
        )

        books_before: list[Book] = self.manager.all()
        new_manager: BookManager = BookManager(file_path=self.TEST_DB_FILE)
        books_after: list[Book] = new_manager.all()

        self.assertEqual(len(books_before), len(books_after))
        self.assertEqual(
            books_before[0].title,
            books_after[0].title,
        )

    def test_empty_db(self) -> None:
        books: list[Book] = self.manager.all()

        self.assertEqual(len(books), 0)


if __name__ == "__main__":
    unittest.main()
