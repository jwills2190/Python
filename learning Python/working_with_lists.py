# Chapter 4 - Working With Lists
# Python for loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians: # for every magician in the list of magicians, print the magicians' name.
    print(f"{magician.title()} seems like a swell person and even better magician")
    print(f"{magician.title()}, I can't wait for your next act\n")
    
print("Off to New York!")
    
# indentations in python are very important. 
pizzas = ['cheese', 'sausage and hot honey', 'pepperoni']
for pizza in pizzas:
    print(f"I'll have you know, {pizza} is one of my go to pizzas")

print("\nI really love pizza!")

animals = ['dogs', 'elephants', 'possums']
for animal in animals: 
    print(f"\n{animals[0]} are great", f"\n{animals[1]} are also great", f"\n{animals[2]} are misunederstood")

    
print("\nAny of these animals would make a great pet")

# range() function
for value in range(1, 5): 
    print(value) # 1-4. range starts printing at the first argument, ends the number before the second argument

# using range() to create a list of numbers
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]

even_numbers = list(range(2, 11, 2)) # the number as the third argument in range skips numbers in the given range
print(even_numbers) #[2, 4, 6, 8, 10]

nums = list(range(0, 100, 5))
print(nums) # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

squares = []
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)
    squares.append(value**2)
    
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

divided_in_half = [value/2 for value in range(1, 100)]
print(divided_in_half)

# use a for loop to print the numbers from 1 - 20, inclusive

for value in range(1, 21):
    print(value)
    

# Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
# million = list(range(1, 100))
# for value in million:
#     print(value)
    
#Make a list of the numbers from 1 - 1000, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly python can add a million numbers

#Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. use a for loop to print each number.
for value in range(1, 21, 2):
    print(value)
  
#Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
threes = []
for value in range(3, 31, 3):
    threes.append(value)
print(threes)

#Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)

# Cube Comprehension: Use a list of comprehension to generate a list of the first 10 cubes
cubes = [value**3 for value in range(1,11)]
print(cubes)

#Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# for player in players[:3]:
#     print(player.title())
names_again = players[:]

names_again.append('Mike')
print(names_again)

# immutable lists are called tuples
# They're similar to how you write lists but with () instead.
# tuples must contain a comma to make them a tuple. to create a tuples with one element you would write it my_t = (3, )
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

def greeting():
    print("Hello World")

greeting()

def new_funct(x, y):
    if(x > y):
        print(x - y)
        
new_funct(10, 7)
        