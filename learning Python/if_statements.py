cars = ['audi', 'bmw', 'subaru', 'toyta']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("hold the anchovies!")