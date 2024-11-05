class Bank_Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}. New balance: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')
        def check_balance():
          print(f'Current balance: {self.balance}')

  

# Usage
deposit, withdraw, check_balance = Bank_Account(100)
deposit(50)
withdraw(30)
check_balance()