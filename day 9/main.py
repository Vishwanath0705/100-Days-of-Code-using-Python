print("Secret Auction Game !!")
auction = {}
def highest_bid(auction_value):
    bid = 0
    for i in auction_value:
        bid_value = auction_value[i]
        if bid_value>bid:
            bid = bid_value
            winner = bid
    print(f"The winner of the auction is {winner}")

end_of_auction = False
while not end_of_auction:
    name = input("Enter the name of the bidder : ")
    bid_value = int(input("Enter the value of the bid : "))
    auction[name] = bid_value
    choice = input("Are there any other bidders?Type 'yes' or 'no' : ")
    if choice=="no":
        end_of_auction = True
        highest_bid(auction)
