bids={}
import os
def clear_console():
    
    if os.name == 'nt':
        clear  = os.system('cls')
bidding_finished =False

def highest_bid(bid_amount):
    amount=0
    winner=""
    for bidder in bid_amount:
        bid_amt=bid_amount[bidder]
        if bid_amt>amount:
            amount=bid_amt
            winner=bidder
    print(f"the winner is {winner} with the bid{amount}")

while not bidding_finished:
    name=input("what is your name")
    price=int(input(("what us your bide ?$")))
    bids[name]=price
    should_continued=input("are any other bidder? 'yes ' or 'no'")
    if should_continued =="no":
        bidding_finished=True
        highest_bid(bids)
    elif should_continued=="yes":
        clear_console()



