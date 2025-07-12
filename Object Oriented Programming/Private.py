# private attribute and methods

class Person:
    __name = "Anonymous" # private attribute
    def __hello(self):
        print("Hello world")

    def welcome(self):  # Private methods
        print("Hello name")
        self.__hello()
obj = Person()
obj.welcome()