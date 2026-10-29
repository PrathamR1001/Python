# Empty Dict
bid_detailed_dict = {}

# Function to get details and store in empty dict

def get_details():
    
    name = str(input("Enter your name: \n").lower())
    bid_value = int(input("Enter your bid value: \n"))

    bid_detailed_dict[name] = bid_value

    return bid_detailed_dict


# Run and check if continue

def auction_program():
    should_continue = True

    while should_continue:

        get_details()

        max_bid = 0
        highest_bidder = ""
        # for k,v in bid_detailed_dict.items():
        #     if v[0] > max_bid:
        #         max_bid = v[0]
        #         highest_bidder = k
        for key in bid_detailed_dict:
            bid_amount = bid_detailed_dict[key]
            if bid_amount > max_bid:
                max_bid = bid_detailed_dict[key]
                highest_bidder = key
        
             
        restart = str(input("Are there any more bidders, 'yes' or 'no': \n"))
        if restart == 'no':
                print(f"Highest bidder was {highest_bidder} with bid of ${max_bid}")
                should_continue = False
        elif restart == 'yes':
            print("\n" * 100)

auction_program()


