from Repository.rentRep import rentRep
import time
import datetime


class bookRep():
    def __init__(self):
        '''
        We have a list for each of the items we need
        '''
        self._data = []
        self._control = rentRep()

    def addBook(self, list):
        '''
        Adds a book class type to the book list
        '''
        self._data.append(list)

    def retId(self, id):
        return self._data[id]

    def __len__(self):
        return len(self._data)

    def updateBook(self, list, oldId):
        '''
        Updates a book by removing the old one and adding the updated one
        '''
        self.removeBook(self.findIdBook(oldId))
        self.addBook(list)

    def findIdBook(self, id):
        '''
        Find id of the book,get_id() is getting the id from the book class
        '''
        for i in range(0, len(self._data)):
            if id == int(self._data[i].get_id()):
                return i
        return -1

    def searchBook(self, val):
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

    def statBook(self, case, con):
        listNm = []
        listTi = []
        for i in range(0, len(self._data)):
            bo = int(self._data[i].get_id())
            nm = 0
            days = 0
            rents = con.listId()
            for j in range(0, len(rents)):
                if bo == rents[j][1]:
                    nm += 1
                    d1 = rents[j][3]
                    d2 = rents[j][5]
                    if d2 == 0 or d2 == '0':
                        today = time.strftime("%d/%m/%Y").split('/')
                        d2 = datetime.date(int(today[2]), int(today[1]), int(today[0]))
                    days += abs((d2 - d1).days)
            listNm.append([nm, self._data[i]])
            listTi.append([days, self._data[i]])
        if case == '1':
            listNm.sort(key=lambda x: x[0], reverse=True)
            return listNm
        else:
            listTi.sort(key=lambda x: x[0], reverse=True)
            return listTi

    def statAuthor(self, con):
        map = {}
        rents = con.listId()
        for i in range(0, len(rents)):
            id = rents[i][1]
            t = self.findIdBook(id)
            author = self._data[t].get_author()
            if author in map:
                map[author][0] += 1
            else:
                map[author] = [1]
        map_sor = sorted(map.items(), key=lambda x: x[1], reverse=True)
        return map_sor

    def sortedbooks(self, index, func):
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

    def removeBook(self, index):
        if index < 0 or index >= len(self._data):
            raise RepositoryException("Invalid element position")
        return self._data.pop(index)

    def getBook(self):
        '''
        returns all the _data
        '''
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
