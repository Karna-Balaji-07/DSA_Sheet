'''
Define a employee class with attributes role, department and salary.
This class also has a show() details method.

create an engineer class that inherits the properties from Employee and
has additional attributes like name and age
'''

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f'Role = {self.role} \nDepartment = {self.department} \nSalary ={self.salary}')

class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.age = age
        self.name = name




emp1 = Employee("IT",'Finance',230000)
emp1.showDetails()