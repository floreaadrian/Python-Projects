
class ListControl:
    '''
    All of these are a bonus layer,such that we don't access data directly
    '''
    def __init__(self, repo):
        self.__repo = repo
        self.__undo = []

    def addBook(self, item):
        self.__undo = self.__repo.getBook()[:]
        self.__repo.addBook(item)

    def addClient(self, item):
        self.__undo = self.__repo.getClient()[:]
        self.__repo.addClient(item)

    def addRent(self, item):
        self.__undo = self.__repo.getRent()[:]
        self.__repo.addRent(item)

    def removeClient(self, id):
        self.__undo = self.__repo.getClient()[:]
        self.__repo.removeClient(self.findIdClient(id))

    def removeBook(self, id):
        self.__undo = self.__repo.getBook()[:]
        self.__repo.removeBook(self.findIdBook(id))

    def removeRent(self, id):
        self.__undo = self.__repo.getRent()[:]
        self.__repo.removeRent(self.findIdRentBook(id))

    def updateRent(self,rentId):
        self.__undo = self.__repo.getRent()[:]
        self.__repo.updateRent(rentId)

    def updateBook(self, oldId, item):
        self.__undo = self.__repo.getBook()[:]
        self.__repo.updateBook(oldId, item)

    def updateClient(self, oldId, item):
        self.__undo = self.__repo.getClient()[:]
        self.__repo.updateClient(oldId, item)

    def searchBook(self,val):
        return self.__repo.searchBook(val)

    def searchClient(self,val):
        return self.__repo.searchClient(val)

    def statBook(self,case):
        return self.__repo.statBook(case)

    def statClient(self):
        return self.__repo.statClient()

    def statAuthor(self):
        return self.__repo.statAuthor()

    def statRents(self):
        return self.__repo.statRents()

    def findIdBook(self, id):
        return self.__repo.findIdBook(id)

    def findIdRent(self, id):
        return self.__repo.findIdRent(id)

    def findIdClient(self,id):
        return self.__repo.findIdClient(id)

    def findIdRentBook(self,id):
        return self.__repo.findIdRentBook(id)

    def getBook(self):
        return self.__repo.getBook()

    def getClient(self):
        return self.__repo.getClient()

    def getRent(self):
        return self.__repo.getRent()

class ControllerException(Exception):

    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message
