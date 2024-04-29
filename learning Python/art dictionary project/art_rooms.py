# A prestigious art gallery has contacted you because management
# wants to figure out how many people visit each room in the gallery
# and for how long. Your goal is to write a program that takes
# a formatted text file that describes the overall gallery's foot-
# traffic on a minute-to-minute basis. From this data you must
# compute the average time spent in each room, and how many visitors
# there were in each room in total.
# The input: each line represents a visitor entering or leaving a room.
# The first item is an integer representing the visitor's unique ID.
# The second item is an integer representing the room's number.
# The third item is either "I" or "O" for "in" or "out" representing
#     a visitor entering or leaving that room.
# The fourth is a timestamp integer, representing the minute of the day.
# Assumptions:
# All of the lines are space-delimited.
# All the input is logically well-formed, meaning each person who
# enters a room will later leave the room at some point in the future.
# A visitor will only be in one room at a time.
# Desired Output:
#     For each room that has data associated with it,
#     print the average length of time visitors have stayed (as a float). 
#     Then print the total number of visitors in the room.
# Example:
#     0 0 I 540
#     1 0 I 540
#     0 0 O 560
#     1 0 O 560
#     "Room 0, 20.0 minute average visit, 2 visitor(s) total"
    
# Hint: dict
# the problem is about rooms

# file = open(r'C:\Users\joelw\Documents\my-portfolio\Python\learning Python\art dictionary project\rooms.txt', 'r', encoding='utf-8')
dict = {}

for i in file:
    user, room, direction, time = i.split()
    if room not in dict:
        dict[room] = [-int(time)]
    else:
        if direction == "I":
            dict[room].append(-int(time))
        else:
            dict[room].append(int(time))
print(dict)


# From this data you must computer the avg time spend in each room + number of visitors
# There were in each __ in each room in total.
# Output should be in this format:
    # "Room 0, 20.0 minute avg visit, 2 visitor(s) total"
# Using sum

# The key is the room # and the value is the list with the time in and time out.
d = {}
for key, values in dict.items():
    # print(sum(values))
    visitors = len(values) //2
    average = round(sum(values)/visitors, 2)
    print(f"Room {key}, {average} minutes average visits, \
        {visitors} visitor(s) total")
    d[key] = visitors
    
alist = list(d.items())

alist.sort(key=lambda x : x[1], reverse=True)

print(alist)
# Use a dictionary to sort rooms by number of visitors
# pep 8 style guide is apparently an interview question.