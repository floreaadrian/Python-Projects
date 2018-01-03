from Repository import repos
from classes import book,client
from Controller import control

class UI:
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
        string += '\t 12 - Help\n'
        string += '\t 0 - Exit\n'
        print(string)


    def mainMenu(self):
        UI.printMenu()
        bookR=repos()
        clientR=repos()
        rentR=repos()
        conBook=control(bookR)
        conRent=control(rentR)
        conClient=control(clientR)
        while True:
            command = input(">> ").strip()
            if command == '0':
                print("exit...")
                break
            elif command == '1':
                id = int(input("Id: "))
                z = UI.readBook(id)
                conBook.addItem(z)
            elif command == '2':
                id=0
                z = UI.readClient(id)
                conClient.addItem(z)
            elif command == '3':
                conBook.updateBook()
            elif command == '4':
                conClient.updateBook()
            elif command == '7':
                for n in conClient.getAll():
                    print(str(n))
            elif command == '8':
                for n in conBook.getAll():
                    print(str(n))
            elif command == '9':
                z = UI.readRent(0,0)
                conRent.addItem(z)

    @staticmethod
    def readRent(id, clientId):
        print("Please say until when,next year, you want this book")
        cal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        while True:
            month = 0
            day = 0
            try:
                ok = True
                while ok:
                    month = int(input("Month: "))
                    if month <= 0 or month > 12:
                        print("Invalid month!")
                    else:
                        ok = False
                ok = True
                while ok:
                    day = int(input("Day: "))
                    if day > cal[month - 1] or day <= 0:
                        print("Invalid day")
                    else:
                        ok = False
            except ValueError:
                print("Invalid input!")
            return (id, clientId, month, day)

    @staticmethod
    def readClient(id):
        name = input("Name = ")
        return client(id, name)

    @staticmethod
    def readBook(id):
        while True:
            title = input("New title = ")
            desc = input("New description = ")
            auth = input("New author = ")
            return book(id, title, desc, auth)