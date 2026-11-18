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


difficulty = input("Choose difficulty: easy or hard: ").lower()

if difficulty == "easy":
    attempts_remaining = 10

elif difficulty == "hard":
    attempts_remaining = 5

else:
    print("Invalid difficulty. Defaulting to easy.")
    attempts_remaining = 10