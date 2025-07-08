# create a student class that takes name and marks of 3 subjects as arguments in
# constructor. then create a method to print the average

class Student:
    def __init__(self,name, biology, physics, chem):
        self.name = name
        self.bio = biology
        self.phy = physics
        self.chem = chem

    def average(self):
        avg = (self.bio+self.phy+ self.chem) // 3
        return avg

obj = Student("Henry",23,28,25)
result = obj.average()
print(f'Average marks : {result}')