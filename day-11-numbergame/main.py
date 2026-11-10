# # Number guessing game

# print("Welcome to the number guessing game !!\n")

# my_input = int(input("I am thinking between numbers 1 to 100.\n"))
# # difficulty = str(input("Choose difficulty level easy or hard: \n"))

# user_input = int(input("Enter a number between 1 and 100: \n"))

# def user_inp():
#     user_inp = int(input("Enter a number between 1 and 100: \n"))
#     user_input == user_inp
#     return user_input

# attempts_remaining = 10

# for i in range(attempts_remaining):
#     if user_input > my_input:
#         attempts_remaining -= 1
#         print(f"Too High. Attempts Remaining {attempts_remaining}")
#         user_inp()
        
#     elif user_input < my_input:
#         attempts_remaining -= 1
#         print("Too low.Attempts Remaining {attempts_remaining}")
#         user_inp()

#     elif user_input == my_input:
#         print(f"You guessed it. The answer is {my_input}")
#         break


import random

# Number guessing game

print("Welcome to the number guessing game !!\n")

my_input = random.randint(1, 100)

attempts_remaining = 10

for i in range(attempts_remaining):

    user_input = int(input("Enter a number between 1 and 100: \n"))

    if user_input > my_input:
        attempts_remaining -= 1
        print(f"Too High. Attempts Remaining: {attempts_remaining}")

    elif user_input < my_input:
        attempts_remaining -= 1
        print(f"Too Low. Attempts Remaining: {attempts_remaining}")

    else:
        print(f"You guessed it! The answer is {my_input}")
        break

if attempts_remaining == 0:
    print(f"You ran out of attempts! The number was {my_input}")
