from Repository.bookRepCSV import bookCSVFileRepository
from Repository.clientRepCSV import clientCSVFileRepository
from Repository.rentRepCSV import rentCSVFileRepository

from controller.bookController import BookControl
from controller.clientController import ClientControl
from controller.rentController import RentControl
from controller.UndoController import UndoController

from Repository.clientPickleFileRepository import PickleFileclientRep
from Repository.bookPickleFileclientRep import PickleFilebookRep
from Repository.rentPickleFileclientRep import PickleFilerentRep
from Repository.test_rentRep import TestRentRep

'''
from domain.clients import client
from domain.books import book
from domain.rents import rent
'''
from ui.menu import UI

SETTINGS_FILE = "settings_text.properties"


# SETTINGS_FILE = "settings_binary.properties"

def readSettings():
    '''
    Reads the program's settings file
    output:
        A dictionary containing the program settings
    '''
    f = open(SETTINGS_FILE, "r")
    lines = f.read().split("\n")
    settings = {}

    for line in lines:
        setting = line.split("=")
        if len(setting) > 1:
            settings[setting[0]] = setting[1]
    f.close()
    return settings


settings = readSettings()

bookR = None
clientR = None
rentR = None

if 'CSV' == settings['repository']:
    bookR = bookCSVFileRepository(settings['books'])
    clientR = clientCSVFileRepository(settings['clients'])
    rentR = rentCSVFileRepository(settings['rentals'])

if 'binary' == settings['repository']:
    bookR = PickleFilebookRep(settings['books'])
    clientR = PickleFileclientRep(settings['clients'])
    rentR = PickleFilerentRep(settings['rentals'])

undoController = UndoController()
ctrlR = RentControl(rentR, undoController)
ctrlC = ClientControl(clientR, undoController, ctrlR)
ctrlB = BookControl(bookR, undoController, ctrlR)

uiS = UI(ctrlB, ctrlC, ctrlR, undoController)

uiS.mainMenu()
