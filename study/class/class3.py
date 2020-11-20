import random

class Account :
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    def get_account_count(self) :
        print(Account.account_count)

SC = Account("SC", 100)
print(SC.name)
print(SC.balance)
print(SC.bank)
print(SC.account_number)
SC.get_account_count()
