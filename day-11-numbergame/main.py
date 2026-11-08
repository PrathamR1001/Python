# Number guessing game

print("Welcome to the number guessing game !!\n")

my_input = int(input("I am thinking between numbers 1 to 100.\n"))
# difficulty = str(input("Choose difficulty level easy or hard: \n"))

user_input = int(input("Enter a number between 1 and 100: \n"))

def user_inp():
    user_inp = int(input("Enter a number between 1 and 100: \n"))
    user_input == user_inp
    return user_input

def calculate_score():
    if user_input > my_input:
        print("Too Low.")
        user_input()
    elif user_input < my_input:
        print("Too High")
        user_input()
    elif user_input == my_input:
        print("You got it.")

attempts_remaining = 10

for i in range(attempts_remaining):
    user_inp()
    calculate_score()

