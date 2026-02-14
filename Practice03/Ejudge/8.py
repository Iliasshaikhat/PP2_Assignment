class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return self.balance
        
balance, withdraw_amount = map(int, input().split())

acc = Account("Owner", balance)
print(acc.withdraw(withdraw_amount))
