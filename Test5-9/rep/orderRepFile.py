from rep.orderRep import ordersRep
from domain.order import orders

class ordersCSVFileRepository(ordersRep):
    def __init__(self, fileName="orders.txt"):
        ordersRep.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                ords = orders(int(attrs[0]),int(attrs[1]))
                ordersRep.addOrder(self, ords)
                line = f.readline().strip()
        except IOError:
            print("Error saving file")
        finally:
            f.close()
