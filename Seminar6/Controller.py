class control:
    def __init__(self, repo):
        self.__repo = repo
        self.__undo = []

    def addItem(self, item):
        self.__undo = self.__repo.getAll()[:]
        self.__repo.addItem(item)

    def removeItem(self, id):
        self.__undo = self.__repo.getAll()[:]
        self.__repo.removeItem(self.findIdItem(id))

    def updateItem(self, oldId, item):
        self.__undo = self.__repo.getAll()[:]
        self.__repo.updateItem(oldId, item)

    def findIdItem(self, id):
        return self.__repo.findIdItem(id)

    def getAll(self):
        return self.__repo.getAll()


class ControllerException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message
