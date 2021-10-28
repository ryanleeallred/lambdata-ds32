class Wallet():
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            return "insufficient funds"
        else:
            self.balance -= amount
    
    def add_cash(self, amount):
        self.balance += amount
