# Number guessing game

print("Welcome to the number guessing game !!\n")

my_input = int(input("I am thinking between numbers 1 to 100.\n"))
difficulty = str(input("Choose difficulty level easy or hard: \n"))

user_input = int(input("Enter a number between 1 and 100: \n"))

if user_input > my_input:
    print("Too High !!")
elif user_input < my_input:
    print("Too low.")

