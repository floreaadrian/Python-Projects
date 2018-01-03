from domain.order import orders

class menu:

    def __init__(self,driverC,orderC):
        self._driverC = driverC
        self._orderC = orderC

    def mainManu(self):
        st = "Hello!\n"
        st += "\t1.Add an order int the system.\n"
        st += "\t2.Display all orders.\n"
        st += "\t3.Compute the income of a driver by their given ID.\n"
        st += "\t-1.Help.\n"
        st += "\t0.Exit"
        print(st)
        while True:
            cmd = input(">> ")
            if cmd == '1':
                '''
                    We will read until the input is good
                '''
                ok = False
                driverId = 0
                km = 0
                flag = True #flag is for us to verify if the input is int
                while ok == False:
                    try:
                        driverId = int(input("The driver id: "))
                    except ValueError:
                        print("Id must be an int")
                        flag = False
                    if self._driverC.findId(driverId) == False:
                        #We search if we find the id of the driver
                        print("We don't have that driver")
                        ok = False
                    elif flag == True:
                        ok = True
                ok = False
                while ok == False:
                    try:
                        km = int(input("The km: "))
                    except ValueError:
                        print("Km must be int!")
                    if km < 1:
                        print("The distance travelled must be at least 1")
                    else:
                        ok = True
                self._orderC.addOrder(orders(driverId,km))
            elif cmd == '2':
                for i in self._orderC.getAll():
                    print(str(i))
                    print(10*"-")
            elif cmd == '3':
                ok = False
                flag = True
                driverId = 0
                while ok == False:
                    try:
                        driverId = int(input("The driver id: "))
                    except ValueError:
                        print("Id must be an int")
                        flag = False
                    if self._driverC.findId(driverId) == False:
                        print("We don't have that driver")
                        ok = False
                    elif flag == True:
                        ok = True
                print("The driver income is: "+str(self._orderC.calculate(driverId))+" RON")
            elif cmd == '-1':
                print(st)
            elif cmd == '0':
                print("bye...")
                return
            else:
                print("Invalid command")

    @staticmethod
    def readDriverId():
        driverId = 0
        try:
            driverId = int(input("The driver id: "))
        except ValueError:
            print("Id must be an int")
        finally:
            return driverId