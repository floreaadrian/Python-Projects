import time
import datetime
from Repository.iterabile import iterabil

class rentRep():
    def __init__(self):
        '''
        We have a list for each of the items we need
        '''
        self._data = iterabil()

    def addRent(self, list):
        '''
        Adds a rent class type to a rent list
        '''
        self._data.append(list)

    def listId(self):
        '''
        :return: The whole rent list for statistics
        '''
        list = []
        for i in range(0, len(self._data)):
            list.append(self._data[i].get_all())
        return list

    def __len__(self):
        return len(self._data)

    def getRentById(self, id):
        return self._data[id]

    def findIdRentBook(self, id):
        for i in range(0, len(self._data)):
            if id == int(self._data[i].get_bookId()):
                return i
        return -1

    def findIdClient(self, id):
        for i in range(0, len(self._data)):
            if id == int(self._data[i].get_client()):
                return i
        return -1

    def findIdRent(self, id):
        for i in range(0, len(self._data)):
            if id == int(self._data[i].get_id()):
                return i
        return -1

    def update(self, new_id, old_id):
        self._data[self.findIdRentBook(old_id)].setBookId(new_id)

    def updateRent(self, rentId, today):
        if today == '0':
            self._data[rentId].modifyReturn('0')
        else:
            today = today.split('/')
            self._data[rentId].modifyReturn(datetime.date(int(today[2]), int(today[1]), int(today[0])))

    def statRents(self):
        list = []
        for i in range(0, len(self._data)):
            d1 = self._data[i].getDue()
            d2 = self._data[i].getRet()
            if d2 == "0":
                today = time.strftime("%d/%m/%Y").split('/')
                d2 = datetime.date(int(today[2]), int(today[1]), int(today[0]))
                if d1 < d2:
                    rentdelay = abs((d2 - d1).days)
                    list.append([rentdelay, self._data[i]])
            else:
                if d1 < d2:
                    rentdelay = abs((d2 - d1).days)
                    list.append([rentdelay, self._data[i]])
        list.sort(key=lambda x: x[0], reverse=True)
        return list

    def sortedrents(self, index, func):
        return self._data.sort(index,func)

    def filter(self, param,cond):
        list =[]
        for i in self._data:
            if cond(i.get_id(),param):
                list.append(i)
        return list

    def removeRent(self, index):
        if index < 0 or index >= len(self._data):
            raise RepositoryException("Invalid element position")
        return self._data.remove(index)

    def getRent(self):
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
