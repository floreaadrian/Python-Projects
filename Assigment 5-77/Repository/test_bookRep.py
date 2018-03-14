from unittest import TestCase
from Repository.bookRep import bookRep
from domain.books import book


class TestBookRep(TestCase):
    def setUp(self):
        self._repo = bookRep()

    def test_addBook(self):
        self._repo.addBook(book(1, "Io", "Mi", "No"))
        self._repo.addBook(book(2, "IOo", "Car", "Yes"))
        self._repo.addBook(book(34, "Plo", "Mian", "Maybe"))
        self.assertEqual(len(self._repo), 3)
        self._repo.addBook(book(54, "Car", "Ico", "No"))
        self.assertEqual(len(self._repo), 4)

    def test_findIdBook(self):
        self._repo.addBook(book(1, "Io", "Mi", "No"))
        self._repo.addBook(book(2, "IOo", "Car", "Yes"))
        self._repo.addBook(book(34, "Plo", "Mian", "Maybe"))
        assert self._repo.findIdBook(34) == 2
        assert self._repo.findIdBook(2) == 1

    def test_removeBook(self):
        self._repo.addBook(book(1, "Io", "Mi", "No"))
        self._repo.addBook(book(2, "IOo", "Car", "Yes"))
        self._repo.addBook(book(34, "Plo", "Mian", "Maybe"))
        self.assertEqual(len(self._repo), 3)
        self._repo.removeBook(2)
        self.assertEqual(len(self._repo), 2)
