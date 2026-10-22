import random


# Rock, Paper, Scissors
choices = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? " \
                "0 for Rock, 1 for Paper, 2 for Scissors\n"))


comp_choice = random.randrange(0, 3)

if user_choice > 2 or user_choice < 0:
    print("Choose between 0 and 2.")
else:
    print(f"You chose : {choices[user_choice]},\nComputer Chose : {choices[comp_choice]}\n")

    if user_choice == 0 and comp_choice == 2:
        print("You win!!!")
    elif comp_choice == 0 and user_choice == 2:
        print("Computer wins!!")
    # elif user_choice > 2 or user_choice < 0:
    #     print("Choose between 0 and 2.")
    elif user_choice < comp_choice:
        print("Computer wins!!!")
    elif user_choice > comp_choice:
        print("You win!!!")
    elif user_choice == comp_choice:
        print("No one wins")




# Who will pay the bill

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# random_name = random.choice(friends)

# print(random_name)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# # dirty_dozen = [fruits, vegetables]
 
# # print(dirty_dozen[1][1])

# print(fruits.index("Apples"))