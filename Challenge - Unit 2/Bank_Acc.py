class Bank_Account:

    #Initializer
    def __init__(self, acc_number, acc_holder_name, initial_balance=0):
        self.__acc_number = acc_number
        self.__acc_holder_name = acc_holder_name
        self.__acc_balance = initial_balance

    #Method for depositing money
    def deposit(self, amount):
        if amount > 0:
            self.__acc_balance += amount
            print(f"₹{amount} deposited. New balance is : ₹{self.__acc_balance}")
        else:
            print("Invalid deposit amount.")

    #Method for withdrawing money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__acc_balance:
            self.__acc_balance -= amount
            print(f"₹{amount} withdrawn. New balance is : ₹{self.__acc_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    #Method to display holder name, acc_num and acc_balance
    def display_balance(self):
        print(f"Account Holder: {self.__acc_holder_name}")
        print(f"Account Number: {self.__acc_number}")
        print(f"Account Balance: ₹{self.__acc_balance}")

#Inputting values from the user
account_number = input("Enter the Account Number: ")
account_holder_name = input("Enter the Account Holder's Name: ")
initial_balance = float(input("Enter the Initial Balance : "))

#Creating an obj of the Bank_Account class
account = Bank_Account(account_number, account_holder_name, initial_balance)

account.display_balance()
deposit_amount = float(input("Enter the deposit amount : "))
account.deposit(deposit_amount)
withdraw_amount = float(input("Enter the withdrawal amount : "))
account.withdraw(withdraw_amount)
