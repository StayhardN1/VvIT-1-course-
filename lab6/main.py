class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self, new_password):
        self.__password = new_password
    def check_password(self, password):
        return self.__password == password
    def get_user_info(self):
        return f"User: {self.username}, Email: {self.email}, Password:{self.__password}"
gku = UserAccount(username="gasanov", email="gasanov@mail.com", password="1939")
print(gku.get_user_info())
gku.set_password("1488")
print(gku.check_password("1488"))
print(gku.check_password("1939"))



class Vehicle:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
    def get_info(self):
        return f"{self.mark} {self.model}"
class Car(Vehicle):
    def __init__(self, mark, model, fuel_type):
        super().__init__(mark, model)
        self.fuel_type = fuel_type
    def get_info(self):
        return f"Mark:{self.mark}, Model:{self.model}, Fuel type: {self.fuel_type}"
Mashina = Vehicle("BMW", "M5 CS")
car = Car("BMW", "M", "Petrol")
print(Mashina.get_info())
print(car.get_info())