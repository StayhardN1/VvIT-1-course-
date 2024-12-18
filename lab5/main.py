class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
circle = Circle(1161)
print("Текущий радиус:", circle.get_radius())
circle.set_radius(1488)
print("Новый радиус:", circle.get_radius())



class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"
book = Book("Пустышка", "Гасанов Курбан", 1488)
print(book.get_info())