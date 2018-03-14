class book:
    def __init__(self, id, title, desc, author):
        self.id = id
        self.title = title
        self.desc = desc
        self.author = author

    def __str__(self):
        r = ''
        r += "Id: " + str(self.id) + "\nTitle: " + str(self.title) + "\nDescription: " + str(
            self.desc) + "\nAuthor: " + str(self.author)
        return r

    def get_id(self):
        return self.id

    def get_author(self):
        return self.author

    def get_all(self):
        return [self.id,self.title,self.desc,self.author]

    def get_title(self):
        return str(self.title)

    def get_desc(self):
        return self.desc

    def getUpper(self):
        r = str(self.id).upper()+ "-" + str(self.title).upper() + "-" + str(self.desc).upper() + "-" + str(self.author).upper() + "-"
        return r

