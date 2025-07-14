'''
Money Manager for tracking expenses and income

Display these also
- Expenses average per week, per day, per month

Visualizations :
- Income vs Expense : Pie chart
- Expenses over time : line chart
- Income over time : Line chart
- Expenses vs categories : Bar chart
- Income vs Categories : Bar chart

'''
import csv,os,sys
import time
from collections import defaultdict

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


    @staticmethod
    def plot_all_visualizations():
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns

        # Load and clean Expense Data
        exp_df = pd.read_csv('Expense.csv')
        exp_df['Date'] = pd.to_datetime(exp_df['Date'], dayfirst=True, errors='coerce')
        exp_df['Expenses'] = pd.to_numeric(exp_df['Expenses'], errors='coerce')
        exp_df['Expense Category'] = exp_df['Expense Category'].str.strip().str.lower()

        # Load and clean Income Data
        inc_df = pd.read_csv('Income.csv')
        inc_df['Date'] = pd.to_datetime(inc_df['Date11'], dayfirst=True, errors='coerce')
        inc_df['Income'] = pd.to_numeric(inc_df['Income'], errors='coerce')
        inc_df['Income Category'] = inc_df['Income Category'].str.strip().str.lower()

        # Aggregate data
        total_exp = exp_df['Expenses'].sum()
        total_inc = inc_df['Income'].sum()
        exp_by_cat = exp_df.groupby('Expense Category')['Expenses'].sum().sort_values(ascending=False)
        inc_by_cat = inc_df.groupby('Income Category')['Income'].sum().sort_values(ascending=False)
        exp_over_time = exp_df.groupby('Date')['Expenses'].sum().sort_index()
        inc_over_time = inc_df.groupby('Date')['Income'].sum().sort_index()

        # Setup subplot grid
        fig, axs = plt.subplots(3, 2, figsize=(18, 16))
        fig.suptitle('📊 Financial Overview', fontsize=20)
        plt.subplots_adjust(hspace=0.4, wspace=0.3)

        # 1. Income vs Expense - Pie Chart
        pie_labels = ['Income', 'Expenses']
        pie_data = [total_inc, total_exp]
        colors = ['#4CAF50', '#F44336']
        wedges, texts, autotexts = axs[0, 0].pie(pie_data, labels=pie_labels, autopct='%1.1f%%', startangle=90,
                                                 colors=colors)
        axs[0, 0].set_title('Income vs Expense')
        for text in autotexts:
            text.set_color('white')
            text.set_fontweight('bold')

        # 2. Expenses Over Time - Line Chart
        sns.lineplot(x=exp_over_time.index, y=exp_over_time.values, marker='o', color='red', ax=axs[0, 1])
        axs[0, 1].set_title('Expenses Over Time')
        axs[0, 1].set_xlabel('Date')
        axs[0, 1].set_ylabel('₹')
        axs[0, 1].tick_params(axis='x', rotation=45)
        for x, y in zip(exp_over_time.index, exp_over_time.values):
            axs[0, 1].annotate(f"{y:.0f}", xy=(x, y), xytext=(0, 5), textcoords='offset points', ha='center',
                               fontsize=9)

        # 3. Income Over Time - Line Chart
        sns.lineplot(x=inc_over_time.index, y=inc_over_time.values, marker='o', color='green', ax=axs[1, 0])
        axs[1, 0].set_title('Income Over Time')
        axs[1, 0].set_xlabel('Date')
        axs[1, 0].set_ylabel('₹')
        axs[1, 0].tick_params(axis='x', rotation=45)
        for x, y in zip(inc_over_time.index, inc_over_time.values):
            axs[1, 0].annotate(f"{y:.0f}", xy=(x, y), xytext=(0, 5), textcoords='offset points', ha='center',
                               fontsize=9)

        # 4. Expenses by Category - Bar Chart
        sns.barplot(x=exp_by_cat.values, y=exp_by_cat.index, palette='Reds_r', ax=axs[1, 1])
        axs[1, 1].set_title('Expenses by Category')
        axs[1, 1].set_xlabel('Total Expenses (₹)')
        axs[1, 1].set_ylabel('Category')
        for i, v in enumerate(exp_by_cat.values):
            axs[1, 1].text(v + 5, i, f"{v:.0f}", va='center', fontsize=9)

        # 5. Income by Category - Bar Chart
        sns.barplot(x=inc_by_cat.values, y=inc_by_cat.index, palette='Greens', ax=axs[2, 0])
        axs[2, 0].set_title('Income by Category')
        axs[2, 0].set_xlabel('Total Income (₹)')
        axs[2, 0].set_ylabel('Category')
        for i, v in enumerate(inc_by_cat.values):
            axs[2, 0].text(v + 5, i, f"{v:.0f}", va='center', fontsize=9)

        # 6th subplot empty
        axs[2, 1].axis('off')

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()

    @staticmethod
    def print_block_with_margin(lines, margin=25):
        import os

        try:
            term_width = os.get_terminal_size().columns
        except OSError:
            term_width = 100  # Fallback width if terminal size can't be detected

        max_line_width = term_width - 2 * margin
        margin_space = " " * margin

        for line in lines:
            # Truncate if line too long, else print with margin
            if len(line) > max_line_width:
                print(margin_space + line[:max_line_width])
            else:
                print(margin_space + line)

    @staticmethod
    def input_with_margin(prompt, margin=10):
        return input(" " * margin + prompt)


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

    '''
    Display total expenses transaction
    '''
    @staticmethod
    def displayExpense():
        expenses = 'Expense.csv'
        file_exists = os.path.exists(expenses)
        with open(expenses,'r',newline='') as file:
            reader = csv.reader(file)
            records = list(reader)

            lines = []
            lines.append("")
            lines.append("=========== Expense Records ===========")
            header = records[0]
            lines.append(" | ".join(header))
            lines.append("-" * (len(header) * 15))
            for row in records[1:]:
                lines.append(" | ".join(row))
            lines.append("=======================================")
            lines.append("")
            Bank.print_block_with_margin(lines)
    '''
    Display transactions by account
    '''
    @staticmethod
    def displayAccountExpenses(account):
        expenses = 'Expense.csv'
        file_exists = os.path.exists(expenses)
        with open(expenses, 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader if row['Account Number'] == account]

            if not rows:
                print(f"No expense records found for Account: {account}")
                return

            lines = []
            lines.append("")
            lines.append("=========== Expense Records ===========")
            lines.append(" | ".join(reader.fieldnames))
            lines.append("-" * (len(reader.fieldnames) * 15))
            for row in rows:
                lines.append(" | ".join(row.values()))
            lines.append("=======================================\n")

            Bank.print_block_with_margin(lines)

    '''
    Display Categories and their expenditure
    '''
    @staticmethod
    def displayExpenseCategoryExpenditure():
        expense = 'Expense.csv'
        categories = defaultdict(int)
        with open(expense,'r',newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    category = row['Expense Category'].strip().lower()
                    amount = int(row['Expenses'])
                    categories[category] += amount
                except (ValueError,KeyError):
                    continue

        lines = []
        lines.append("")
        lines.append("====== Total Expenses by Category ======")
        for category, total in categories.items():
            lines.append(f"{category.capitalize():<15}: ₹{total:.2f}")
        lines.append("========================================\n")

        Bank.print_block_with_margin(lines)

    '''
    User input
    '''

    @staticmethod
    def update():
        try:
            date = Bank.input_with_margin("Date of Transaction: ")
            Account = Bank.input_with_margin("Account Number: ")
            amount = int(Bank.input_with_margin("Expense: "))
            category = Bank.input_with_margin("Expense Category: ")

            balance = Bank.get_latest_balance(Account)
            exp = Expense(Account, amount, category, date, balance)
            exp.AddExpenseFile()
            exp.AddExpenseCommonFile()
            Bank.print_block_with_margin(["", "✅ Transaction Updated Successfully.\n"])
        except Exception as e:
            Bank.print_block_with_margin([f"❌ Error found: {e}"])


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
            date = Bank.input_with_margin("Date of Transaction: ")
            Account = Bank.input_with_margin("Account Number: ")
            amount = int(Bank.input_with_margin("Expense: "))
            category = Bank.input_with_margin("Expense Category: ")

            balance = Bank.get_latest_balance(Account)
            inc = Income(date,Account,balance,amount,category)
            inc.AddIncomeFile()
            inc.AddIncomeCommonFile()
            Bank.print_block_with_margin(["", "✅ Transaction Updated Successfully.\n"])
        except Exception as e:
            Bank.print_block_with_margin([f"❌ Error found: {e}"])


    @staticmethod
    def displayIncome():
        incomes = 'Income.csv'
        file_exists = os.path.exists(incomes)
        with open(incomes,'r',newline='') as file:
            reader = csv.reader(file)
            records = list(reader)

            lines = []
            lines.append("")
            lines.append("=========== Income Records ===========")
            header = records[0]
            lines.append(" | ".join(header))
            lines.append("-" * (len(header) * 15))
            for row in records[1:]:
                lines.append(" | ".join(row))
            lines.append("=======================================\n")

            Bank.print_block_with_margin(lines)

    @staticmethod
    def displayAccountIncome(account):
        expenses = 'Income.csv'
        file_exists = os.path.exists(expenses)
        with open(expenses, 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader if row['Account Number'] == account]

            if not rows:
                Bank.print_block_with_margin([f"❌ No income records found for Account: {account}"])
                return

            lines = []
            lines.append("")
            lines.append("=========== Income Records ===========")
            lines.append(" | ".join(reader.fieldnames))
            lines.append("-" * (len(reader.fieldnames) * 15))
            for row in rows:
                lines.append(" | ".join(row.values()))
            lines.append("=======================================\n")

            Bank.print_block_with_margin(lines)

    @staticmethod
    def displayIncomeCategoryExpenditure():
        income = 'Income.csv'
        categories = defaultdict(int)
        with open(income,'r',newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    category = row['Income Category'].strip().lower()
                    amount = int(row['Income'])
                    categories[category] += amount
                except (ValueError,KeyError):
                    continue

        lines = []
        lines.append("")
        lines.append("====== Total Income by Category ======")
        for category, total in categories.items():
            lines.append(f"{category.capitalize():<15}: ₹{total:.2f}")
        lines.append("========================================\n")

        Bank.print_block_with_margin(lines)


'''
Main Function : ******************************************************************************************************
'''
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    dicts = {
        '1': 'Add Expense',
        '2': 'Add Income',
        '3': 'View Current Balance',
        '4': 'View Expense Transactions',
        '5': 'View Income Transactions',
        '6': 'View Whole Transaction',
        '7': 'View Account Expenses',
        '8': 'View Account Income',
        '9': 'Category-wise Expense',
        '10': 'Category-wise Income',
        '11' : 'Visualize',
        '12': 'Exit'
    }

    while True:
        clear_screen()
        lines = []
        lines.append("")
        lines.append("====== BANK TRANSACTION MENU ======")
        for idx, val in dicts.items():
            lines.append(f"{idx:<2} : {val}")
        lines.append("===================================")

        Bank.print_block_with_margin(lines)

        choice = Bank.input_with_margin("Enter your choice (1-11): ").strip()
        clear_screen()  # Clear before action output

        if choice == '1':
            Expense.update()
        elif choice == '2':
            Income.update()
        elif choice == '3':
            account = Bank.input_with_margin("Enter your account Number: ")
            balance = Bank.get_latest_balance(account)
            Bank.print_block_with_margin([f"💰 Remaining bank balance: ₹{balance}"])
        elif choice == '4':
            Expense.displayExpense()
        elif choice == '5':
            Income.displayIncome()
        elif choice == '6':
            Bank.displayTransactions()
        elif choice == '7':
            account = Bank.input_with_margin("Enter your account Number: ")
            Expense.displayAccountExpenses(account)
        elif choice == '8':
            account = Bank.input_with_margin("Enter your account Number: ")
            Income.displayAccountIncome(account)
        elif choice == '9':
            Expense.displayExpenseCategoryExpenditure()
        elif choice == '10':
            Income.displayIncomeCategoryExpenditure()
        elif choice == '11':
            Bank.plot_all_visualizations()
        elif choice == '12':
            Bank.print_block_with_margin(["✅ Thank you for using the system."])
            break
        else:
            Bank.print_block_with_margin(["❌ Invalid choice. Please enter a number between 1 and 11."])
        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()



