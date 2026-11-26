class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._branch = "Main"  
        self.__balance = balance  

    def get_balance(self):
        return self.__balance

acc = BankAccount("Sita", 1000)
print(acc.owner, acc._branch)
print("Balance:", acc.get_balance())
# print(acc.__balance)  # would fail from outside