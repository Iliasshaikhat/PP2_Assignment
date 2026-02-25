class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def raise_salary(self,percent):
        self.salary += percent
        return self.salary
        
aaa = Employee( "NAME", 100)
print(aaa.raise_salary(10))