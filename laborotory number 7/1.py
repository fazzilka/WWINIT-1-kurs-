class Employee:
    def __init__(self, name, id, **kwargs):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Employee Name: {self.name}, ID: {self.id}"


# 2. Создадим класс Manager с дополнительным атрибутом department и методом manage_project()

class Manager(Employee):
    def __init__(self, name, id, departments, **kwargs):
        super().__init__(name, id, **kwargs)
        self.department = departments

    def manage_project(self):
        return f"{self.name} is managing a project in the {self.department} department."

    def get_info(self):
        return super().get_info() + f", Department: {self.department}"


# 3. Создадим класс Technician с атрибутом specialization и методом perform_maintenance()

class Technician(Employee):
    def __init__(self, name, id, specialization, **kwargs):
        super().__init__(name, id, **kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} is performing maintenance in the field of {self.specialization}."

    def get_info(self):
        return super().get_info() + f", Specialization: {self.specialization}"


# 4. Создадим класс TechManager, который наследует как Manager, так и Technician
# Этот класс будет комбинировать атрибуты и методы обеих ролей

class TechManager(Manager, Technician):
    def __init__(self, name, id, departments, specialization):
        super().__init__(name = name, id = id, departments = departments, specialization = specialization)
        self.team = []  # Инициализируем пустой список подчинённых

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = [member.get_info() for member in self.team]
        return "Colaps Information:\n" + "\n".join(team_info)

    def get_info(self):
        return super().get_info() + f", Specialization: {self.specialization}"


# 5. Создадим объекты и продемонстрируем их функциональность

# Создадим сотрудника, менеджера, техника и технического менеджера


# Создание объекта класса Employee
employee = Employee("Daniil", 101)
print(employee.get_info())
print()

# Создание объекта класса Manager
manager = Manager("Bogdan", 202, "Sales")
print(manager.get_info())
print(manager.manage_project())
print()

# Создание объекта класса Technician
technician = Technician("Natalie", 303, "IT Support")
print(technician.get_info())
print(technician.perform_maintenance())
print()

# Создание объекта класса TechManager
tech_manager = TechManager("Oleg", 404, "IT", "Network Security")
print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())
print()

# Добавим сотрудников в команду подчинённых TechManager
tech_manager.add_employee(employee)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)


    # Выведем информацию о команде
print(tech_manager.get_team_info())

print()

print(TechManager.__mro__)