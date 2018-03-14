from unittest import TestCase
from domain import board,airplane

class TestBoard(TestCase):
    def setUp(self):
        self._repo = board()

    def test_cond1(self):
        self._repo.make_move(airplane(2,3,1))
        assert self._repo.cond1(3,4) == False
        assert self._repo.cond1(5,5) == True



    def test_cond2(self):
        self._repo.make_move(airplane(3,4,2))
        assert self._repo.cond1(3,4) == False
        assert self._repo.cond1(5,4) == True


    def test_cond3(self):
        self._repo.make_move(airplane(3, 3, 3))
        assert self._repo.cond1(3, 4) == False
        assert self._repo.cond1(5, 4) == True


    def test_cond4(self):
        self._repo.make_move(airplane(4, 5, 4))
        assert self._repo.cond1(4, 3) == False
        assert self._repo.cond1(3, 4) == True


    def test_validate_move(self):
        assert self._repo.validate_move(airplane(2,3,1),'player') == True
        assert self._repo.validate_move(airplane(1,3,2),'player') == False
        assert self._repo.validate_move(airplane(6,7,3),'player') == False
        assert self._repo.validate_move(airplane(3,2,4),'player') == True
        assert self._repo.validate_move(airplane(1,3,5),'player') == False
