from main import book, client, rent
import time
import datetime

class UI:
    def __init__(self, controller):
        self._controller = controller

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
                        if self._controller.findIdBook(id) != -1:
                            print("We already have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                z = UI.readBook(id)
                self._controller.addBook(z)
            elif command == '2':
                ok = True
                id = 0
                while ok:
                    try:
                        id = int(input("Id: "))
                        if self._controller.findIdClient(id) != -1:
                            print("We already have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                z = UI.readClient(id)
                self._controller.addClient(z)
            elif command == '3':
                ok = True
                old_id = 0
                while ok:
                    try:
                        old_id = int(input("The old id: "))
                        if self._controller.findIdBook(old_id) == -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                z = UI.readUpBook(old_id)
                self._controller.updateBook(z, old_id)
            elif command == '4':
                ok = True
                old_id = 0
                while ok:
                    try:
                        old_id = int(input("The old id: "))
                        if self._controller.findIdClient(old_id) == -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                z = UI.readUpClient(old_id)
                self._controller.updateClient(z, old_id)
            elif command == '5':
                id = 0
                ok = True
                while ok:
                    try:
                        id = int(input("The id of the deleted element: "))
                        if self._controller.findIdBook(id) == -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                self._controller.removeBook(id)
            elif command == '6':
                id = 0
                ok = True
                while ok:
                    try:
                        id = int(input("The id of the deleted element: "))
                        if self._controller.findIdClient(id) == -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                self._controller.removeClient(id)
            elif command == '7':
                if len(self._controller.getClient()) == 0:
                    print("We don't have any client!")
                for n in self._controller.getClient():
                    print(str(n))
                    print("- " * 10)
            elif command == '8':
                if len(self._controller.getBook()) == 0:
                    print("We don't have any book available!")
                for n in self._controller.getBook():
                    print(str(n))
                    print("- " * 10)
            elif command == '9':
                clientId = 0
                ok = True
                id = 0
                while ok:
                    try:
                        clientId = int(input("Your id: "))
                        if self._controller.findIdClient(clientId) == -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                ok= True
                while ok:
                    try:
                        id = int(input("The id of the book you want to rent: "))
                        if self._controller.findIdBook(id) == -1:
                            print("We don't have that book!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                z = UI.readRent(id, clientId)
                ln = len(self._controller.getRent())
                today = time.strftime("%d/%m/%Y").split('/')
                d2 = datetime.date(int(today[2]),int(today[1]),int(today[0]))
                k = rent(ln+1, z[0], z[1], d2, datetime.date(z[4], z[3], z[2]),0)
                self._controller.addRent(k)
            elif command == '10':
                ok = True
                id = 0
                rentId = 0
                while ok:
                    try:
                        id = int(input("Book id: "))
                        rentId = self._controller.findIdRentBook(id)
                        if rentId== -1:
                            print("We don't have that id!")
                        else:
                            ok = False
                    except ValueError:
                        print("Id must be number!")
                self._controller.updateRent(rentId)
            elif command == '11':
                if len(self._controller.getRent()) == 0:
                    print("We don't have any rents!")
                for n in self._controller.getRent():
                    print(str(n))
                    print("- "*10)
            elif command == '12':
                val = input("What do you want: ")
                list = self._controller.searchBook(val)
                for i in list:
                    print(i)
                    print("- " * 10)
            elif command == '13':
                val = input("What do you want: ")
                list = self._controller.searchClient(val)
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
                list = self._controller.statBook(case)
                for i in list:
                    print(str(i[1]))
                    if case == '1':
                        print("For",i[0],"times")
                    else:
                        print("For", i[0], "days")
                    print("- " * 10)
            elif command == '15':
                list = self._controller.statClient()
                for i in list:
                    print(str(i[1]))
                    print(">> Have",i[0],"of days in which they have rented books")
            elif command == '16':
                list = self._controller.statAuthor()
                for key in list:
                    print(key[0],"was rented",key[1],"times")
            elif command == '17':
                list = self._controller.statRents()
                for i in list:
                    print(str(i[1]))
                    print(">> Is late by",i[0],"days")
            elif command == '-1':
                UI.printMenu()
            else:
                print("Invalid command")

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
            return client(id,name)

    @staticmethod
    def readRent(id, clientId):
        print("Please say until you want this book")
        cal = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
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
                elif datetime.date(year,month,day) < datetime.date(int(today[2]),int(today[1]),int(today[0])):
                    print("Invalid input!")
                else:
                    return (id, clientId, day,month,year)
            except ValueError:
                print("Invalid input!")
