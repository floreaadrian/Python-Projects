class clasaparental:
    def __init__(self):
        self._data=[]

    def add(self,obj):
        self._data.append(obj)

    def getAll(self):
        return self._data
