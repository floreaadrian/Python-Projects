from controller.UndoController import FunctionCall, Operation
from domain.books import book
from domain.rents import rent


class BookControl:
    '''
    All of these are a bonus layer,such that we don't access data directly
    '''

    def __init__(self, repo, undoController, rentC):
        self.__repo = repo
        self._undoController = undoController
        self.rentC = rentC

    def addBook(self, item, recordForUndo=True):
        '''
        Add's a book by the parameter item
        Item is a book type class
        '''
        self.__repo.addBook(item)
        if recordForUndo == False:
            return
        undo = FunctionCall(self.removeBook, item.get_id(), False)
        redo = FunctionCall(self.addBook, book(item.get_id(), item.get_title(), item.get_author(), item.get_desc()),
                            False)
        operation = [Operation(redo, undo)]
        self._undoController.recordOperation(operation)

    def removeBook(self, id, recordForUndo=True):
        '''
            Delete's a book by the id
            We still need to find the position in the list
        '''
        bookr = self.__repo.retId(self.findIdBook(id))
        rents = []
        self.__repo.removeBook(self.findIdBook(id))
        k = self.rentC.findIdRentBook(id)
        if recordForUndo == False:
            return
        while k != -1:
            rento = self.rentC.getRentById(k)
            rents.append(rent(rento.get_id(), rento.get_bookId(), rento.get_client(), rento.getRent(), rento.getDue(),
                              rento.getRet()))
            self.rentC.removeRent(k, False)
            k = self.rentC.findIdRentBook(id)
        operation = []
        undo = FunctionCall(self.addBook, bookr, False)
        redo = FunctionCall(self.removeBook, id, False)
        operation.append(Operation(redo, undo))
        for renties in rents:
            undo = FunctionCall(self.rentC.addRent,
                                rent(renties.get_id(), renties.get_bookId(), renties.get_client(), renties.getRent(),
                                     renties.getDue(), renties.getRet()), False)
            redo = FunctionCall(self.rentC.removeRentNot, renties.get_id())
            operation.append(Operation(redo, undo))
        self._undoController.recordOperation(operation)

    def updateBook(self, item, oldId, recordForUndo=True):
        '''
        Updates by deleting the old item
        And adding one new
        :param item: Book class object
        :param oldId: Id
        :return:
        '''
        bookr = self.__repo.retId(self.findIdBook(oldId))
        self.__repo.updateBook(item, oldId)
        if recordForUndo == False:
            return
        undo = FunctionCall(self.updateBook, bookr, oldId, False)
        redo = FunctionCall(self.updateBook, item, oldId, False)
        operation = [Operation(redo, undo)]
        self._undoController.recordOperation(operation)

    def statBook(self, case, con):
        '''
        Returns the status of the most rented books
        '''
        return self.__repo.statBook(case, con)

    def statAuthor(self, con):
        '''
        Returns the status of the most rented author
        '''
        return self.__repo.statAuthor(con)

    def sortedbooks(self, index, func):
        return self.__repo.sortedbooks(index, func)

    def searchBook(self, val):
        '''
        Searchs in books after the val parametere
        '''
        return self.__repo.searchBook(val)

    def filter(self,para,cond):
        return self.__repo.filter(para,cond)

    def findIdBook(self, id):
        return self.__repo.findIdBook(id)

    def getBook(self):
        return self.__repo.getBook()
