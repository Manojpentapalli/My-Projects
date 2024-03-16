print("Welcome to the secret auction program.")

logo = '''
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

auction=dict()

others=True

while others:
    
    name=input("What is your name?: \n")
    
    bid_price=int(input("What's your bid?: \n"))
    
    auction[name]=bid_price
    
    others_exist=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    if others_exist=="no":
        others=False
        print("\033[H\033[J")
    else:
        print("\033[H\033[J")

#print(auction)

highest_bid=0

winner=""

for i in auction:
    
    bid_amount=auction[i]
    
    if bid_amount>highest_bid:
        highest_bid=bid_amount
        winner=i
        
print(f"""The winner is {winner} with a bid of ${highest_bid}.""")
    
     