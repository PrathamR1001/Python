import random

# ace = [11, 1]

cards = [2,3,4,5,6,7,8,9,10,10,10,10,"ace"]
print(cards)

# include the ace as a variable inside the list
# after random choice >> 
# if the list includes ace calculate the total without ace
# if 21-total is greater than 11 than ace = 11
# else if 21-total is less than 11 than ace = 1



# player_cards = random.choices(cards,k=2)
player_cards = ["ace", 5]
dealer_cards = random.choices(cards,k=2)

print(f"Your Cards are : {player_cards}")
print(f"Dealer Card: {dealer_cards}")


# Ace Calculation logic

# def ace_function(cards_list):
#     if "ace" in cards_list:
#         cards_list.remove("ace")
#         print(cards_list)
        
#         difference = 21 - sum(cards_list)
        
#         if difference >= 11:
#             # print(f"difference V1 is {difference}")
#             ace_val = 11
#             # cards_list.append(ace_val)
#             # print(cards_list)
#         elif difference < 11:
#             # print(f"difference V2 is {difference}")
#             ace_val = 1
#         cards_list.append(ace_val)
#         print(cards_list)
#     return cards_list

def ace_function(cards_list):
    new_cards = []

    # Initially consider every Ace as 11
    for card in cards_list:
        if card == "ace":
            new_cards.append(11)
        else:
            new_cards.append(card)

    total = sum(new_cards)

    # Change Ace from 11 to 1 if necessary
    while total > 21 and 11 in new_cards:
        new_cards.remove(11)
        new_cards.append(1)
        total = sum(new_cards)

    return new_cards

# Card Dealing Function
def deal_cards(cards_list):
    return cards_list.append(random.choice(cards))


# Score Calculation Function
def calculate_score(cards_list):
    ace_function(cards_list)
    total = int(sum(cards_list))
    return total


# Player Turn
# def player_turn():
player_turn = True
player_ingame = True

while player_turn:
    player_input = str(input("Do you want a hit, y or n: \n").lower())
    total = calculate_score(player_cards)
    if player_input == "n":
        if total > 21 :
            print(f"You Lose. Your total is {total}.")
            player_ingame = False
            player_turn = False
        elif total == 21:
            print(f"BlackJack. Player Wins. \nScore: {total}")
            player_ingame = False
            player_turn = False       
        print("Dealer Turn")
        player_turn = False
    elif player_input == "y":
        # total = calculate_score(player_cards)
        if total < 21:    
            deal_cards(player_cards)
            print(player_cards)
        elif total > 21 :
            player_ingame = False
            print(f"You Lose. Your total is {total}.")
            player_turn = False
        elif total == 21:
            print(f"BlackJack. Player Wins. \nScore: {total}")
            player_ingame = False
            player_turn = False

player_score = calculate_score(player_cards)
print(f"Player Cards: {player_cards}, Player Score is {player_score}.")
# return player_score


# Dealer Turn
# def dealer_turn():
dealer_score = calculate_score(dealer_cards)
print(f"Dealer Score : {dealer_score}")

while dealer_score < 17 and player_ingame:
    
    deal_cards(dealer_cards)
    dealer_score = calculate_score(dealer_cards)

if dealer_score > 21:
    print(f"Player Wins. Dealer Score is {dealer_score}.")
elif dealer_score == 21:
    print(f"Dealer Wins. BlackJack. \n Dealer Score is {dealer_score}")
elif dealer_score > player_score:
    print(f"Dealer Wins.\nPlayer Score: {player_score}.\nDealer Score:{dealer_score}")
elif player_score > dealer_score:
    print(f"Player Wins.\nPlayer Score: {player_score}.\nDealer Score:{dealer_score}")