"""
Program is creating Dictionary from two different Tuples as keys and values
and then encrypts User message using this dictionary
finally it decodes message
"""

mykeys = ('A', 'B', 'C', 'D', 'E', 'F', 'G',
          'H', 'I', 'J', 'K', 'L', 'M', 'N',
          'O', 'P', 'Q', 'R', 'S', 'T', 'U',
          'V', 'W', 'X', 'Y', 'Z')

myvalues = ('1', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', '11', '12', '13',
            '14', '15', '16', '17', '18', '19',
            '20', '21', '22', '23', '24', '25', '26')

mydictionary = {}
for x in range(len(mykeys)):
    mydictionary[mykeys[x].casefold()] = myvalues[x]

user_message = input("Enter Message to encrypt: ").casefold()

encoded_message = ""
for x in user_message:
    encoded_message += mydictionary[x] + " "
encoded_message = encoded_message.strip(" ")
print("Encoded message: " + encoded_message)

decoded_message = ""
for x in encoded_message.split(' '):
    decoded_message += list(mydictionary.keys())[list(mydictionary.values()).index(x)]

print("Decoded message: " + decoded_message)

