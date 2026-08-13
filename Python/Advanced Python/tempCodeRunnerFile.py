class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Book Name   : {self.title}")
        print(f"Author Name : {self.author}")
        print(f"Price       : {self.price}")
        print()


book1 = Book("IKIGAI", "XYZ", 200)
book2 = Book("Soumya", "Balkrushna", 100000)
book3 = Book("Python Basics", "ABC", 500)

book1.display()
book2.display()
book3.display()