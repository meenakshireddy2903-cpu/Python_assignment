
class BankAccount:
    bname = 'SBI'
    branch = 'Hyderabad'
    ifsc = "SBIN000123"
    helpline = "1800-11-2211"
    min_balance = 1000   

    def __init__(self, name, age, acc_no, balance):
        self.name = name
        self.age = age
        self.acc_no = acc_no
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw")
        elif self.balance - amount < BankAccount.min_balance:
            print("Cannot withdraw.")
        else:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Amount deposited:", amount)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Acc no:", self.acc_no)
        print("Balance:", self.balance)

    @classmethod  
    def update_min_balance(cls, new_balance):
        cls.min_balance = new_balance
        print("Minimum balance :", cls.min_balance)


acc1 = BankAccount("Meenakshi", 20, 2005, 16000)

acc1.display()
acc1.deposit(2000)
acc1.withdraw(500)
acc1.display()
BankAccount.update_min_balance(2000)
