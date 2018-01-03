
from Keys import getCode
from functions import *

def printMenu():
    print("These are the commands that you can make: ")
    print("Please write the number of the command you want to make")
    print("     1.Add a flight: <code>,<duration>,<departure_city>,<destination_city>")
    print("     2.Delete a flight: <code>")
    print("     3.Show all flights from a departure city sorted increasing by their destination city: <departure_city>")
    print("     4.Delay from a given departure city by some minutes: <departure_city>,<delay_duration>")
    print("     5.Print all the flights")
    print("     0.Exit")



def do():
    flights = []
    initial(flights)
    tests(flights)
    while True:
        printMenu()
        case = input(">> ")
        if case == '1':
            case_1(flights,case_1in(flights))
        elif case == '2':
            ok= True
            code = 0
            while ok:
                code = input("The code of the flight that you want to remove: ")
                if searchCode(code,flights) == True:
                    print("We don't have that flight!")
                else:
                    ok= False
            delete(code,flights)
        elif case == '3':
            dept_city = input("Departure city: ")
            show_dept(dept_city,flights)
        elif case == '4':
            delay,dept_city = readDelay()
            flights = addDelay(delay,dept_city,flights)
        elif case == '5':
            for i in flights:
                print("Code: ", i[getCode()], "\nDuration: ", i[getDur()],"\nDeparture city: ",i[getDept()], "\nDestination city: ", i[getDest()])
        elif case == '0':
            print("Goodbye...")
            break
        else:
            print("Invalid input!")


do()