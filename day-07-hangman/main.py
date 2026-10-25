import random

# Get some random words.
# select a random word from the above list
# generate the same number of blanks as the selected word length
# Ask the user to guess the letter >> If in the word, then replace the blank
        # else reduce one life

lives = 6
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

print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
# Create an empty string called "display"


while not game_over:

    user_input = str(input("Enter your letter: ").lower())

    display = ""

    for i in random_selection:
        if i == user_input:
            display += i
            correct_letters.append(user_input)
        elif i in correct_letters:
            display += i
        else:
            display += "_"

    print(f"Word to guess: {display}")

    if user_input not in random_selection:
        lives -= 1
        if lives == 0:
            game_over = True


    if "_" not in display:
        game_over = True
