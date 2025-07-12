# # Inheritance
# from tkinter.font import names
#
#
# class Car:
#
#     def __init__(self,type):
#         self.type = type
#
#     @staticmethod
#     def start():
#         print("Car started")
#
#     @staticmethod
#     def stop():
#         print("Car stopped")
#
# class Toyota(Car):
#     def __init__(self,name,type):
#         self.name= name
#         super().__init__(type)
#         super().start()
#
# car = Toyota("Prius","electric")
# print(car.type)
#
#
#
#
#
# class Grandparent:
#     def show1(self):
#         print("Grandparent")
#
# class Parent(Grandparent):
#     def show2(self):
#         print("Parent")
#
# class Child(Parent):
#     def show3(self):
#         print("CHild")
#
#
# class A:
#     vara = "Welcome to class a"
#
# class B:
#     varb = "Welcome to class b"
#
# class C(A,B):
#     varc = "welcome to class c"
#
# # obj = C()
# # print(obj.varc)
# # print(obj.varb)
# #
# #
# # obj = Child()
# # obj.show1()
# # obj.show3()
# # obj.show2()


# class Person:
#     name = "Rohan"
#     @classmethod
#     def changenae(cls,name):
#         cls.name = name
#
#
# obj = Person()
#
# print(obj.name)
# print(Person.name)

class Student:
    def __init__(self, phy,bio, chem):
        self.phy = phy
        self.chem = chem
        self.bio = bio

    @property
    def percentage(self):
        return str((self.bio+self.chem+self.phy)/3) + "%"

obj = Student(90,92,87)
print(obj.percentage)
obj.phy = 79
print(obj.percentage)

