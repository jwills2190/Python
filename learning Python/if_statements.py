cars = ['audi', 'bmw', 'subaru', 'toyta', "Honda"]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print("hold the anchovies!")
    
age0 = 22
age1 = 18


# if age0 > 20 and age1 < 20:
#     print(False)

car = "Honda"
if car not in cars:
    print(f"{car.title()}, you aren't here")
else:
    print(f"{car.title()}, whoa")
    
    print("Is car == 'Honda'? I predict True.")
    print(car == "Honda")
    
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')
    
age = 10
if age > 9:
    print("You are old enough")
    print("Have you started 5th grade?")
else: 
    print("Too young!")
    
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission costs ${price}")

requested_toppings = ['mushrooms', 'extra cheese', 'pepperoni']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if "tomato" in requested_toppings:
        print("Adding tomato.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
    
print("\nFinished making your pizza!")


alien_color = 'green'
if alien_color == 'red':
    print('1 point earned')
elif alien_color == 'yellow':
    print('2 points earned')
elif alien_color == 'green':
    print('5 points earned!')
else:
    print(alien_color)
    
for requested_toppin in requested_toppings:
    print(f"Adding {requested_toppin}.")
    
print("\nFinished making your pizza!")