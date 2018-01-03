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


class client:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        r = ''
        r += "Id: " + str(self.id) + "\nName: " + str(self.name)
        return r

    def get_id(self):
        return self.id


class rent:
    def __init__(self, rent_id, book_id, client_id, rent_date, due_date, ret_date):
        self.rent_id = rent_id
        self.book_id = book_id
        self.client_id = client_id
        self.rent_date = rent_date
        self.due_date = due_date
        self.ret_date = ret_date

    def get_bookId(self):
        return self.book_id

    def get_id(self):
        return self.rent_id

    def __str__(self):
        r = ''
        r += "Rent id: " + str(self.rent_id) + "\nBook id: " + str(self.book_id) + "\nClient id: " + str(self.client_id) \
             +"\nRent date: " + str(self.rent_date) + "\nDue date: " + str(self.due_date) + "\nReturned date: " + str(
            self.ret_date)
        return r


def test_Class():
    assert str(book(1,"Yb","A","Mo")) == "Id: 1\nTitle: Yb\nDescription: A\nAuthor: Mo"
    assert str(client(32,"K")) == "Id: 32\nName: K"
    assert client.get_id(client(454,"Na")) == 454
    assert rent.get_bookId(rent(43,23,98,"54","54","54")) ==  23