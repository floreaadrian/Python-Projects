
from Repository.bookRep import bookRep
from domain.books import book
from Repository.RepositoryException import RepositoryException

class bookCSVFileRepository(bookRep):
    def __init__(self, fileName="cars.txt"):
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
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                books = book(int(attrs[0]),attrs[1],attrs[2],attrs[3])
                bookRep.addBook(self, books)
                line = f.readline().strip()
        except IOError:
            raise RepositoryException("Error saving file")
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        books = bookRep.getBook(self)
        for bk in books:
            strf = str(bk.get_id()) + "," + bk.get_title() + "," + str(bk.get_desc()) + "," + str(bk.get_author()) + "\n"
            f.write(strf)
        f.close()
