# How do you define dictionaries?
# Feel confident in response to what dictionaries are. They have key, value pairs with unique identifiers. Collection of pairs that have key and a value. The key has to be unique, and should be immutable data type.
# Class creates an object
# Dictionary's cannot be sorted. lists can. Dictionaries are mutable.
# List = collection of iterable items stored in a variable surrounded by [].

d = {'z': 275, 'c': 1, 'a': 67}
def get_number(t):
    print(t[1])
    return t[1]

alist = list(d.items())
alist.sort(key=get_number, reverse=True)
# alist.sort()
print(alist)

t = ('z', 275) 
# how to get 275 out of tuple
def get_number(t):
    return t[1]
print(t[1])


# map(t)

# Lambda is anonymous function. function without name.

# functions that take *args (Non-Keyword Arguments). If you have two arguments, the first is the variable name.
def add(var, *args):
  return sum(args)
print(add('Hello',2,3,4,45,66))

# function can take kwargs. Need to pass keyword arguments or dictionary.
def new(**kwargs):
    print(kwargs['greeting'], kwargs['name'])

new(name="John", greeting="Hello")
