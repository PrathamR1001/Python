import random

# Without Ace

cards = [2,3,4,5,6,7,8,9,10,10,10,10]

# Deal cards
player_cards = random.choices(cards, k=2)
dealer_cards = random.choices(cards, k=2)

# Show cards
print(f"Your cards are: {player_cards}")
print(f"Dealer cards : {random.choice(dealer_cards)}")

# Check Score
player_score = sum(player_cards)
dealer_score = sum(dealer_cards)

# Player turn

should_continue = True

while should_continue:
    player_input = str(input("Do you want to hit y or n: ").lower())

    if player_input == 'y' :
        player_cards.append(random.choice(cards))
        player_score = sum(player_cards)
        print(f"Your cards are: {player_cards}")
        print(f"Your score is : {player_score}")
        if player_score > 21:
            should_continue = False
            print("You lose.")
            
    elif player_input == 'n':
        should_continue = False
    else:
        print("Please enter y or n")

# print(player_score)

# Dealer's turn
if player_score < 21 :
    while dealer_score < 17:
        dealer_cards.append(random.choice(cards))
        dealer_score = sum(dealer_cards)
    print(f"Dealer score is : {dealer_score}")


if player_score > 21:
    print("Dealer Wins !!")
elif dealer_score > 21:
    print("Player Wins !!")
elif player_score > dealer_score:
    print("Player Wins !!")
elif player_score == dealer_score:
    print("Its a Draw")
else:
    print("Dealer Wins !!")
