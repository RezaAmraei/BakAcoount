class BankAccount:
    def __init__(self, amount = 0 ,intrest = 0.01):
        self.amount = amount
        self.intrest_rate = intrest
    
    def deposit(self, amount):
        self.amount += amount
        return self
    def withdraw(self, amount):
        if self.amount - amount >= 0:
            self.amount -= amount
        else:
            print('nsufficient funds: Charging a $5 fee')
            self.amount -= 5
        return self
    def display_account_info(self):
        print("Balance: ",self.amount)
        return self
    def yield_intrest(self):
        if self.amount >= 0:
            self.amount += self.intrest_rate * self.amount
            return self



reza = BankAccount(100).deposit(20).deposit(200).deposit(100).withdraw(200).yield_intrest().display_account_info()

vini = BankAccount(200).deposit(200).deposit(2000).withdraw(50).withdraw(20).withdraw(200).withdraw(500).yield_intrest().display_account_info()