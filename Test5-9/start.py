from rep.driverRepFile import driverCSVFileRepository
from rep.orderRepFile import ordersCSVFileRepository

from controller.driverController import driverCon
from controller.orderController import orderCon

from ui.UI import menu

orderRep = ordersCSVFileRepository()
driverRep = driverCSVFileRepository()

orderC = orderCon(orderRep)
driverC = driverCon(driverRep)

uiS = menu(driverC, orderC)
uiS.mainManu()
