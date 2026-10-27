import string

# take a code (string)
# take a number to move the string by that number
# move the current letters by that value

letters = list(string.ascii_lowercase)
print("".join(letters))
# print(type(letters))

word = str(input("Enter the code: \n").lower())

num = int(input("Enter the number: \n"))

code = []

for i in word:
    for x,letter in enumerate(letters):
        if i == letter:
            # print(letters[x + num], num, x, i)
            # print(type(letters[x + num]))
            code.append(letters[x + num])
            new_code = "".join(code)
print(f"Your new code:\n{new_code}")