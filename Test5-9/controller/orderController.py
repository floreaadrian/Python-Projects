from domain.order import orders


class orderCon:
    def __init__(self,repo):
        self._repo = repo

    def addOrder(self, order):
        self._repo.addOrder(order)

    def calculate(self,id):
        return self._repo.calculate(id)

    def getAll(self):
        return self._repo.getAll()