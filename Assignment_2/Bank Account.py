class Bank:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def add_money(self, amt):
        if amt > 0:
            self.balance += amt
            print("Amount added:", amt)
        else:
            print("Invalid amount")

    def remove_money(self, amt):
        if amt <= self.balance and amt > 0:
            self.balance -= amt
            print("Amount withdrawn:", amt)
        else:
            print("Not enough balance")

    def show_balance(self):
        print("Balance is:", self.balance)


acc = Bank("987654321", 500)

while True:
    print("\n1.Check 2.Deposit 3.Withdraw 4.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        acc.show_balance()
    elif ch == "2":
        x = float(input("Enter amount: "))
        acc.add_money(x)
    elif ch == "3":
        x = float(input("Enter amount: "))
        acc.remove_money(x)
    elif ch == "4":
        break
    else:
        print("Wrong input")