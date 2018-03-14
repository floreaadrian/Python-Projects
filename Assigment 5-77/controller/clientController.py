from controller.UndoController import FunctionCall, Operation
from domain.clients import client
from domain.rents import rent


class ClientControl:
    '''
    All of these are a bonus layer,such that we don't access data directly
    '''


    def __init__(self, repo, undoController, rentC):
        self.__repo = repo
        self._undoController = undoController
        self.rentC = rentC


    def addClient(self, item, recordForUndo=True):
        self.__repo.addClient(item)
        if recordForUndo == False:
            return
        undo = FunctionCall(self.removeClient, item.get_id(), False)
        redo = FunctionCall(self.addClient, client(item.get_id(), item.get_name()), False)
        operation = [Operation(redo, undo)]
        self._undoController.recordOperation(operation)


    def removeClient(self, id, recordForUndo=True):
        clin = self.__repo.retId(self.findIdClient(id))
        self.__repo.removeClient(self.findIdClient(id))
        rents = []
        k = self.rentC.findIdClient(id)
        if recordForUndo == False:
            return
        while k != -1:
            rento = self.rentC.getRentById(k)
            rents.append(rent(rento.get_id(), rento.get_bookId(), rento.get_client(), rento.getRent(), rento.getDue(),
                              rento.getRet()))
            self.rentC.removeRent(k, False)
            k = self.rentC.findIdClient(id)
        undo = FunctionCall(self.addClient, clin, False)
        redo = FunctionCall(self.removeClient, id, False)
        operation = [Operation(redo, undo)]
        for renties in rents:
            undo = FunctionCall(self.rentC.addRent,
                                rent(renties.get_id(), renties.get_bookId(), renties.get_client(), renties.getRent(),
                                     renties.getDue(), renties.getRet()), False)
            redo = FunctionCall(self.rentC.removeRentNot, renties.get_id())
            operation.append(Operation(redo, undo))
        self._undoController.recordOperation(operation)


    def updateClient(self, item, oldId, recordForUndo=True):
        name = (self.__repo.retId(self.findIdClient(id))).get_name()
        self.__repo.updateClient(item, oldId)
        if recordForUndo == False:
            return
        undo = FunctionCall(self.updateClient, client(oldId, name), oldId, False)
        redo = FunctionCall(self.updateClient, item, oldId, False)
        operation = [Operation(redo, undo)]
        self._undoController.recordOperation(operation)


    def searchClient(self, val):
        return self.__repo.searchClient(val)


    def statClient(self, con):
        return self.__repo.statClient(con)


    def sortedclients(self, index, func):
        return self.__repo.sortedclients(index, func)


    def findIdClient(self, id):
        return self.__repo.findIdClient(id)


    def filter(self, para, cond):
        return self.__repo.filter(para, cond)


    def getClient(self):
        return self.__repo.getClient()
