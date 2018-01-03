class repos():
    def __init__(self):
        self.__data = []

    def addItem(self,list):
        self.__data.append(list)

    def removeItem(self, index):
        if index < 0 or index >= len(self.__data):
            raise RepositoryException("Invalid element position")
        return self.__data.pop(index)

    def getAll(self):
        return self.__data

class RepositoryException(Exception):

    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message
