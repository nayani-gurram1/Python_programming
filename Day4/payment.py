class Payment:
    pass
class cashPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹{amount}in cash")
class cardPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹{amount}using credit/debit card")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid ₹{amount}using UPI")
payments = [cashPayment(), cardPayment(), UPIPayment()]
 
for p in payments:
    p.pay(1000)
