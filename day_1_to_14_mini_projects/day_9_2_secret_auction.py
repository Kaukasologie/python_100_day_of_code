logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

continue_bidding = True
bids_data = {}

while continue_bidding:
    name = input("What is your name?:\n--->> ")
    price = int(input("What is your bid?:\n--->> $"))
    bids_data[name] = price
    if input("\nAre there any other bidders? Type 'Yes' or 'No'.\n--->> ").lower() != "yes":
        continue_bidding = False
    else:
        print("\n" * 1)

highest_bid = 0
winner = ""

for bid in bids_data:
    if bids_data[bid] > highest_bid:
        highest_bid = bids_data[bid]
        winner = bid

print(f"\nThe winner is {winner} with a bid of ${highest_bid}")
