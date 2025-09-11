class BankAccount:
    def __init__(self,balance):
        self.__balance=0
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposit ₹{amount}")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdraw ₹{amount}")
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
account = BankAccount()
account.deposit(5000)
account.withdraw(2000)
print("Final Balance:", account.get_balance())
