class Book:
    def __init__(self, name, writer):
        self.name = name
        self.writer = writer
        self.status = True

    def issue(self):
        if self.status:
            self.status = False
            print(self.name, "issued")
        else:
            print("Not available")

    def submit(self):
        self.status = True
        print(self.name, "submitted")

    def show(self):
        if self.status:
            print(self.name, "by", self.writer, "is available")


b1 = Book("Python Guide", "Alex")
b2 = Book("OOP Concepts", "David")

b1.show()
b1.issue()
b1.submit()