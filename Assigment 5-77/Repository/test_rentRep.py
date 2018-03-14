import unittest
from Repository.rentRep import rentRep
from domain.rents import rent


class TestRentRep(unittest.TestCase):
    def setUp(self):
        self._repo = rentRep()

    def test_addRent(self):
        self._repo.addRent(rent(1, 1, 1, 0, 0, 0))
        self.assertEqual(len(self._repo), 1)
        self._repo.addRent(rent(2, 1, 1, 0, 0, 0))
        self.assertEqual(len(self._repo), 2)

    def test_findIdRentBook(self):
        self._repo.addRent(rent(1, 2, 1, 0, 0, 0))
        assert self._repo.findIdRentBook(2) == 0
        self._repo.addRent(rent(2, 43, 1, 0, 0, 0))
        self._repo.addRent(rent(3, 54, 1, 0, 0, 0))
        assert self._repo.findIdRentBook(43) == 1
        assert self._repo.findIdRentBook(54) == 2

    def test_findIdClient(self):
        self._repo.addRent(rent(1, 2, 1, 0, 0, 0))
        assert self._repo.findIdClient(1) == 0
        self._repo.addRent(rent(2, 43, 342, 0, 0, 0))
        self._repo.addRent(rent(3, 54, 32, 0, 0, 0))
        assert self._repo.findIdClient(342) == 1
        assert self._repo.findIdClient(32) == 2

    def test_findIdRent(self):
        self._repo.addRent(rent(1, 2, 1, 0, 0, 0))
        assert self._repo.findIdRent(1) == 0
        self._repo.addRent(rent(2, 43, 1, 0, 0, 0))
        self._repo.addRent(rent(3, 54, 1, 0, 0, 0))
        assert self._repo.findIdRent(2) == 1
        assert self._repo.findIdRent(3) == 2

    def test_removeRent(self):
        self._repo.addRent(rent(1, 1, 1, 0, 0, 0))
        self.assertEqual(len(self._repo), 1)
        self._repo.addRent(rent(2, 1, 1, 0, 0, 0))
        self.assertEqual(len(self._repo), 2)
        self._repo.removeRent(1)
        self.assertEqual(len(self._repo), 1)

if __name__ == '__main__':
    unittest.main()