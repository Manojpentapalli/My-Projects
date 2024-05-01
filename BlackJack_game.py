import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer=[] 
user=[] 
repeat=False
again=False
count=0

def draw(): #to draw random card from given deck of cards
    x=random.choice(cards)
    return x
    
def bjcheck(): #checks either computer or user cards add up to be (21) which counts as blackjack 
    global repeat
    if sum(computer)==21:
        repeat=True
        print(f'computer = {computer}')
        print(f'user = {user}')
        print("You lose! Computer got a Blackjack.")
        
    elif sum(user)==21:
        repeat=True
        print(f'computer = {computer}')
        print(f'user = {user}')
        print("You won! You got a Blackjack.")
        
    elif sum(computer)==21 and sum(user)==21:
        repeat=True
        print(f'computer = {computer}')
        print(f'user = {user}')
        print("it's a tie")
        
def anothercard(): #asks user whether they would like to draw another card, if yes draws a random card using draw() funtion and appends it to the user list, if no then computers gets random cards added to its list till the sum of computer list adds up to 17 or higher
    global repeat
    card=input("would you like to draw another card? type 'Y' for yes or 'N' for no: ")
    if card.lower()=="y":
        user.append(draw())
        print(f'user = {user}')
    elif card.lower()=="n":
        repeat=True
        while sum(computer)<17:
            computer.append(draw())
        final()
            
def final(): #compares the scores of both user and computer at the end after drawing cards
    print(f'computer = {computer}')
    print(f'user = {user}')
    
    if sum(computer)>21:
        print("You Won!")
    
    elif sum(computer)<21:
        if sum(computer)<sum(user):
            print("You won!")
        elif sum(user)<sum(computer):
            print("You lose! Computer won")
        elif sum(user)==sum(computer):
            print("it's a tie")
            
    elif sum(computer)==21:
        print("You lose! Computer got a Blackjack.")

#logic starts

while not again:
    
    for i in range(2): #appends 2 random cards to both computer and user
        computer.append(draw())
        user.append(draw())
    
    print(logo)
    
    print(f'computer = {[computer[0]]}') #displays only first card of computer according to the game rules
    
    print(f'user = {user}')
    
    while not repeat:
    
        bjcheck()
            
        if sum(user)>21:
            for i in user:
                if i==11: # checks whether the list has an ace (11) card so that it removes ace card and appends '1' card to the list
                    user.remove(11)
                    user.append(1)
                    if sum(user)>21:
                        print("You lose!")
                        repeat=True
                    else:
                        anothercard()
                        print(f'user = {user}')
                    
                elif i!=11:        
                    count+=1
                    if count==len(user):
                        print(f'computer = {computer}')
                        print(f'user = {user}')
                        print("You lose!")
                        repeat=True
            
        elif sum(user)<21:
            anothercard()
    
    go_again=input("Do you want to play again? type 'Y' for yes or 'N' for no: ") 
    
    if go_again=='n':
        again=True
    elif go_again=='y':
        print("\033[H\033[J") #clears the screen before staring the game again 
        computer.clear()
        user.clear()
        repeat=False

