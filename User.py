class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):	
        self.account_balance += amount	

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"{self.name}, Balance: $ {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
chris = User("Chris B", "Chris@python.com")

guido.make_deposit(10)
guido.make_deposit(20)
guido.make_deposit(30)
guido.make_withdrawal(10)
guido.display_user_balance()
monty.make_deposit(20)
monty.make_deposit(40)
monty.make_withdrawal(10)
monty.make_withdrawal(10)
monty.display_user_balance()
chris.make_deposit(100)
chris.make_withdrawal(20)
chris.make_withdrawal(20)
chris.make_withdrawal(20)
chris.display_user_balance()
guido.transfer_money(chris,20)
guido.display_user_balance()
chris.display_user_balance()