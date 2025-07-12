'''
Money Manager for tracking expenses and income



for output and visualization purposes
- Income by month, bank account, category
- Expense by month, Bank accounts, category
- Full Transactions

Visualizations :
- Income vs Expense
- Income by Month
- Expenses by month compare the date string with the input month.. 02-01-2000 compare input month with date[3:5]
    - we can make input month in string names and have a dictionary for month names and numbers
-Income by Year
- Expenses by year
-

'''
import csv,os

class Bank:
    def __init__(self,bankaccount,balance):
        self.account = bankaccount
        self.balance = balance

    @staticmethod
    def get_latest_balance(account):
        if not os.path.exists('common.csv'):
            return 10000  # default balance if file doesn't exist yet

        with open('common.csv', 'r') as file:
            reader = csv.DictReader(file)
            latest = 10000  # default
            for row in reader:
                if row['Account Number'] == account:
                    latest = int(row['Balance'])  # keep updating until last match
            return latest

    @staticmethod
    def displayTransactions():
        with open('common.csv','r',newline='') as file:
            reader = csv.reader(file)
            records = list(reader)

            print("\n=========== Expense Records ===========")
            header = records[0]
            print(" | ".join(header))
            print("-" * (len(header) * 15))

            for row in records[1:]:
                print(" | ".join(row))
            print("=======================================\n")

'''
Expense System ********************************************************************************************************
'''
class Expense(Bank):
    def __init__(self, account, expense, category, date,balance):
        self.expense = int(expense)
        self.category = category
        self.date = date

        latest_balance = Bank.get_latest_balance(account)
        self.updated_balance = latest_balance - self.expense
        super().__init__(account, self.updated_balance)

    def AddExpenseCommonFile(self):
        common = 'common.csv'
        file_exists = os.path.exists(common)
        with open(common,'a',newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Date','Account Number','Income','Expense','Balance'])
            writer.writerow([self.date, self.account,0,self.expense,self.updated_balance])

    def AddExpenseFile(self):
        expense = 'Expense.csv'
        file_exists = os.path.exists(expense)

        with open(expense,'a',newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Date','Account Number','Expense Category','Expenses','Balance'])
            writer.writerow([self.date, self.account, self.category, self.expense, self.updated_balance])
    @staticmethod
    def displayExpense():
        expenses = 'Expense.csv'
        file_exists = os.path.exists(expenses)
        with open(expenses,'r',newline='') as file:
            reader = csv.reader(file)
            records = list(reader)

            print("\n=========== Expense Records ===========")
            header = records[0]
            print(" | ".join(header))
            print("-" * (len(header) * 15))

            for row in records[1:]:
                print(" | ".join(row))
            print("=======================================\n")

    @staticmethod
    def update():
        try:
            date = input("Date of Transaction: ")
            Account = input("Account Number: ")
            amount = int(input('Expense: '))
            category = input("Expense Category: ")
            balance = Bank.get_latest_balance(Account)
            exp = Expense(Account,amount,category,date,balance)
            exp.AddExpenseFile()
            exp.AddExpenseCommonFile()
            print("Transaction Updated Successfully.\n")
        except Exception as e:
            print(f'Error found {e}')


'''
Income system**********************************************************************************************************
'''
class Income(Bank):
    def __init__(self,date, account,balance,income, category):
        self.date = date
        self.income = int(income)
        self.category = category

        latest_balance = Bank.get_latest_balance(account)
        self.updated_balance = latest_balance + self.income
        super().__init__(account,self.updated_balance)


    def AddIncomeCommonFile(self):
        common = 'common.csv'
        file_exists = os.path.exists(common)

        with open(common,'a',newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Date','Account Number','Income','Expense','Balance'])
            writer.writerow([self.date, self.account,self.income,0,self.updated_balance])

    def AddIncomeFile(self):
        income = 'Income.csv'
        file_exists = os.path.exists(income)
        with open(income,'a',newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Date','Account Number','Income Category','Income','Balance'])
            writer.writerow([self.date, self.account, self.category, self.income, self.updated_balance])

    @staticmethod
    def update():
        try:
            date = input("Date of Transaction: ")
            Account = input("Account Number: ")
            amount = int(input('Income: '))
            category = input("Income Category: ")
            balance = Bank.get_latest_balance(Account)
            inc = Income(date,Account,balance,amount,category)
            inc.AddIncomeFile()
            inc.AddIncomeCommonFile()
            print("Transaction Updated Successfully.\n")
        except Exception as e:
            print(f'Error found {e}')
    @staticmethod
    def displayIncome():
        incomes = 'Income.csv'
        file_exists = os.path.exists(incomes)
        with open(incomes,'r',newline='') as file:
            reader = csv.reader(file)
            records = list(reader)

            print("\n=========== Income Records ===========")
            header = records[0]
            print(" | ".join(header))
            print("-" * (len(header) * 15))

            for row in records[1:]:
                print(" | ".join(row))
            print("=======================================\n")

'''
Main Function : ******************************************************************************************************
'''

def main():
    dicts = {'1':'Add Expense',
             '2' : 'Add Income',
             '3': 'View Current Balance',
             '4' : 'View Expense Transactions',
             '5' : 'View Income Transactions',
             '6' : 'View Whole Transaction',
             '7' : 'Exit'
             }

    while True:

        print("\n====== BANK TRANSACTION MENU ======")
        for index, value in dicts.items():
            print(f'{index} : {value}')
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            Expense.update()
        elif choice == '2':
            Income.update()
        elif choice == '3':
            account = input("Enter Account Number: ")
            balance = Bank.get_latest_balance(account)
            print(f'Remaining bank balance : {balance}')
        elif choice == '4':
            Expense.displayExpense()
        elif choice == '5':
            Income.displayIncome()
        elif choice == '6':
            Bank.displayTransactions()
        elif choice == '7':
            print("Thank you for using")
            break
        else:
            print("Enter a valid choice: ")


if __name__ == '__main__':
    main()



