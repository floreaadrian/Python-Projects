from unittest import TestCase
from domain.order import orders
from rep.orderRep import ordersRep

class TestOrdersRep(TestCase):
    def setUp(self):
        self._repo = ordersRep()

    def test_addOrder(self):
        self._repo.addOrder(orders(1,3))
        self._repo.addOrder(orders(32,44))
        self._repo.addOrder(orders(54,2))

    def test_calculate(self):
        self._repo.addOrder(orders(4, 3))
        self._repo.addOrder(orders(4, 44))
        self._repo.addOrder(orders(33, 2))
        assert self._repo.calculate(4) == '117.5'

    def test_getAll(self):
        self._repo.addOrder(orders(1, 3))
        self._repo.addOrder(orders(32, 44))
        self._repo.addOrder(orders(54, 2))
        pass
