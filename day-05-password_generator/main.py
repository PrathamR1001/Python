import random
import string

#Password Generator
print("Welcome to the PyPassword Generator!\n")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

letters_list = string.ascii_letters
symbols_list = string.punctuation
numbers_list = string.digits

# print(letters_list)
# print(symbols_list)
# print(numbers_list)

password_list = []
for i in range(letters):
    random_str = random.choice(letters_list)
    password_list.append(random_str)

for i in range(symbols):
    random_sym = random.choice(symbols_list)
    password_list.append(random_sym)
    
for i in range(numbers):
    random_num = random.choice(numbers_list)
    password_list.append(random_num)
    
print(password_list)
random.shuffle(password_list)

password = ""
for i in password_list:
    password += random.choice(password_list)

# password = "".join(password_list)
print(f"Your password is {password}.")

# 2nd approach 

# random_str = random.choices(letters_list, k=letters)
# random_sym = random.choices(symbols_list, k=symbols)
# random_num = random.choices(numbers_list,k=numbers)

# print(random_str)
# print(random_sym)
# print(random_num)

# password_values = random_str + random_sym + random_num
# print(password_values)


# random.shuffle(password_values)

# print(password_values)

# password = "".join(password_values)

# print(password)

# passw = password_values[1] + password_values[11]
# print(passw)

# password = ""
# for value in password_values:
#     password += value
# print(password)


# Practice

# max function without using built in max function
# num_list = []
# for i in range(1,50):
#     num_list.append(i)


# num_list.extend([99,240])

# some_val = 0
# for i in num_list:
#     if i > some_val:
#         some_val = i

# print(f"max value in the list is: {some_val}")


# adding consecutive numbers
# total_sum = 0
# for i in range(1,101):
#     # total_sum = i
#     total_sum += i 

# print(total_sum)


# FizzBuzz
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0 :
#         print("Fizz")
#     else:
#         print(i)