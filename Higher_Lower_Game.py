import random

count=0 
game=False
go_again=False
    
f1= open("H_L_game_data.py",'r')
from H_L_game_data import data
# print(data)

f2=open("H_L_game_art.py",'r')
from H_L_game_art import logo, vs 

while not go_again:

    w=False
    
    print(logo)
    
    while not game:
        
        if not w:
            x= random.randint(0,49)
            w=False
        print(f'who do you think have more followers on instagram \nA - {data[x]["name"]}, a {data[x]["description"]}, from {data[x]["country"]}.')
        
        print(vs)
        
        y=random.randint(0,49)
        if y==x:
            y+=1 
        print(f'or B - {data[y]["name"]}, a {data[y]["description"]}, from {data[y]["country"]}.')
        
        user=input("type A or B: ").lower()
        
        if user=="a":
            if data[x]["follower_count"] > data[y]["follower_count"]:
                count+=1
                print(f"correct. your current score is {count}")
                x=y
                w=True
            else:
                game=True
                
        elif user=="b":
            if data[y]["follower_count"] > data[x]["follower_count"]:
                count+=1
                print(f"correct. your current score is {count}")
                x=y
                w=True
            else:
                game=True
                
        else:
            game=True
        
    print("wrong")        
    print(f"your score: {count}")
    
    again=input("want to play again? type 'y' for yes and 'n' for no: ").lower()
    if again=="y":
        count=0
        game=False
        print("\033[H\033[J")
    elif again=="n":
        go_again=True 
        
