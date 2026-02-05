class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


class SavingsAccount(BankAccount):

    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}")


class CurrentAccount(BankAccount):

    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn using overdraft")
        else:
            print("Overdraft limit exceeded")


print("\n--- Savings Account ---")
s = SavingsAccount("Alice", 1000, 5)
s.deposit(500)
s.add_interest()
s.withdraw(300)
s.display_balance()

print("\n--- Current Account ---")
c = CurrentAccount("Bob", 2000, 1000)
c.withdraw_with_overdraft(2500)
c.deposit(200)
c.display_balance()
