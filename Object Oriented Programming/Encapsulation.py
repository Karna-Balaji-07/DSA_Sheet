class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

acct = BankAccount(1000)
acct.deposit(500)
acct.withdraw(200)
print(acct.get_balance())  # ✅ 1300

# print(acct.__balance)  ❌ AttributeError (due to name mangling)
