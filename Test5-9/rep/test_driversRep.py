from unittest import TestCase
from domain.driver import drivers
from rep.driverRep import driversRep

class TestDriversRep(TestCase):
    def setUp(self):
        self._repo = driversRep()

    def test_findId(self):
        self._repo.addDriver(drivers(1,"Mihai"))
        self._repo.addDriver(drivers(2, "Ion"))
        self._repo.addDriver(drivers(34532, "Cristi"))
        self._repo.addDriver(drivers(322, "Mihaiel"))
        assert self._repo.findId(3) == False
        assert self._repo.findId(322) == True
        assert self._repo.findId(34532) == True
        assert self._repo.findId(32) == False
