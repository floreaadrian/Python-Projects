from rep.driverRep import driversRep
from domain.driver import drivers

class driverCSVFileRepository(driversRep):
    def __init__(self, fileName="driver.txt"):
        driversRep.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                driv = drivers(int(attrs[0]),attrs[1])
                driversRep.addDriver(self, driv)
                line = f.readline().strip()
        except IOError:
            print("Error saving file")
        finally:
            f.close()
