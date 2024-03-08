print(''' 
Welcome to
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

Your mission is to find the treasure.''')
turn = input("""You are starting at an intersection
type 'R' to turn right, 'L' to turn left and 'S' to go straight. 
choose your path wisely!\n""")
if turn=="L":
    mode=input('''You came across a lake, 
to swim over the lake type "S" or to wait for the boat type "W"\n''')
    if mode=="W":
        door=input('''A boat came and carried you across the lake,
you are now standing on an island facing three doors painted in red, blue and yello.
to enter type "R" for red, "B" for blue and "Y" for yello\n''')
        if door=="Y":
            print("Congratulations! You Win.")
        elif door=="R":
            print("You're burned by fire. Game Over!")
        elif door=="B":
            print("You're eaten by beasts. Game Over!.")
        else:
            print("Game Over!")
    else:
        print("You are attacked by a trout.Game Over!")
else:
    print("You fell into a hole. Game Over!")