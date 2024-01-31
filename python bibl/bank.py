class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Not Enough Minerals")

    def statement(self):
        print (f"Account Balance: ${self.balance}")


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self):
        return f"{self.name}'s Current Account : Balance $ {self.balance}"

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return f"{self.name}'s Savings Account : Balance $ {self.balance}"

Z = Current("Marius", 500)
Z.deposit(300)
Z.statement()
Z.withdraw(1000)
Z.statement()
Z.withdraw(1000)
print(Z)

T = Savings("Tom", 300)
T.withdraw(300)
T.withdraw(1)