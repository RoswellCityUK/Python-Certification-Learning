list_to_analyse = ['C', 'i', 't', 'y', ' ', 'o', 'f', ' ',
                   'G', 'l', 'a', 's', 'g', 'o', 'w', ' ',
                   'C', 'o', 'l', 'l', 'e', 'g', 'e']

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

number_of_letters = len(list_to_analyse)
number_of_vowels = 0

for letter in list_to_analyse:
    if letter in vowels:
        number_of_vowels += 1

number_of_consonants = number_of_letters - number_of_vowels

print("List contains:", number_of_letters, "letters,", number_of_vowels, "vowels,", number_of_consonants, "consonants")
print()

del list_to_analyse[0]
del list_to_analyse[4]
del list_to_analyse[-1]

list_to_analyse[0] = 'Z'
list_to_analyse.insert(4, '2')

list_to_analyse[0], list_to_analyse[-1] = list_to_analyse[-1], list_to_analyse[0]

final_slice = list_to_analyse[::2]
print(f"Final slice [len: {len(final_slice)}]", final_slice)

letters_list = ['t', 'y', 'x']
if any(x in final_slice for x in letters_list):
    print("Final list contain one of the letters:", letters_list)
else:
    print("Final list dose not contain any of the letters:", letters_list)
