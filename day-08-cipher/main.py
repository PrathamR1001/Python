import string

letters = list(string.ascii_lowercase)
print("".join(letters))

# print(max(letters))
# def decode():
#     code_rev = []

#     for i in word:
#             for x,letter in enumerate(letters):
#                 if i == letter:
#                     # print(letters[x + num], num, x, i)
#                     # print(type(letters[x + num]))
#                     code_rev.append(letters[x - num])
#                     new_code_rev = "".join(code_rev)
#     print(f"Your decoded message is:\n{new_code_rev}")

# decode()

# get_input = str(input("Type 'encode' to encrypt, type 'decode' to decrypt': ").lower())

# word = str(input("Enter your message: \n").lower())

# num = int(input("Enter the shift number: \n"))

# if get_input == 'encode':

#     code = []

#     for i in word:
#         for x,letter in enumerate(letters):
#             if i == letter:
#                 code.append(letters[x + num])
#                 new_code = "".join(code)
#     print(f"Your encoded message is:\n{new_code}")



# elif get_input == 'decode':
#     decode()
# else:
#     print("Please enter encode or decode")


# Love Calculator

# def calculate_love_score(name1, name2):
#     names = (name1 + " " + name2).lower()
#     print(names)

#     list1 = []
#     list2 = []

#     word1= "True".lower()
#     word2 = "Love".lower()

#     for letter in names:
#         for i in word1:
#             if letter == i and letter != " ":
#                 list1.append(letter)

#     for letter1 in names:
#         for j in word2:
#             if letter1 == j and letter1 != " ":
#                 list2.append(letter1)

#     score1 = len(list1)
#     score2 = len(list2)

#     total_score = str(score1) + str(score2)
#     print(total_score)


# calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")
# calculate_love_score("prince william", "kate middleton")
# calculate_love_score("brad pitt", "jennifer aniston")

# originalText = "abcde"
# shiftAmount = 1

# My solution

def encrypt(originalText, shiftAmount):
    new_word = ""
    for i in originalText: 
            index_val = letters.index(i)
            # print(index_val)
            new_index = index_val + shiftAmount
            if new_index >= len(letters):
                difference = len(letters) - index_val
                shift_diff = shiftAmount - difference
                new_index =  shift_diff
            new_word += letters[new_index]

    print(new_word)

encrypt(originalText= "hello" ,shiftAmount= 2)


# Given Solution

word = "hello"
shift_val = 2 
cipher_text = ""

for i in word:
    shifted_val = letters.index(i) + shift_val
    shifted_val = shifted_val % len(letters) 
    cipher_text += letters[shifted_val]

print(cipher_text)
