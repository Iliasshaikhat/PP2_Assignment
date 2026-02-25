class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.base_salary + self.base_salary * self.bonus_percent / 100


class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self):
        return self.base_salary + self.completed_projects * 500


class Intern(Employee):
    pass


# Чтение входных данных
data = input().split()
role = data[0]

if role == "Manager":
    _, name, base, bonus = data
    emp = Manager(name, int(base), int(bonus))

elif role == "Developer":
    _, name, base, projects = data
    emp = Developer(name, int(base), int(projects))

else:  # Intern
    _, name, base = data
    emp = Intern(name, int(base))

# Вывод результата
print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")
