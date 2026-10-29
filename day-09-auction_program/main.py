bid_detailed_dict = {}

def get_details():
    
    name = str(input("Enter your name: \n").lower())
    bid_value = int(input("Enter your bid value: \n"))

    bid_detailed_dict[name] = [bid_value]

    return bid_detailed_dict


def auction_program():
    should_continue = True

    while should_continue:

        get_details()

        max_bid = 0
        highest_bidder = ""
        for k,v in bid_detailed_dict.items():
            if v[0] > max_bid:
                max_bid = v[0]
                highest_bidder = k

        restart = str(input("Are there any more bidders, 'yes' or 'no': \n"))
        if restart == 'no':
                print(f"Highest bidder was {highest_bidder} with bid of ${max_bid}")
                should_continue = False

auction_program()
