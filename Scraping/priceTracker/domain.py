
# defining the product type


class Product:
    def __init__(self, tp, name, link, price):
        self.type = tp
        self.name = name
        self.link = link
        self.price = price

    def priceDifference(self, other):
        return self.price - other.price

    def toList(self):
        return [self.type, self.name, self.link, str(self.price)]

    def __str__(self):
        sr = self.type
        sr += "->" + self.name
        sr += " " + str(self.price)
        return sr


def writeToFile(file, data):
    try:
        f = open(file, "w")
        f.write(data)
        f.write("\n")
    except IOError:
        print("Off")
    finally:
        f.close()

def createSites(list1):
    k = []
    for line in list1:
        k.append("https://www.emag.ro/search/"+line)
        l = line.split()
        if(len(l)>1):
            line = "+".join(l)
        k.append("https://altex.ro/search/?q="+line)
    return k
