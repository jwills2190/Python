age = 20
price = 19.95
first_name = 'Joel'
is_online = True
# print(age + price)


first_name = 'John'
last_name = "Smith"
age = 20
new_patient = True

# name = input("What is your name? ")
# print("Hello " + name)

#Changing one data type to another
# birth_year = input("Enter your birth year: ")
# age = 2020 - int(birth_year) # 2020 is an int and birth_year is a string. You can't do math with a string
print(age)

#convert data type to integer (whole number)
int()

# convert data type to float (number with decimal)
float()

# convert data type to boolean (True or False)
bool()

# convert data type to string
str()

# basic calculator. enter two numbers. program will print the sum of the two numbers.

# num1 = float(input("Enter a number "))
# num2 = float(input("Enter a second number "))
# sum = num1 + num2
# print("Total is " + str(sum))

course = 'Python for Beginners' # this is an object
print(course.upper()) # converts string to uppercase. It returns a new string and doesn't alter the variable course
print(course.find('y')) # returns first index occurence in the string. 1 in this case

#Arithmatic Operators
print(10 // 3) # single / gives you division and double // gives you the whole number.
x = 10
x += 3
print(x)

#Operator Precedence
y = 10 + 3 * 2  # 16
z = (10 + 3) * 2 # 26

#Comparison Operators
a = 3 > 2 # boolean True
# >= 
# < 
# <=
# == 
# !=

#Logical Operators
price = 5
print(price > 10 or price < 30) # True
print(price > 10 and price < 30) # False
print(not price > 10) # inverses the given value

# If statements
# There are no curly braces in Python
temperature = 25

if temperature > 30: 
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else: # only executes if none of the above are true
    print("It's cold")
print("Done")

#Weight converter program

# Weight: 170
# (K)g or (L)bs: l  
# Ask for input if the weight is in K or L, the user can enter uppercase or lowercase.
# output the weight in the selected letter
# Weight in Kg: 76.5
# input function always returns a string

# weight = int(input("What is your weight? "))
# unit = input("Is that in (K)g or (L)bs? ")

# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in Lbs: " + str(converted))
# else:
#     converted = weight * 0.45
#     print("Weight in Kg:" + str(converted))
    
# i = 1
# while i <= 10:
#     print(i * "*")
#     i = i + 1

# names = ['Joel', "Kailey", 'John', 'Mary', 'Maple']
# names[2] = 'Max'
# print(names[0:3]) # returns index 0-3 exclusive of the 3rd index

#list methods. strings and lists are objects
# number = [1,2,3,4,5]

# print(len(number))


# numbers = [1, 2, 3, 4, 5, 6]
# for item in numbers: 
#     print(item)
    
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# number = range(5) # range object that can store sequence of numbers
# for item in number:
#     print(item) # 0 1 2 3 4 

# numbers = range(5, 10)
# for number in numbers:
#     print(number) # 5 6 7 8 9 
    
# numberz = range(5, 10, 2)
# for numberd in numberz:
#     print(numberd) # 5 7 9


#tuples
# similar to lists. They're immutable

numbers = (1, 2, 3) # this cannot be changes
numbers.count(3) # 1
numbers.index(2) # 1


