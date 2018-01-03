from main import book,client,rent,test_Class
from firstop import ListControl
from baseOfNum import BaseNumb

from menu import UI

base = BaseNumb()

test_Class()

import datetime
t1 = datetime.date(2017, 2, 3)
t2 = datetime.date(2017, 2, 23)
t3 = datetime.date(2017, 5, 23)
t4 = datetime.date(2017, 9, 2)
t5 = datetime.date(2017, 10, 23)
t6 = datetime.date(2017, 11, 23)
t7 = datetime.date(2017, 11, 28)
t8 = datetime.date(2017, 9, 20)
t9 = datetime.date(2017, 10, 10)


base.addBook(book(54,"Oribitor","Best","Mircea Cartarescu"))
base.addClient(client(43,"Florea Adrian"))
base.addRent(rent(1,3,43,t1,t1,0))
base.addBook(book(43,"Solenoid","Favorite","Mircea Cartarescu"))
base.addClient(client(9,"Mihai Adrian"))
base.addRent(rent(2,9,23,t2,t2,0))
base.addBook(book(654,"Travesti","Weird but awesome","Mircea Cartarescu"))
base.addClient(client(12,"Cristian Luci"))
base.addRent(rent(3,99,43,t3,t3,0))
base.addBook(book(99,"Nostalgia","Early","Mircea Cartarescu"))
base.addClient(client(23,"Tudor Ioan"))
base.addRent(rent(7,99,43,t4,t5,0))
base.addRent(rent(8,99,43,t4,t5,0))
base.addRent(rent(13,23,43,t4,t5,0))
base.addRent(rent(9,99,43,t4,t5,0))
base.addBook(book(23,"Colectionarul","Another Favorite","John Fowles"))
base.addBook(book(542,"Colectionarul","Another Favorite","Florin Iaru"))
base.addClient(client(64,"Marcel Dorel"))
base.addRent(rent(10,542,64,t4,t7,0))
base.addRent(rent(11,542,64,t4,t7,0))
base.addRent(rent(12,542,64,t4,t9,0))
base.addBook(book(32,"Solenoid","Best","Mircea Cartarescu"))
base.addBook(book(3423,"Solenoid","Best","Mircea Cartarescu"))
base.addClient(client(76,"Radu Hitic"))
base.addRent(rent(6,3,43,t8,t6,0))

ctrl = ListControl(base)

ui = UI(ctrl)

ui.mainMenu()