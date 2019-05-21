from domain import Product, writeToFile
from datetime import date


def readerFromFile(file):
    produse = []
    try:
        f = open(file, "r")
        line = f.readline().split('|||')
        while len(line) != 1:
            if len(line) == 4:
                k = Product(line[0], line[1], line[2], int(line[3]))
                produse.append(k)
            line = f.readline().split('|||')
        f.close()
    except IOError:
        print("Off")
    return produse


def times():
    f = open("times.txt", "r")
    dates = []
    line = f.readline().split(",")
    f.close()
    f = open("times.txt", "w")
    st = str(date.today()) + ".csv"
    line.append(st)
    st = ",".join(line)
    f.write(st)
    f.close()
    return dates

def run():
    ps4File = "top/ps4/"+str(date.today())+".csv"
    xboxFile = "top/xbox/"+str(date.today())+".csv"
    ps4FileA = "all/ps4/"+str(date.today())+".csv"
    xboxFileA = "all/xbox/"+str(date.today())+".csv"
    ps4 = readerFromFile(ps4FileA)
    print(ps4FileA)
    xbox = readerFromFile(xboxFileA)
    ps4O = readerFromFile(ps4FileA)
    xboxO = readerFromFile(xboxFileA)
    ps4.sort(key=lambda x: x.price)
    xbox.sort(key=lambda x: x.price)
    xboxList = ""
    ps4List = ""
    for i in range(3):
        k = '|||'.join(ps4[i].toList())
        k += '\n'
        ps4List += k
        k = '|||'.join(xbox[i].toList())
        k += '\n'
        xboxList += k
    print(ps4File)
    writeToFile(ps4File, ps4List)
    writeToFile(xboxFile, xboxList)
    times()

run()

def getData():
    return ps4
