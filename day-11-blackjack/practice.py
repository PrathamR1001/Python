import random

# Start game

# Give player 2 cards
# Give dealer 2 cards

ace = [11,1]
cards = [2,3,4,5,6,7,8,9,10,10,10,10]


 
print(cards)

player_cards = random.choices(cards, k=2)
dealer_cards = random.choices(cards, k=2)

dealer_visible_card = random.choice(dealer_cards)
print(player_cards,dealer_cards,dealer_visible_card)


# Calculate player's score

player_score = sum(player_cards)
dealer_score = sum(dealer_cards)

print(player_score, dealer_score)

# If player has Blackjack:
#     handle Blackjack
if player_score == 21:
    print("Blackjack, Player wins !!")

# Otherwise:
else:
    player_input = str(input("Do you want another card, y or n: ").lower())
    if player_input == 'y':
        player_cards.append(random.choice(cards))
        player_score = sum(player_cards)
        print(player_cards)
        print(player_score)
        
        pass
    elif player_input == 'n':
        pass


#     Ask player:
#         "Do you want another card?"

#     If yes:
#         give another card
#         calculate score again

#         If score > 21:
#             player loses

#         Otherwise:
#             ask again

#     If no:
#         stop player's turn


# Dealer's turn:

#     calculate dealer's score

while dealer_score < 17:
    dealer_cards.append(random.choice(cards))
    dealer_score = sum(dealer_cards)

print(f"Dealer cards are: {dealer_cards}")
print(f"dealer score is : {dealer_score}")
#     while dealer score < 17:
#         give dealer another card

#     if dealer score > 21:
#         player wins


# Otherwise compare scores:

#     player > dealer:
#         player wins

#     dealer > player:
#         dealer wins

#     same:
#         draw


# Deal 2 cards to player
# Deal 2 cards to dealer

# Show:
#     player's full hand
#     player's score
#     dealer's first card only

# Player decides Hit or Stand

# After player's turn ends:
#     reveal dealer's full hand

# Dealer draws while score < 17

# Compare scores