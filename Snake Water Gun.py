import random 
from time import sleep

def Game():
    global pcscore
    global p1score
    com_input = random.choice([0,1,2])
    b = {0:"Snake",1:"Water",2:"Gun"}
    pc_choice = b[com_input]
    player_input = int(input("Enter your choice:\n Press\n1 for Snake\n2 for Water\n3 for Gun\n"))
    d = {1:0,2:1,3:2}
    e = d[player_input]
    player_choice = b[e]
    wl_matrix = [["D","L","W"],["L","D","W"],["W","L","D"]]
    result = wl_matrix[e][com_input]
    
    sleep(1)
    print(f"The Player chose {player_choice}")
    sleep(1.5)
    print(f"The Computer chose {pc_choice}")
    sleep(1.5)
    if result == "D":
        print("It's a Draw")
    elif result == "L":
        print("You Lose")
        pcscore+=1
    else:
        print("You Win")
        p1score+=1

while True:
    p1score=0
    pcscore=0
    for i in range(3):
        Game()
        sleep(1.5)
    print(f"Player Score: {p1score}")
    sleep(1.5)
    print(f"Computer Score: {pcscore}")
    sleep(1.5)
    y = input("Do you want to play again?\nPress y or n ")
    if y == "n":    
        
        break