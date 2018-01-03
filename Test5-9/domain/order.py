class orders:

    def __init__(self,driver_id,km):
        self._driver_id = driver_id
        self._km = km

    def get_km(self):
        return self._km

    def get_driver(self):
        return self._driver_id

    def __str__(self):
        st = "The driver is: "+str(self._driver_id)+"\nDistance travelled is: "+str(self._km)
        return st
