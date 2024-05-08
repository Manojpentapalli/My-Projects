import random

logo= '''
 _______  __   __  _______  _______  _______    __   __  _______    __  
|       ||  | |  ||       ||       ||       |  |  |_|  ||       |  |  | 
|    ___||  | |  ||    ___||  _____||  _____|  |       ||    ___|  |  | 
|   | __ |  |_|  ||   |___ | |_____ | |_____   |       ||   |___   |  | 
|   ||  ||       ||    ___||_____  ||_____  |  |       ||    ___|  |__| 
|   |_| ||       ||   |___  _____| | _____| |  | ||_|| ||   |___    __  
|_______||_______||_______||_______||_______|  |_|   |_||_______|  |__| 

'''

again=False

def compare(): # compares both user input number and computer randomly generated number
    global i, res
    if user>computer:
        res="too high"
        print(res)
    elif user<computer:
        res="too low"
        print(res)
    elif user==computer:
        res="correct guess!"
        i=-1
        print(res)
    return i,res

def guess_again(): # asks user to guess another number if the number does not match computer generated random number
    global user
    user=int(input("guess again: "))
    return user

def game(): # recursion occurs till the chances remaining arw zero (0) and displays the correct number if user fails to guess in respective chances
    global i
    while i>=0:
        compare()
        if i>0:
            guess_again()
            i-=1
        if i==0:
            break
    if res!="correct guess!":
        print('you are out of chances!')
        print(f'the number is {computer}')
        go_again()
    elif res=="correct guess!":
        go_again()

def go_again(): # asks user if they want to play again and resets the game if user input is yes and terminates if it is no.
    global again 
    go_again=input("do you want to play again? type 'y' for yes and 'n' for no: ").lower()
    if go_again=="y":
        user=0 
        print("\033[H\033[J")
    elif go_again=="n":
        again=True
    else:
        print("invalid input")
        again=True

# logic starts

while not again:
    
    print(logo)
    
    computer = random.randint(1,100) # asssigns a random integer between 1 and 100 to the computer
    #print(computer)
    
    level=input("select the level of difficulty, easy or hard: ").lower()
    user=int(input("Guess the number between 1 and 100 chosen by the computer: "))
    
    if user in list(range(1,101)): # checks whether the user input is between 1 and 100
        if level=="easy":
            i=9
            game()
        
        elif level=="hard":
            i=4
            game()
    else:
        print("Guess out of range.")

