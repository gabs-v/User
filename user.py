class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0 

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self, amount):
        self.amount -= amount

    def user_balance(self):
        print (f"User: {self.name}, Balance: {self.amount}")

    def transfer(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.user_balance()
        user.user_balance()


gaby = User("Gaby")
gibby = User("Gibby")
gabs = User("Gabs")

gaby.make_deposit(200)
gaby.make_deposit(400)
gaby.make_deposit(55)
gaby.make_withdrawl(200)
gaby.user_balance()

gibby.make_deposit(3000)
gibby.make_deposit(400)
gibby.make_withdrawl(28)
gibby.make_withdrawl(42)
gibby.user_balance()

gabs.make_deposit(100)
gabs.make_withdrawl(200)
gabs.make_withdrawl(250)
gabs.make_withdrawl(300)
gabs.user_balance()

gaby.transfer(400, gabs)