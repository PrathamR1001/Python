# Treasure Island Game
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice_1 = str(input("Which direction do you want to go Left or Right:\n").capitalize())

if choice_1 == "Left":
    print("You are on the river coast !! ")
    choice_2 = str(input("Do you want to swim or wait, type Swim or Wait:\n").capitalize())
    if choice_2 == "Swim":
        print("Game Over")
    elif choice_2 == "Wait":
        choice_3 = str(input("Which door do you want to enter Red, Blue or Yellow:\n").capitalize())
        if choice_3 == "Red" or choice_3 == "Blue":
            print("Game Over")
        elif choice_3 == "Yellow":
            print("You win !!!")
        else:
            print("Enter the correct choice")
    else:
        print("Enter the correct choice")
elif choice_1 == "Right":
    print("Game Over")
else:
    print("Enter the correct choice")









# Practice

# print("Welcome to the rollecoaster!!")

# height = int(input("Enter your height in cm: "))

# if height > 120: 
#     print("welcome")
# else:
#     print("Not tall enough")



# num = int(input("Enter your number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# height = int(input("Enter your height : "))
# age = int(input("Enter your age: "))

# if age >= 18:
#     if height >= 120:
#         print("Welcome")
#     else:
#         print("Not tall enough!!")
# else:
#     print("Not old enough")

# print("Welcome to Python Pizza Deliveries!!")
# size = str(input("What size pizza do you want? S, M, L: ").upper())
# pepperoni = str(input("Do you want pepperoni on your pizza? Y or N: ").upper())        
# extra_cheese = str(input("Do you want extra cheese? Y or N: ").upper())

# # Small = 15, M = 20, L = 25, pepperoni = s = +2, m/l = +3, cheese= +1 
# bill = 0

# # Size
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("Wrong Input")

# # pepperoni
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# # cheese
# if extra_cheese == "Y":
#     bill += 1

# print(f"Your total bill is ${bill}.")


# height = int(input("Enter your height: "))
# bill = 0

# if height > 120:
#     age = int(input("Enter your age: "))
#     if age < 12:
#         bill +=5
#         print(f"Your bill is ${bill}")
#     elif age < 18:
#         bill += 7
#         print(f"Your bill is ${bill}")
#     elif age > 18 and age < 45:
#         bill += 12
#         print(f"Your bill is ${bill}")
#     elif age > 45 and age < 55:
#         bill += 0
#         print(f"Your bill is ${bill}") 
#     elif age > 55:
#         bill += 12
#         print(f"Your bill is ${bill}")
    
#     want_photos = str(input("Do you want photos, Y or N: ").upper())

#     if want_photos == "Y" :
#         bill += 3
#         print(f"Your bill is ${bill}")
# else:
#     print("Not tall enough")

