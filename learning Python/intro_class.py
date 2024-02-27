# data type is a classification, mostly needed for a computer so that the computer can know how you intend to use the data in the future.

# Data type is a container for data. Data structure
# Python comes with built-in data types.
# String - sequence of characters. Strings are immutable.
# int - whole number
# float - number with decimals
# boolean - True or False. immutable
# Dictionary - {'Key': 'Value'}. Apparently the most popular job interview question.'Can tuple be used as a key in a dictionary?'. 'Can you use list as a key in a dictionary?'. Only immutable data type can be used as a key in a dictionary. Int, float, string, boolean, tuple. Anything else can be used as a value.
# list - sequence of values seperated by values, held in [] and has indicies
# tuple - immutable data type held in (). data usually comes in form of tuple. if function returns more than 1 result, it's packaged as a tuple.
# dictionary is fast because keys are unique. If you store phone numbers in a list then you need to iterate.
# set - collection of immutable items. set itself is mutable. 
# range - generates sequence of ints; start (inclusive) to stop (exclusive). When using range, you can use (start, stop, step). with 0 arguments, it defaults to stop. negative steps goes backward indicies.
# 1. type
# 2. dir - helps you to see what is possible with current code. 
# 3. help - function that does exactly what it says, 'help'.

word = 'apple'
for i in range(len(word)-1, -1, -1):
    print(i, word[i]) 
    
    
# palindrome is a popular interview question
# 1. Ask user for a word
# 2. Return True if word is palindrome
# 3. Return False if not.
# 4. Use range function
# divmod(5,3)

res = divmod(5,3)
a,b = res
print(b)

word = 'racecar'
mp = len(word)//2
is_palindrome = True
for index in range(mp):
    print(len(word)-1-index, word[len(word)-1-index])
    if word[index] != word[len(word)-1-index]:
        is_palindrome = False
is_palindrome

# using range function, build multiplication table
# n = int(input("Please enter a positive integer between 1 and 15: "))
for row in range(1, 11):
    for col in range(1, 11):
        print(f"{row*col:4}", end=" ")
    print()

print

# always take run time complexity into consideration: Big O notation.