# from replit import clear  (only works in replit)
from blindAuctionArt import logo

# HINT: You can call clear() to clear the output in the console.
print(logo)
bidders = {}
another_bid = "yes"


def collect_bid(name, price):
    bidders[name] = price


def highest_bidder(bidders_dictionary):
    highest_bidder_key = max(bidders_dictionary, key=bidders_dictionary.get)
    return highest_bidder_key


while another_bid == "yes":
    bidders_name = input("What is the bidders name? \n>> ")
    bidders_price = input("What amount would you like to bid? \n>> £")
    another_bid = input("Are there any other bids? yes or no \n>> ")

    collect_bid(bidders_name, bidders_price)
    #clear() (only works in replit)

highest_bid = bidders[highest_bidder(bidders)]
highest_bidder = highest_bidder(bidders)
print(f"The winning bid is £{highest_bid} from {highest_bidder}")


