atmcard = input("Please enter your card number: ")
pin = input("Please enter your PIN: ")

class Atm(object):

    def _init_(self, atmcard = 0, pin=0, money = 10000):
        self.atmcard = atmcard
        self.pin = pin
        self.money = money

    def cashWithDrawl(self):
        moneytowithdraw = int(input("How much ammount do you want to withdraw: "))
        self.money = int(self.money) - moneytowithdraw
        print("You have withdrawed Rs",moneytowithdraw, "from your bank account.")
    
    def balance(self):
        print("Your bank balance is Rs", self.money)

user = Atm("10000","1010", "10000")

if atmcard == user.atmcard and pin == user.pin:
    user.cashWithDrawl()
    user.balance()
    toDo = input("If you want to withdraw more money then please enter ""Withdraw""(without quotes), If you want to sign out then enter ""Sign Out"": ")
    if toDo == "Withdraw":
        user.cashWithDrawl()
        user.balance()
    if toDo == "Sign Out":
        exit