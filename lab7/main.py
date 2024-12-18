class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"


employee = Employee("Kurban", 1)
print(employee.get_info())


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id, )
        self.department = department

    def manage_project(self, project_name):
        return f"Manager {self.name} is managing the project: {project_name} in department {self.department}"

    def get_info(self):
        return super().get_info() + f", Department: {self.department}"


manager = Manager("Gasanov", 21, "prodazhi")
print(manager.get_info())
print(manager.manage_project("Kuvalda"))


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self, equipment):
        return f"Technician {self.name} with specialization in {self.specialization} is maintaining {equipment}"

    def get_info(self):
        return super().get_info() + f", Specialization: {self.specialization}"


technician = Technician("Artem", 32, "Technic")
print(technician.get_info())
print(technician.perform_maintenance("Ne znayu"))


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return f"TechManager {self.name} has no employees in the team."
        team_info = f"TechManager {self.name}'s Team:\n"
        for employee in self.team:
            team_info += f" - {employee.get_info()}\n"
        return team_info

    def get_info(self):
        return f"TechManager Info: {super().get_info()}"


tech_manager = TechManager("Maga", 11, "IT", "programs")
tech_manager.add_employee(employee)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)
print(tech_manager.get_info())
print(tech_manager.get_team_info())
print(tech_manager.manage_project("Brawl Stars"))
print(tech_manager.perform_maintenance("Clash Royale"))
