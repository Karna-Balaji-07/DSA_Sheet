# create account class with 2 attributes - balance and account no.
# create methods for debit, credit, and printing balance

class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.acc = accno

    def debit(self, amount):
        self.balance -= amount
        print(f'Rs. {amount} was deducted. Available balance is Rs. {self.balance}')

    def credit(self, amount):
        self.balance += amount
        print(f'Rs. {amount} credited to you account')
        print(f'Available balance is Rs. {self.balance}')

    def get_balance(self):
        return self.balance
acc1 = Account(1000,10111)
print(acc1.get_balance())
