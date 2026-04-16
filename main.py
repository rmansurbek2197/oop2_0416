class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough money")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def add_interest(self):
        self._BankAccount__balance *= 1.05
