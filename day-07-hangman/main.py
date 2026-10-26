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

# Create an empty string called "display"

game_over = False
correct_letters = []

while not game_over:
    display = ""
    print(correct_letters)
    user_input = str(input("Enter your letter: ").lower())

    if user_input in correct_letters:
        print("You have already guessed this letter.")

    for i in random_selection:
        if i == user_input:
            display += user_input
            correct_letters.append(user_input)
            print(display)
        elif i in correct_letters:
            display += i
        else:
            display += "_"
    print(lives)
            #print(display)
            
    
    if user_input not in random_selection:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.") 
    
    if "_" not in display:
        game_over = True
        print("You Win!!!")

    
    print(f"Word to guess: {display}")
