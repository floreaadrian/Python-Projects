from Repository.clientRep import clientRep
from domain.clients import client
from Repository.RepositoryException import RepositoryException


class clientCSVFileRepository(clientRep):
    def __init__(self, fileName="cars.txt"):
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
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                clients = client(int(attrs[0]), attrs[1])
                clientRep.addClient(self, clients)
                line = f.readline().strip()
        except IOError:
            raise RepositoryException("Error saving file")
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        clients = clientRep.getClient(self)
        for client in clients:
            strf = str(client.get_id()) + "," + str(client.get_name()) + "\n"
            f.write(strf)
        f.close()
