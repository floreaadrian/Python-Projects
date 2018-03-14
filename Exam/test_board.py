from unittest import TestCase
from domain import Board, Point


class TestBoard(TestCase):
    def setUp(self):
        self.repo = Board()

    def test_checkWin1(self):
        """
        We verify if the check works well when we have a diagonal
        """
        self.repo.makeMovePlayer(Point(0, 0, "O"))
        self.repo.makeMovePlayer(Point(1, 1, "O"))
        self.repo.makeMovePlayer(Point(2, 2, "O"))
        self.repo.makeMovePlayer(Point(3, 3, "O"))
        self.repo.makeMovePlayer(Point(4, 4, "O"))
        self.assertEqual(True, self.repo.checkWin())

    def test_checkWin2(self):
        """
        We verify if the check works well when we have 5 consecutive in a row
        """
        self.repo.Empty()
        self.repo.makeMovePlayer(Point(0, 0, "O"))
        self.repo.makeMovePlayer(Point(0, 1, "O"))
        self.repo.makeMovePlayer(Point(0, 2, "O"))
        self.repo.makeMovePlayer(Point(0, 3, "O"))
        self.repo.makeMovePlayer(Point(0, 4, "O"))
        self.assertEqual(True, self.repo.checkWin())

    def test_checkWin3(self):
        """
        We verify if the check works well when we have a diagonal
        """
        self.repo.Empty()
        self.repo.makeMovePlayer(Point(0, 5, "X"))
        self.repo.makeMovePlayer(Point(1, 4, "X"))
        self.repo.makeMovePlayer(Point(2, 3, "X"))
        self.repo.makeMovePlayer(Point(3, 2, "X"))
        self.repo.makeMovePlayer(Point(4, 1, "X"))
        self.assertEqual(True, self.repo.checkWin())

    def test_checkWin4(self):
        """
        We verify if the check works well when we have a 5 consecutive in a column
        """
        self.repo.Empty()
        self.repo.makeMovePlayer(Point(0, 0, "O"))
        self.repo.makeMovePlayer(Point(1, 0, "O"))
        self.repo.makeMovePlayer(Point(2, 0, "O"))
        self.repo.makeMovePlayer(Point(3, 0, "O"))
        self.repo.makeMovePlayer(Point(4, 0, "O"))
        self.assertEqual(True, self.repo.checkWin())

    def test_checkWin5(self):
        """
        We verify if the check works well when we don't have a win
        """
        self.repo.Empty()
        self.repo.makeMovePlayer(Point(0, 0, "O"))
        self.repo.makeMovePlayer(Point(0, 1, "O"))
        self.repo.makeMovePlayer(Point(0, 2, "O"))
        self.repo.makeMovePlayer(Point(0, 3, "O"))
        self.assertEqual(False, self.repo.checkWin())

    def test_checkWin6(self):
        """
        We verify if the check works well when we don't have a win
        """
        self.repo.Empty()
        self.repo.makeMovePlayer(Point(2, 0, "X"))
        self.repo.makeMovePlayer(Point(2, 1, "X"))
        self.repo.makeMovePlayer(Point(2, 2, "X"))
        self.repo.makeMovePlayer(Point(2, 3, "X"))
        self.repo.makeMovePlayer(Point(2, 4, "X"))
        self.assertEqual(True, self.repo.checkWin())

    def test_valide_move(self):
        self.assertEqual(self.repo.valide_move(1, 3), True)
        self.assertEqual(self.repo.valide_move(0, -1), False)
        self.assertEqual(self.repo.valide_move(5, 5), True)
        self.assertEqual(self.repo.valide_move(1, 0), True)
        self.repo.makeMovePlayer(Point(0, 3, "O"))
        self.assertEqual(self.repo.valide_move(0, 3), False)

    def test_makeMovePlayer(self):
        self.repo.makeMovePlayer(Point(0, 3, "O"))
        self.assertEqual(self.repo.valide_move(0, 3), False)

    def test_makeMoveAi(self):
        self.repo.makeMoveAi()
        self.repo.makeMovePlayer(Point(2, 1, "X"))
        self.repo.makeMovePlayer(Point(2, 2, "X"))
        self.repo.makeMovePlayer(Point(2, 3, "X"))
        self.repo.makeMoveAi()
        self.assertEqual(self.repo.checkWin(), False)
        self.repo.makeMovePlayer(Point(2, 4, "X"))
        self.repo.makeMoveAi()
        self.assertEqual(self.repo.checkWin(), True)
