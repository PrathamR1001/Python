# import string

# letters = list(string.ascii_lowercase)
# print("".join(letters))

# # def decode():
# #     code_rev = []

# #     for i in word:
# #             for x,letter in enumerate(letters):
# #                 if i == letter:
# #                     # print(letters[x + num], num, x, i)
# #                     # print(type(letters[x + num]))
# #                     code_rev.append(letters[x - num])
# #                     new_code_rev = "".join(code_rev)
# #     print(f"Your decoded message is:\n{new_code_rev}")

# # decode()

# get_input = str(input("Type 'encode' to encrypt, type 'decode' to decrypt': ").lower())

# word = str(input("Enter your message: \n").lower())

# num = int(input("Enter the shift number: \n"))

# if get_input == 'encode':
#     def encode():
#         code = []

#         for i in word:
#             for x,letter in enumerate(letters):
#                 if i == letter:
#                     code.append(letters[x + num])
#                     new_code = "".join(code)
#         print(f"Your encoded message is:\n{new_code}")
#     encode()


# # elif get_input == 'decode':
# #     decode()
# else:
#     print("Please enter encode or decode")




# def greet(name, location):
#     print(f"Hello {name}, where are you from?")
#     print(f"Hi, I am from {location}.")
#     print("Great !!")




# vowels = "true"
# name = "kanye west kim kardashian"

# # output >>  e : 1, i : 2, a : 1 total = 1 + 2 + 1 = 4
# # check if the vowels are present in the name and how many times they occur
# letter_list = []
# for letter in name:
#     for vowel in vowels:
#         if letter == vowel and letter != " ":
#             letter_list.append(letter)
#             # print(letter, vowel)
#             # print(letter_list)


# vowels1 = "love"
# letter_list_1 = []
# for letter in name:
#     for vowel in vowels1:
#         if letter == vowel and letter != " ":
#             letter_list_1.append(letter)
#             #print(letter, vowel)
#             #print(letter_list)


# print(letter_list, letter_list_1)

# total_score = str(len(letter_list)) + str(len(letter_list_1))
# print(total_score)

# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# names = (name1 + " " + name2).lower()
# print(names)


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



def calculate_love_score(name1, name2):
    names = (name1 + " " + name2).lower()

    list1 = []
    list2 = []

    word1= "True".lower()
    word2 = "Love".lower()

    for letter in names:
        for i in word1:
            if letter == i and letter != " ":
                list1.append(letter)

    for letter1 in names:
        for j in word2:
            if letter1 == j and letter1 != " ":
                list2.append(letter1)

    score1 = str(len(list1))
    score2 = str(len(list2))

    total_score = score1 + score2
    
    return print(total_score)
    
calculate_love_score("Kanye West", "Kim Kardashian")