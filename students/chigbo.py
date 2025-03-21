# create a banking system where users can create an account deposit money, withdraw money, and check balances

class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute for balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.__balance}")

    def get_balance(self): #getter method for balance.
        return self.__balance

class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts (account_number: BankAccount)

    def create_account(self, account_number, account_holder, initial_balance=0):
        if account_number not in self.accounts:
            new_account = BankAccount(account_number, account_holder, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account created for {account_holder} with account number {account_number}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

# Example Usage
bank = Bank()

bank.create_account("123459999", "Alice Smith", 1000)
bank.create_account("67890", "Bob Johnson")

alice_account = bank.get_account("123459999")
bob_account = bank.get_account("67890")

if alice_account:
    alice_account.deposit(500)
    alice_account.withdraw(200)
    alice_account.check_balance()

if bob_account:
    bob_account.deposit(100)
    bob_account.withdraw(150) #should return insufficient funds.
    bob_account.check_balance()

print(f"Alice balance: {alice_account.get_balance()}") #showing getter method.
