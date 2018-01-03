from controller.UndoController import FunctionCall, Operation
from domain.rents import rent

class RentControl:
    '''
    All of these are a bonus layer,such that we don't access data directly
    '''
    def __init__(self, repo, undoController):
        self.__repo = repo
        self._undoController = undoController

    def listId(self):
        return self.__repo.listId()

    def addRent(self, item,recordForUndo=True):
        self.__repo.addRent(item)
        if recordForUndo == False:
            return
        undo = FunctionCall(self.removeRent, self.findIdRent(item.get_id()),False)
        redo = FunctionCall(self.addRent, rent(item.get_id(),item.get_bookId(),item.get_client(),item.getRent(),item.getDue(),item.getRet()),False)
        operation = [Operation(redo, undo)]
        self._undoController.recordOperation(operation)

    def removeRentNot(self,id):
        self.__repo.removeRent(self.findIdRent(id))

    def removeRent(self, id, recordForUndo=True):
        rento = self.__repo.getRentById(id)
        self.__repo.removeRent(id)
        if recordForUndo == False:
            return
        undo = FunctionCall(self.addRent, rent(rento.get_id(),rento.get_bookId(),rento.get_client(),rento.getRent(),rento.getDue(),rento.getRet()),False)
        redo = FunctionCall(self.removeRent, id,False)
        operation = [Operation(redo, undo)]
        self._undoController.recordOperation(operation)

    def getRentById(self,id):
        return self.__repo.getRentById(id)

    def update(self,new_id,old_id):
        self.__repo.update(new_id,old_id)

    def updateRent(self,rentId,date,recordForUndo=True):
        self.__repo.updateRent(rentId,date)
        if recordForUndo == False:
            return
        undo = FunctionCall(self.updateRent,rentId, '0',False)
        redo = FunctionCall(self.updateRent,rentId, date,False)
        operation = []
        operation.append(Operation(redo, undo))
        self._undoController.recordOperation(operation)

    def statRents(self):
        return self.__repo.statRents()

    def sortedrents(self,index,func):
        return self.__repo.sortedrents(index,func)

    def findIdRent(self, id):
        return self.__repo.findIdRent(id)

    def findIdClient(self, id):
        return self.__repo.findIdClient(id)

    def findIdRentBook(self,id):
        return self.__repo.findIdRentBook(id)

    def getRent(self):
        return self.__repo.getRent()