class Account:

    _balance = 0
    id = None

    def __init__(self, id):
        self.id = id

    def check_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        return True

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
            return True
 
    def transfer(self, account, amount):
        if (account.withdraw(amount)):
            self.deposit(amount)
            return True
