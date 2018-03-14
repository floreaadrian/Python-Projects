from Repository.rentRep import rentRep

import pickle


class PickleFilerentRep(rentRep):
    def __init__(self, fileName="rents.pickle"):
        rentRep.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def addRent(self, list):
        rentRep.addRent(self, list)
        self.__storeToFile()

    def removeRent(self, rentId):
        rentRep.removeRent(self, rentId)
        self.__storeToFile()

    def updateRent(self, rentId, today):
        rentRep.updateRent(self, rentId, today)
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
