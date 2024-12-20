"""
Name: Kaden Meir
Date: 12/20/24
"""

#list creation - use []

list_of_numbers = [1,,2,3,4,5,6,8]
print(list_of_numbers)

# lists are mutable - can be changed
list_of_numbers[6] = 7
print(list_of_numbers)

# can be extended
list_of_numbers.append(8)
print(list_of_numbers)

list_of_numbers.remove(1) # value not index
print(list_of_numbers)

list_letters = ["a","b","c","d","e"]

# make elements of a list into a string
letter_string = "".join(list_letters)
print(letter_string)
letter_string = "*".join(list_letters)
print(letter_string)

# make a string into a list
vowels = "aeiou"
vowel_list = vowel.split() # doesn't work at intended
print(vowel_list)

# make each vowel an element
vowel_list.clear() # nothing in list after used
print(vowel_list)
for letter in vowels:
  vowel_list.append(letter) # this spaces the letters out
print(vowel_list)

# iterating through a list
for vowel in vowel_list:
  print(vowel)
