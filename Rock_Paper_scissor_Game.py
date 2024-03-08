import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("type 0 to choose rock, 1 to choose paper, 2 to choose scissors:\n"))
def p_c(player_choice):
    global player
    player=0
    if player_choice>2 or player_choice<0:
        print("Invalid choice, You lose!")
        player="NA"
    elif player_choice==0:
        player=0
        print(f''' You chose 
        {rock}''')
    elif player_choice==1:
        player=1
        print(f'''You chose
        {paper}''')
    elif player_choice==2:
        player=2
        print(f'''You chose
        {scissors}''')
    return 0
    
computer_choice=random.randint(0,2)
def c_c(computer_choice):
    global computer
    computer=0
    if computer_choice==0:
        computer=0
        print(f'''computer chose 
        {rock}''')
    elif computer_choice==1:
        computer=1
        print(f'''computer chose
        {paper}''')
    elif computer_choice==2:
        computer=2
        print(f''' computer chose
        {scissors}''')
    return 0
p_c(player_choice)
if player!="NA":
    c_c(computer_choice)

if computer_choice==2:
    if player_choice==0:
        player=3
if player_choice==2:
    if computer_choice==0:
        computer=3

if player=="NA":
    None
elif computer>player:
    print("You Lose")
elif computer==player:
    print("Its a tie!")
else:
    print("You Won!")
    

