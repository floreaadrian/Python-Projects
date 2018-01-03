class client:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        r = ''
        r += "Id: " + str(self.id) + "\nName: " + str(self.name)
        return r

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_all(self):
        return [self.id,self.name]

    def getUpper(self):
        r = str(self.id).upper() + "-" + str(self.name).upper()
        return r
