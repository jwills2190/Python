message = "One of Python's strengths is its diverse community."
print(message)

first_name = "Joel"
last_name = "Williams"
hello = f"Hello {first_name}, would you like to learn some Python today?"

print(hello)
print(first_name.lower())
print(first_name.upper())

quote = 'Neil deGrasse Tyson once said, "We are stardust brought to life, then empowered by the universe to figure itself out and we have only just begun"'
print(quote)

names = ['joel', 'kailey', 'maple']
missing_guest = names.pop()
print(f"I'm so sorry you aren't able to come to dinner {missing_guest}")
print(names)
names.append('sergio')
print(names)
print(f"I have found a bigger table and will be inviting 3 more people, {names[0].title()} {names[1].title()} {names[2].title()}")


names.insert(0, 'Sergio')
names.insert(2, 'Krystina')
names.append('Max')
print(names)

message = f"I have found a bigger table and would love to have you over for dinner, {names[0].title()}, {names[1].title()}, {names[2].title()}, {names[3].title()}, {names[4].title()}, "
print(message) 

message = f"My table won't arrive and now I won't be able to have all 5 people over. Sorry {names[0].title()}, {names[1].title()}, {names[2].title()}, {names[3].title()}, {names[4].title()},"

names.pop()
names.pop()
names.pop()
print(message)
print(names)

del names[0]
print(names)
del names[1]
print(names)
del names[0]
print(names)

# sort() method permanently alters the list
cars = ['bmw', 'subaru', 'jeep', 'toyota', 'honda', 'hyundai', 'ferrari']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# sorted() method temporarily alters the list
print(sorted(cars))

# reverse() method just flips the order of the items in the list.
cars.reverse()
print(cars)

len(cars)
print

dreamVacations = ['scotland', 'bali', 'japan', 'new zealand', 'banf', 'chile']
print(dreamVacations) #['scotland', 'bali', 'japan', 'new zealand', 'banf', 'chile']
print(sorted(dreamVacations)) #['bali', 'banf', 'chile', 'japan', 'new zealand', 'scotland']
print(dreamVacations) #['scotland', 'bali', 'japan', 'new zealand', 'banf', 'chile']
print(sorted(dreamVacations, reverse=True)) # ['scotland', 'new zealand', 'japan', 'chile', 'banf', 'bali']
dreamVacations.reverse()
print(dreamVacations) # ['chile', 'banf', 'new zealand', 'japan', 'bali', 'scotland']
dreamVacations.reverse()
print(dreamVacations) # ['scotland', 'bali', 'japan', 'new zealand', 'banf', 'chile']
dreamVacations.sort()
print(dreamVacations) # ['bali', 'banf', 'chile', 'japan', 'new zealand', 'scotland']
dreamVacations.sort(reverse=True)
print(dreamVacations) # ['scotland', 'new zealand', 'japan', 'chile', 'banf', 'bali']
print(dreamVacations[-1]) # -1 prints the last item in a list



