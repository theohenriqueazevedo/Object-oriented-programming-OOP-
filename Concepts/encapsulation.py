# encapsulation.py

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance

def main():
    account = BankAccount("Alice", 1000)
    print("Initial balance:", account.get_balance())
    account.deposit(200)
    account.withdraw(150)
    print("Final balance:", account.get_balance())

if __name__ == "__main__":
    main()
