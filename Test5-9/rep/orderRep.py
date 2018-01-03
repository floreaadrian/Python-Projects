from domain.order import orders


class ordersRep:
    def __init__(self):
        '''
        We initialize the array in which we store the data
        self._data is all the orders
        '''
        self._data = []

    def addOrder(self, order):
        '''
        We append to the self._data an order
        :param order: is an object given by the order class
        '''
        self._data.append(order)

    def calculate(self, id):
        '''
        We calculate the income by multiplaing the driver km and adding it to the sum
        :param id: the id of the driver we need to calculate the income
        :return:
        '''
        sum = 0
        for i in self._data:
            '''
            We go trough the data with i and verify if the order is from the driver we need to calculate income
            '''
            if i.get_driver() == id:
                sum += 2.5 * i.get_km()

        return sum

    def getAll(self):
        return self._data