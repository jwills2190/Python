
# enumerate will give you a count next to item in dictionary or list.

numbers = [1,2,3,4,5,5,5,5,5]
fives = []

for num in numbers:
    if num == 5:
        fives.append(num)
print(fives)

# [expression for loop filter] 
# this is list comprehension. runs faster than traditional for loop
f = [num for num in numbers if num == 5]
print(f)

week = ['mon', 'tues', 'wed']
days = [day.title() for day in week] #.capitalize() and .title() are the same.
print(days)

string = 'a1b2c3d4e5'
# use list comprehension and string method join to get just letters from string and return just alphabetical chars
new_string = [str for str in string if str.isalpha()]
print(''.join(new_string))

# exercise to clean and manipulate data. Before writing code, make pseudocode.

# Pig Latin (also known as Dog Latin) is a language game in which words are altered according to certain rules. To make the pig latin form of an English word, the initial consonant sound is transposed to the end of the word, and an "ay" is affixed. Specifically, there are two rules:

# If a word begins with a vowel, append "yay" to the end of the word. If a word begins with a consonant, remove all the consonants from the beginning up to the first vowel and append them to the end of the word. Finally, append "ay" to the end of the word.

# For example:

# dog => ogday
# python => onpythay
# scratch => atchscray
# is => isyay
# apple => appleyay

word = 'apple'
# 1. Define vowels
# 2. Slice the first char
# 3. if char is in vowels, add 'ay' to the word
# 4. else iterate until we find the vowel
# 5. get the index of the vowel
# 6. slice all letters up to the vowel
# 7. slice all letters starting with the vowel
# 8. concatinate all the parts and add 'ay'

def is_vowel(letter):
    """
    Returns True if letter is a vowel
    """
    letter = letter.lower()
    vowels = ('a','e','i','o','u')
    if letter in vowels:
        return True
    else:
        return False

def game(word):
    """
    Returns Pig Latin version of the word
    """
    if is_vowel(word[0]):
        res = word + 'ay'
    else:
        for index in range(len(word)):
            if is_vowel(word[index]):
                part_one = word[0:index]
                part_two = word[index:]
                res = part_two + part_one + 'ay'
                break
    print(res)
    
def main():
    word = 'apple'
    if word.isalpha() and len(word) > 1:
        result = game(word)
    else:
        result = 'Not valid input'
    return result

main()


# Many people do not use capital letters correctly, especially when typing on small devices like smart phones. In this exercise, you will write a function that capitalizes the appropriate characters in a string. A lowercase 'i' should be replaced with an uppercase "I" if it both preceded and followed by a space. The first character in the string should also be capitalized, as well as the first non-space character after a ".", '!' or "?". For example, if the function is provided with the string "what time do i have to be there? what's the address?" then it should return the string "What time do I have to be there? What's the address?". Include a main program that reads a string from the user, capitalizes it using your function, and displays the result.

# Find index of first char of words after punctuation.
# var with punctuation. then find index.
# replace any 'i' with 'I' if there is nothing before or after the letter.
# slice first char for each sentence. return it capitalized.

nonspace = ".!?"
string = "what time do i have to be there? what's the address? call you later."
string = string.capitalize()
string = string.replace(' i ', ' I ')
print(string)

for index in range(len(string)-2):
    if string[index] in nonspace:
        print(index, string[index]) 
        index_to_change = index + 2
        letter_to_capitalize = string[index_to_change].capitalize()
        # print(letter_to_capitalize)
        part_one = string[0:index_to_change]
        # print(part_one)
        part_two = string[index_to_change+1:]
        # print(part_two)
        string = part_one + letter_to_capitalize + part_two
print(string)




