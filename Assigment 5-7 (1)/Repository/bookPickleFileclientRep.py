
from Repository.bookRep import bookRep

import pickle


class PickleFilebookRep(bookRep):
    def __init__(self, fileName="books.pickle"):
        bookRep.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def addBook(self,list):
        bookRep.addBook(self, list)
        self.__storeToFile()

    def removeBook(self, id):
        bookRep.removeBook(self, id)
        self.__storeToFile()

    def updateBook(self, list, oldId):
        bookRep.updateBook(self, list, oldId)
        self.__storeToFile()

    def __loadFromFile(self):
        f = open(self.__fName, "rb")
        try:
            self._data = pickle.load(f)
        except EOFError:
            self._data = []
        except Exception as e:
            raise e
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "wb")
        pickle.dump(self._data, f)
        f.close()