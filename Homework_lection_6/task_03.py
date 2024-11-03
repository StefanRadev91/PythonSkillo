# Problem 3:
# Design a class "BankAccount" with methods 
# for deposit, withdrawal, and balance inquiry. Use encapsulation to protect the account balance (it should be read-only).
# Demonstrate proper usage of the class.

class BankAccount:
    def __init__(self, start_sum):
        self._account_balance = start_sum

    def withdrawal(self, sum):
        if sum > self._account_balance:
            print("Insufficient funds")
        else:
            self._account_balance -= sum

    def deposit(self, sum):
        self._account_balance += sum

    @property
    def balance(self):
        return self._account_balance

bankacc = BankAccount(50)
bankacc.deposit(50)
print(bankacc.balance)        