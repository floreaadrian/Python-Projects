from unittest import TestCase
from Repository.clientRep import clientRep
from domain.clients import client


class TestClientRep(TestCase):
    def setUp(self):
        self._repo = clientRep()

    def test_addClient(self):
        self.assertEqual(len(self._repo), 0)
        self._repo.addClient(client(1, "Mihai"))
        self._repo.addClient(client(2, "Andrei"))
        self.assertEqual(len(self._repo), 2)

    def test_updateClient(self):
        self._repo.addClient(client(1, "Mihai"))
        self._repo.updateClient([2, "Ion"], 1)

    def test_findIdClient(self):
        self._repo.addClient(client(1, "Mihai"))
        self._repo.addClient(client(23, "Ion"))
        self._repo.addClient(client(99, "Raul"))
        assert self._repo.findIdClient(23) == 1

    def test_removeClient(self):
        self.assertEqual(len(self._repo), 0)
        self._repo.addClient(client(2, "Mihai"))
        self._repo.addClient(client(45, "Andrei"))
        self.assertEqual(len(self._repo), 2)
        self._repo.removeClient(1)
        self.assertEqual(len(self._repo), 1)
        self._repo.removeClient(0)
        self.assertEqual(len(self._repo), 0)
