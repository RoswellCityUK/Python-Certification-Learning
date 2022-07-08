"""
The program takes the user's word and counts the letters in it in some strange way
"""

import string

dictionary_letters = {}

for x in string.ascii_letters:
    dictionary_letters[x] = 0

user_word = input("Enter word to analise: ")

for x in user_word:
    dictionary_letters[x] += 1

for x in dictionary_letters.keys():
    if dictionary_letters[x] > 0:
        print(f"{x} --> {dictionary_letters[x]}")
