
from Repository.clientRep import clientRep

import pickle


class PickleFileclientRep(clientRep):
    def __init__(self, fileName="clients.pickle"):
        clientRep.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def addClient(self, list):
        clientRep.addClient(self, list)
        self.__storeToFile()

    def deleteClient(self, clientId):
        clientRep.deleteClient(self, clientId)
        self.__storeToFile()

    def updateClient(self, list, oldId):
        clientRep.updateClient(self, list, oldId)
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