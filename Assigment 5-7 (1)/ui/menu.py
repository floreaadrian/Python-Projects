from domain.books import book
from domain.clients import client
from domain.rents import rent

import time
import datetime


def increasing(x, y):
    return x <= y


def decreasing(x, y):
    return x >= y


def equal(x, y):
    return x == y


class UI:
    def __init__(self, bookC, clientC, rentC, undoC):
        self.bookC = bookC
        self.clientC = clientC
        self.rentC = rentC
        self.undoC = undoC

    @staticmethod
    def printMenu():
        string = '\nAvailable commands:\n'
        string += '\t 1 - Add book\n'
        string += '\t 2 - Add client\n'
        string += '\t 3 - Update a book by id\n'
        string += '\t 4 - Update a client by id\n'
        string += '\t 5 - Remove a book by id\n'
        string += '\t 6 - Remove a client by id\n'
        string += '\t 7 - List clients\n'
        string += '\t 8 - List books\n'
        string += '\t 9 - Rent a book by id\n'
        string += '\t 10 - Return a book\n'
        string += '\t 11 - Print the rent list\n'
        string += '\t 12 - Search a book\n'
        string += '\t 13 - Search a client\n'
        string += '\t 14 - Statistic about most rented book\n'
        string += '\t 15 - Statistic about the most active client\n'
        string += '\t 16 - Statistic about most rented author\n'
        string += '\t 17 - Statistic about late rentals\n'
        string += '\t 18 - Sort\n'
        string += '\t 19 - Filter\n'
        string += '\t 20 - Undo\n'
        string += '\t 21 - Redo\n'
        string += '\t -1 - Help\n'
        string += '\t 0 - Exit\n'
        print(string)

    def mainMenu(self):
        UI.printMenu()
        while True:
            command = input(">> ").strip()
            if command == '0':
                print("exit...")
                break
            elif command == '1':
                ok = True
                id = 0
                while ok:
                    try:
                        id = int(input("Id: "))
                        if self.bookC.findIdBook(id) != -1:
                            print("We already have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                z = UI.readBook(id)
                self.bookC.addBook(z)
            elif command == '2':
                ok = True
                id = 0
                while ok:
                    try:
                        id = int(input("Id: "))
                        if self.clientC.findIdClient(id) != -1:
                            print("We already have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                z = UI.readClient(id)
                self.clientC.addClient(z, True)
            elif command == '3':
                ok = True
                old_id = 0
                while ok:
                    try:
                        old_id = int(input("The old id: "))
                        if self.bookC.findIdBook(old_id) == -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                z = UI.readUpBook(old_id)
                self.bookC.updateBook(z, old_id)
            elif command == '4':
                ok = True
                old_id = 0
                while ok:
                    try:
                        old_id = int(input("Id: "))
                        if self.clientC.findIdClient(old_id) == -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                z = UI.readUpClient(old_id)
                self.clientC.updateClient(z, old_id)
            elif command == '5':
                id = 0
                ok = True
                while ok:
                    try:
                        id = int(input("The id of the deleted element: "))
                        if self.bookC.findIdBook(id) == -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                self.bookC.removeBook(id)
            elif command == '6':
                id = 0
                ok = True
                while ok:
                    try:
                        id = int(input("The id of the deleted element: "))
                        if self.clientC.findIdClient(id) == -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                self.clientC.removeClient(id, True)
            elif command == '7':
                if len(self.clientC.getClient()) == 0:
                    print("We don't have any client!")
                for n in self.clientC.getClient():
                    print(str(n))
                    print("- " * 10)
            elif command == '8':
                if len(self.bookC.getBook()) == 0:
                    print("We don't have any book available!")
                for n in self.bookC.getBook():
                    print(str(n))
                    print("- " * 10)
            elif command == '9':
                clientId = 0
                ok = True
                id = 0
                while ok:
                    try:
                        clientId = int(input("Your id: "))
                        if self.clientC.findIdClient(clientId) == -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                ok = True
                while ok:
                    try:
                        id = int(input("The id of the book you want to rent: "))
                        if self.bookC.findIdBook(id) == -1:
                            print("We don't have that book!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                z = UI.readRent(id, clientId)
                ln = len(self.rentC.getRent())
                today = time.strftime("%d/%m/%Y").split('/')
                d2 = datetime.date(int(today[2]), int(today[1]), int(today[0]))
                k = rent(ln + 1, z[0], z[1], d2, datetime.date(z[4], z[3], z[2]), 0)
                self.rentC.addRent(k)
            elif command == '10':
                ok = True
                id = 0
                rentId = 0
                while ok:
                    try:
                        id = int(input("Book id: "))
                        rentId = self.rentC.findIdRentBook(id)
                        if rentId == -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                today = time.strftime("%d/%m/%Y")
                self.rentC.updateRent(rentId, today)
            elif command == '11':
                if len(self.rentC.getRent()) == 0:
                    print("We don't have any rents!")
                for n in self.rentC.getRent():
                    print(str(n))
                    print("- " * 10)
            elif command == '12':
                val = input("What do you want: ")
                list = self.bookC.searchBook(val)
                for i in list:
                    print(i)
                    print("- " * 10)
            elif command == '13':
                val = input("What do you want: ")
                list = self.clientC.searchClient(val)
                for i in list:
                    print(i)
                    print("- " * 10)
            elif command == '14':
                case = 0
                while True:
                    print("1.Print by number of times rented")
                    print("2.Print by number of days rented")
                    case = input()
                    if case != '1' and case != '2':
                        print("Invalid input!")
                    else:
                        break
                list = self.bookC.statBook(case, self.rentC)
                for i in list:
                    print(str(i[1]))
                    if case == '1':
                        print("For", i[0], "times")
                    else:
                        print("For", i[0], "days")
                    print("- " * 10)
            elif command == '15':
                list = self.clientC.statClient(self.rentC)
                for i in list:
                    print(str(i[1]))
                    print(">> Have", i[0], "of days in which they have rented books")
            elif command == '16':
                list = self.bookC.statAuthor(self.rentC)
                for key in list:
                    print(key[0], "was rented", key[1], "times")
            elif command == '17':
                list = self.rentC.statRents()
                for i in list:
                    print(str(i[1]))
                    print(">> Is late by", i[0], "days")
                    print("- " * 10)
            elif command == '18':
                self.sort()
            elif command == '19':
                pass
            elif command == '20':
                self.undoC.undo()
            elif command == '21':
                self.undoC.redo()
            elif command == '-1':
                UI.printMenu()
            else:
                print("Invalid command")

    def sort(self):
        st = "Chose one: \n"
        st += "\t1.Sort books\n"
        st += "\t2.Sort clients\n"
        st += "\t3.Sort rents"
        print(st)
        n = 0
        try:
            n = int(input(">> "))
        except ValueError:
            print("Invalid input!")
        if n == 1:
            st = "Chose one: \n"
            st += "\t1.Sort by book id\n"
            st += "\t2.Sort by book name\n"
            st += "\t3.Sort by author name"
            n = 0
            print(st)
            try:
                n = int(input(">> "))
            except ValueError:
                print("Invalid input!")
            if n == 1 or n == 2:
                print("\t1.Incrasing")
                print("\t2.Decreasing")
                k = 0
                try:
                    k = int(input(">> "))
                except ValueError:
                    print("Invalid input!")

                if k == 1:
                    a = self.bookC.sortedbooks(n - 1, increasing)
                    for n in a:
                        print(str(n))
                        print("- " * 10)
                elif k == 2:
                    a = self.bookC.sortedbooks(n - 1, decreasing)
                    for n in a:
                        print(str(n))
                        print("- " * 10)
                else:
                    print("Invalid input!")
            elif n == 3:
                print("\t1.Incrasing")
                print("\t2.Decreasing")
                k = 0
                try:
                    k = int(input(">> "))
                except ValueError:
                    print("Invalid input!")
                if k == 1:
                    a = self.bookC.sortedbooks(n, increasing)
                    for n in a:
                        print(str(n))
                        print("- " * 10)
                elif k == 2:
                    a = self.bookC.sortedbooks(n, decreasing)
                    for n in a:
                        print(str(n))
                        print("- " * 10)
            else:
                print("Invalid input!")
        elif n == 2:
            st = "Chose one: \n"
            st += "\t1.Sort by client id\n"
            st += "\t2.Sort by client name"
            n = 0
            print(st)
            try:
                n = int(input(">> "))
            except ValueError:
                print("Invalid input!")
            if n == 1 or n == 2:
                print("\t1.Incrasing")
                print("\t2.Decreasing")
                k = 0
                try:
                    k = int(input(">> "))
                except ValueError:
                    print("Invalid input!")
                if k == 1:
                    a = self.clientC.sortedclients(n - 1, increasing)
                    for n in a:
                        print(str(n))
                        print("- " * 10)
                elif k == 2:
                    a = self.clientC.sortedclients(n - 1, decreasing)
                    for n in a:
                        print(str(n))
                        print("- " * 10)
            else:
                print("Invalid input!")
        elif n == 3:
            st = "Chose one: \n"
            st += "\t1.Sort by rent id\n"
            st += "\t2.Sort by book id\n"
            st += "\t3.Sort by client id"
            n = 0
            print(st)
            try:
                n = int(input(">> "))
            except ValueError:
                print("Invalid input!")
            if n < 1 and n > 3:
                print("Invalid input!")
            else:
                print("\t1.Incrasing")
                print("\t2.Decreasing")
                k = 0
                try:
                    k = int(input(">> "))
                except ValueError:
                    print("Invalid input!")
                if k == 1:
                    a = self.rentC.sortedrents(n - 1, increasing)
                    for n in a:
                        print(str(n))
                        print("- " * 10)
                elif k == 2:
                    a = self.rentC.sortedrents(n - 1, decreasing)
                    for n in a:
                        print(str(n))
                        print("- " * 10)
        else:
            print("Invalid input! ")

    @staticmethod
    def readBook(id):
        title = input("Title = ")
        desc = input("Description = ")
        auth = input("Author = ")
        return book(id, title, desc, auth)

    @staticmethod
    def readClient(id):
        name = input("Name = ")
        return client(id, name)

    @staticmethod
    def readUpBook(id):
        while True:
            title = input("New title = ")
            desc = input("New description = ")
            auth = input("New author = ")
            return book(id, title, desc, auth)

    @staticmethod
    def readUpClient(id):
        while True:
            name = input("New name = ")
            return client(id, name)

    @staticmethod
    def readRent(id, clientId):
        print("Please say until you want this book")
        cal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        while True:
            try:
                val = input("Please give me a date in this format: dd-mm-yyyy: ")
                val = val.split('-')
                day = int(val[0])
                month = int(val[1])
                year = int(val[2])
                today = time.strftime("%d/%m/%Y").split('/')
                if month > 12 or month < 1:
                    print("Invalid input!")
                elif cal[month] < day:
                    print("Invalid input!")
                elif datetime.date(year, month, day) < datetime.date(int(today[2]), int(today[1]), int(today[0])):
                    print("Invalid input!")
                else:
                    return (id, clientId, day, month, year)
            except ValueError:
                print("Invalid input!")
