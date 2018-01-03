import time
import datetime


class BaseNumb():
    def __init__(self):
        '''
        We have a list for each of the items we need

        '''
        self.books = []
        self.clients = []
        self.rents = []

    def addBook(self, list):
        '''
        Adds a book class type to the book list
        '''
        self.books.append(list)

    def addClient(self, list):
        '''
        Adds a client class type to a client list
        '''
        self.clients.append(list)


    def addRent(self, list):
        '''
        Adds a rent class type to a rent list
        '''
        self.rents.append(list)

    def updateBook(self, list, oldId):
        '''
        Updates a book by removing the old one and adding the updated one
        '''
        self.removeBook(self.findIdBook(oldId))
        self.addBook(list)

    def updateClient(self, list, oldId):
        '''
        Updates a client by removing the old one and adding the updated one
        '''
        self.removeClient(self.findIdClient(oldId))
        self.addClient(list)

    def findIdBook(self, id):
        '''
        Find id of the book,get_id() is getting the id from the book class
        '''
        for i in range(0, len(self.books)):
            if id == int(self.books[i].get_id()):
                return i
        return -1

    def findIdClient(self, id):
        for i in range(0,len(self.clients)):
            if id == int(self.clients[i].get_id()):
                return i
        return -1

    def findIdRentBook(self,id):
        for i in range(0,len(self.rents)):
            if id == int(self.rents[i].get_bookId()):
                return i
        return -1

    def findIdRent(self, id):
        for i in range(0,len(self.rents)):
            if id == int(self.rents[i].get_id()):
                return i
        return -1

    def updateRent(self,rentId):
        today = time.strftime("%d/%m/%Y").split('/')
        self.rents[rentId].modifyReturn(datetime.date(int(today[2]),int(today[1]),int(today[0])))

    def searchBook(self,val):
        val = val.upper()
        list = []
        for j in range(0,len(self.books)):
            search = self.books[j].getUpper()
            i = 0
            ok = True
            while i < len(search) + 1 and ok == True:
                if search[i:i+len(val)] == val:
                    list.append(str(self.books[j]))
                    ok = False
                i+=1
        return list

    def searchClient(self,val):
        val = val.upper()
        list = []
        for j in range(0,len(self.clients)):
            search = self.clients[j].getUpper()
            i = 0
            ok = True
            while i < len(search) + 1 and ok == True:
                if search[i:i+len(val)] == val:
                    list.append(str(self.clients[j]))
                    ok = False
                i+=1
        return list

    def statBook(self,case):
        listNm = []
        listTi = []
        for i in range(0,len(self.books)):
            bo = int(self.books[i].get_id())
            nm = 0
            days = 0
            for j in range(0,len(self.rents)):
                if bo == self.rents[j].get_bookId():
                    nm +=1
                    d1 = self.rents[j].getRent()
                    d2 = self.rents[j].getRet()
                    if d2 == 0 or d2 == '0':
                        today = time.strftime("%d/%m/%Y").split('/')
                        d2 = datetime.date(int(today[2]),int(today[1]),int(today[0]))
                    days += abs((d2-d1).days)
            listNm.append([nm,self.books[i]])
            listTi.append([days,self.books[i]])
        if case == '1':
            listNm.sort(key=lambda x:x[0] ,reverse=True)
            return listNm
        else:
            listTi.sort(key=lambda x:x[0] ,reverse=True)
            return listTi

    def statClient(self):
        list = []
        for i in range(0,len(self.clients)):
            cli = int(self.clients[i].get_id())
            days = 0
            for j in range(0, len(self.rents)):
                if cli == self.rents[j].get_client():
                    d1 = self.rents[j].getRent()
                    d2 = self.rents[j].getRet()
                    if d2 == 0 or d2 == '0':
                        today = time.strftime("%d/%m/%Y").split('/')
                        d2 = datetime.date(int(today[2]), int(today[1]), int(today[0]))
                    days += abs((d2 - d1).days)
            list.append([days, self.clients[i]])
        list.sort(key=lambda x: x[0], reverse=True)
        return list

    def statAuthor(self):
        map = {}
        for i in range(0,len(self.rents)):
            id = self.rents[i].get_bookId()
            t = self.findIdBook(id)
            author = self.books[t].get_author()
            if author in map:
                map[author][0]+=1
            else:
                map[author] = [1]
        map_sor=sorted(map.items(),key = lambda x:x[1],reverse=True)
        return map_sor

    def statRents(self):
        list = []
        for i in range(0, len(self.rents)):
            d1 = self.rents[i].getDue()
            d2 = self.rents[i].getRet()
            if d2 == 0:
                today = time.strftime("%d/%m/%Y").split('/')
                d2 = datetime.date(int(today[2]), int(today[1]), int(today[0]))
                if d1 < d2:
                    rentdelay = abs((d2 - d1).days)
                    list.append([rentdelay,self.rents[i]])
        list.sort(key=lambda x: x[0], reverse=True)
        return list

    def removeRent(self, index):
        if index < 0 or index >= len(self.rents):
            raise RepositoryException("Invalid element position")
        return self.books.pop(index)

    def removeBook(self, index):
        if index < 0 or index >= len(self.books):
            raise RepositoryException("Invalid element position")
        return self.books.pop(index)

    def removeClient(self, index):
        if index < 0 or index >= len(self.clients):
            raise RepositoryException("Invalid element position")
        return self.clients.pop(index)

    def getBook(self):
        '''
        returns all the books
        '''
        return self.books

    def getClient(self):
        return self.clients

    def getRent(self):
        return self.rents


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
