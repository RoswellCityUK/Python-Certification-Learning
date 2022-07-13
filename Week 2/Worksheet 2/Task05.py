"""
Program asks User for few things:
    - to enter a string of at least four words in the one line
    - to enter a word to be found in the list of entered words
    - to enter a replacement word
"""

user_words = input("Enter at least four words in one line: ")
user_search_word = input("Enter word to find: ")
user_replacement_word = input("Enter replacement word: ")

if user_words.count(user_search_word) == 0:
    print("Word not found!")
else:
    user_words = user_words.replace(user_search_word, user_replacement_word).title()
    print(user_words)
