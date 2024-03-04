# Class is the blueprint to create an object. 
# We use function and method interchangebly but method belongs to a class (built into object). method always has first argument, 'self'
# Functions are more generic, methods visually also begin with def __init__

class Car:
    def __init__(self, make, model, color="white"):
        self.make = make
        self.model = model
        self.color = color
        
car1 = Car("Ford", "Mustang", "Black")
car2 = Car("Honda", "Civic", "Green")

print(car1.model) # Mustang
print(car2.color) # Green


class Customer:
    def __init__(self, name, balance=0.00):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError("Not enough money")
        self.balance -= amount
        return self.balance

john = Customer('John', 1000)
john.deposit(100)
john.withdraw(500)

print(john.balance)

