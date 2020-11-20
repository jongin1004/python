import random

class Account :
    account_count = 0
    deposit_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC"
        self.deposit_log = []
        self.withdraw_log = []

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


    def deposit(self, deposit) :
        if deposit > 0 :
            self.balance += deposit

            self.deposit_log.append(deposit)
            Account.deposit_count += 1

        if Account.deposit_count%5 == 0 :
            self.balance += self.balance*0.01


    def withdraw(self, withdraw) :
        if withdraw <= self.balance :
            self.withdraw_log.append(deposit)
            self.balance -= withdraw

    def display_info(self) :
        print("bank name :" + self.bank)
        print("name : " + self.name)
        print("account : " + self.account_number)
        print("balance : " + format(self.balance, ","))

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        # for amount in self.deposit_log:
        #     print(amount)
        print(self.deposit_log)


k = Account("kim", 10000)
k.deposit(1000)
k.deposit(1000)
k.deposit(1000)
k.deposit(1000)
k.deposit(1000)
k.deposit_history()
# print(k.deposit_count)
# print(k.balance)
#-
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# account_list = []
#
# c = Account("choi", 10000000)
# j = Account("jong", 10000)
# i = Account("in", 10000)
#
# account_list.append(c)
# account_list.append(j)
# account_list.append(i)
#
# for i in account_list :
#     if i.balance >= 1000000 :
#         i.display_info()
