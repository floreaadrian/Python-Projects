
import datetime
from Repository.rentRep import rentRep
from domain.rents import rent
from Repository.RepositoryException import RepositoryException

class rentCSVFileRepository(rentRep):
    def __init__(self, fileName="cars.txt"):
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

    def statRents(self):
        return rentRep.statRents(self)

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                rent_date = attrs[3].split('-')
                due_date = attrs[4].split('-')
                ret_date = attrs[5]
                if ret_date != '0':
                    ret_date = ret_date.split('-')
                    ret_date = datetime.date(int(ret_date[0]), int(ret_date[1]), int(ret_date[2]))
                rent_date = datetime.date(int(rent_date[0]), int(rent_date[1]), int(rent_date[2]))
                due_date = datetime.date(int(due_date[0]), int(due_date[1]), int(due_date[2]))
                rents = rent(int(attrs[0]),int(attrs[1]),int(attrs[2]),rent_date,due_date,ret_date)
                rentRep.addRent(self, rents)
                line = f.readline().strip()
        except IOError:
            raise RepositoryException("Error saving file")
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        rents = rentRep.getRent(self)
        for ret in rents:
            strf = str(ret.get_id()) + "," + str(ret.get_bookId()) + "," + str(ret.get_client()) + ","\
                   + str(ret.getRent()) + "," + str(ret.getDue()) + "," + str(ret.getRet()) + "\n"
            f.write(strf)
        f.close()
