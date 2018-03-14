class iterabil:
    def __init__(self):
        self._data=[]
        self.index = len(self._data)

    def __setitem__(self,key,item):
        self._data[key]=item

    def __delitem__(self,key):
        self._data.remove(key)


    def __iter__(self):
        self._iterPoz = 0
        return self


    def __next__(self):
        if self._iterPoz >= len(self._data):
            raise StopIteration()
        rez = self._data[self._iterPoz]
        self._iterPoz = self._iterPoz + 1
        return rez

    def __getitem__(self, item):
        return self._data[item]

    def remove(self,obj):
        self._data.pop(obj)

    def append(self,obj):
        self._data.append(obj)

    def __len__(self):
        return len(self._data)

    def sort(self, index, func):
        a = self._data
        i, j, size = 1, 2, len(a)
        while i < size:
            x, y = self._data[i].get_all(), self._data[i - 1].get_all()
            if func(y[index],x[index]):
                i, j = j, j + 1
            else:
                a[i - 1], a[i] = a[i], a[i - 1]
                i -= 1
                if i == 0:
                    i, j = j, j + 1
        return a
