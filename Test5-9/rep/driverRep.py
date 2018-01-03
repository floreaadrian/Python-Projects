
class driversRep:
    def __init__(self):
        '''
        We initialize the array in which we store the data
        self._data is all the drivers
        '''
        self._data = []

    def addDriver(self, driver):
        self._data.append(driver)


    def findId(self, id):
        '''
        This function returns True if we found the id of the driver,otherwise returns False
        :param id: an int value which is the id of the driver
        :return:
        '''
        for i in self._data:
            if i.get_id() == id:
                return True
        return False
