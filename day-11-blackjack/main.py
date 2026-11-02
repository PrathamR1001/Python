import random

# Without Ace

cards = [2,3,4,5,6,7,8,9,10,10,10,10]

# Deal cards
def deal_cards():
    return random.choice(cards)

# Player Score
def calculate_score(card_list):
    return sum(card_list)


player_cards = random.choices(cards, k=2)
dealer_cards = random.choices(cards, k=2)

# Show cards
print(f"Your cards are: {player_cards}")
print(f"Dealer card : {random.choice(dealer_cards)}")

# Check Score
player_score = calculate_score(player_cards)
dealer_score = calculate_score(dealer_cards)

# Player turn

player_turn = True

while player_turn:
    player_input = str(input("Do you want to hit y or n: ").lower())

    if player_input == 'y' :
        player_cards.append(deal_cards())
        player_score = calculate_score(player_cards)
        print(f"Your cards are: {player_cards}")
        print(f"Your score is : {player_score}")
        if player_score > 21:
            player_turn = False
            print("You lose.")
            
    elif player_input == 'n':
        player_turn = False
    else:
        print("Please enter y or n")

# print(player_score)

# Dealer's turn
if player_score < 21 :
    while dealer_score < 17:
        dealer_cards.append(deal_cards())
        dealer_score = calculate_score(dealer_cards)
    print(f"Dealer score is : {dealer_score}")


# Find the winner
if player_score == 21:
    print("Blackjack. Player Wins!!")
elif dealer_score == 21:
    print("Blackjack. Dealer Wins!!")
elif player_score > 21:
    print("Dealer Wins !!")
elif dealer_score > 21:
    print("Player Wins !!")
elif player_score > dealer_score:
    print("Player Wins !!")
elif player_score == dealer_score:
    print("Its a Draw")
else:
    print("Dealer Wins !!")
