class account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

     # debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs. ",amount,"was debited")
        print("Total balance = ",self.get_balance())


      #credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs. ",amount,"was credited")
        print("Total balance = ",self.get_balance())


    def get_balance(self):
        return self.balance
    


acc1 = account(10000,37187799390)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(2000)
acc1.credit(1500)
acc1.credit(50000)
acc1.debit(10000)
