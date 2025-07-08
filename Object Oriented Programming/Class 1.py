# class 1

class Students:

    College = "ABC"
    Type = "Private"

    def __init__(self,name1, name2, name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3

    def method1(self):
        print("Method1 ",self.name2)

    def addition(self,a,b):
        return a+b

    @staticmethod
    def subtraction(a,b):
        return b-a


obj = Students("Kilo","John","mark")
obj.method1()
print(obj.addition(2,5))
print(Students.subtraction(10,20))

