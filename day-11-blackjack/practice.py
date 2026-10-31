import random

# Start game

# Give player 2 cards
# Give dealer 2 cards

ace = [11,1]
cards = [2,3,4,5,6,7,8,9,10,10,10,10]


print(cards)

player_cards = random.choices(cards, k=2)
dealer_cards = random.choices(cards, k=2)


print(player_cards,dealer_cards)


# Calculate player's score

player_score = sum(player_cards)
dealer_score = sum(dealer_cards)

print(player_score, dealer_score)

# If player has Blackjack:
#     handle Blackjack

# Otherwise:

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