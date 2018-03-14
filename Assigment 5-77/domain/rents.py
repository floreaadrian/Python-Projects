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

    def get_client(self):
        return self.client_id

    def get_id(self):
        return self.rent_id

    def getRet(self):
        return self.ret_date

    def getRent(self):
        return self.rent_date

    def getDue(self):
        return self.due_date

    def setBookId(self,new_id):
        self.book_id = new_id

    def get_all(self):
        return [self.rent_id, self.book_id, self.client_id, self.rent_date, self.due_date, self.ret_date]

    def modifyReturn(self,new):
        self.ret_date = new

    def __str__(self):
        r = ''
        r += "Rent id: " + str(self.rent_id) + "\nBook id: " + str(self.book_id) + "\nClient id: " + str(self.client_id) \
             +"\nRent date: " + str(self.rent_date) + "\nDue date: " + str(self.due_date) + "\nReturned date: " + str(
            self.ret_date)
        return r