import random

# Get some random words.
# select a random word from the above list
# generate the same number of blanks as the selected word length
# Ask the user to guess the letter >> If in the word, then replace the blank
        # else reduce one life


# Generate random list of words
word_list = ["Samsung", "Apple", "Nokia"]


# Select Random word from the list
random_selection = random.choice(word_list).lower()
print(random_selection)

# User Input
print("\nYou are guessing a smartphone company.")


# Create a placeholder
placeholder = ""
for i in range(len(random_selection)):
    placeholder += "_"

# print(placeholder)

# Create an empty string called "display"
display = ""

# if the guess matches the letter in the random_selection then
# reveal tha letter in that position AND display the rest as blanks.

# unit = len(random_selection)
# while unit != 0:
user_input = str(input("Enter your letter: ").lower())
for i in random_selection:
    if i == user_input:
        display += i
    else:
        display += "_"

print(display)
