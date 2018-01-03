import time
import datetime


class clientRep():
    def __init__(self):
        '''
        We have a list for each of the items we need
        '''
        self._data = []

    def addClient(self, list):
        '''
        Adds a client class type to a client list
        '''
        self._data.append(list)

    def __len__(self):
        return len(self._data)

    def updateClient(self, list, oldId):
        '''
        Updates a client by removing the old one and adding the updated one
        '''
        self.removeClient(self.findIdClient(oldId))
        self.addClient(list)

    def deleteClient(self, id):
        self.removeClient(self.findIdClient(id))

    def findIdClient(self, id):
        for i in range(0, len(self._data)):
            if id == int(self._data[i].get_id()):
                return i
        return -1

    def retId(self, id):
        return self._data[id]

    def searchClient(self, val):
        val = val.upper()
        list = []
        for j in range(0, len(self._data)):
            search = self._data[j].getUpper()
            i = 0
            ok = True
            while i < len(search) + 1 and ok == True:
                if search[i:i + len(val)] == val:
                    list.append(str(self._data[j]))
                    ok = False
                i += 1
        return list

    def statClient(self, con):
        list = []
        for i in range(0, len(self._data)):
            cli = int(self._data[i].get_id())
            days = 0
            rents = con.listId()
            for j in range(0, len(rents)):
                if cli == rents[j][2]:
                    d1 = rents[j][3]
                    d2 = rents[j][5]
                    if d2 == 0 or d2 == '0':
                        today = time.strftime("%d/%m/%Y").split('/')
                        d2 = datetime.date(int(today[2]), int(today[1]), int(today[0]))
                    days += abs((d2 - d1).days)
            list.append([days, self._data[i]])
        list.sort(key=lambda x: x[0], reverse=True)
        return list

    def sortedclients(self, index, func):
        a = self._data
        i, j, size = 1, 2, len(a)
        while i < size:
            x, y = self._data[i].get_all(), self._data[i - 1].get_all()
            if func(y[index], x[index]):
                i, j = j, j + 1
            else:
                a[i - 1], a[i] = a[i], a[i - 1]
                i -= 1
                if i == 0:
                    i, j = j, j + 1
        return a

    def removeClient(self, index):
        if index < 0 or index >= len(self._data):
            raise RepositoryException("Invalid element position")
        return self._data.pop(index)

    def getClient(self):
        return self._data


class RepositoryException(Exception):
    """
    Exception class for repository errors
    """

    def __init__(self, message):
        """
        Constructor for repository exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message
