# get 1st bidders details >> name and bid (store)
# ask if any more bidders >> if yes >> continue with getting bidder details
# else tally the stored values and return highest bidder details


def get_bidder_details():
    bidder_details = {"name": [], "bid_value": []}

    name = str(input("Enter your name: "))
    bid_value = int(input("Enter your bid value: "))

    bidder_details["name"].append(name)
    bidder_details["bid_value"].append(bid_value)

    return print(bidder_details)

def auction_program(bidder_details):

    should_continue = True

    while should_continue:
        get_bidder_details()

        restart = str(input("Are there any more bidders, type 'yes' or 'no': " ).lower())

        if restart == "no":
            should_continue = False

            print("GoodBye.")



    return print(bidder_details)

