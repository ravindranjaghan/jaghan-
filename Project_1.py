import random
choices=["Rock","Paper","Scissors"]
computer=random.choice(choices)
cpu_score=0
player_score=0
while True:
    player=input("Rock,Paper or Scissors").capitalize()
    if player==computer:
        print("Tie!!!")
    elif player=="Rock":
        if computer=="Paper":
            print("You lose!!!",computer,"covers",player)
            cpu_score+=1
        if computer=="Scissors":
            print("You lose!!!",player,"smashes",computer)
            player_score+=1
    elif player=="Paper":
        if computer=="Rock":
            print("You lose!!!",player,"covers",computer)
            player_score+1
        if computer=="Scissors":
            print("You lose!!!",computer,"cuts",player)
            cpu_score+=1
    elif player=="Scissors":
        if computer=="Rock":
            print("You lose!!!",computer,"smashes",player)
            cpu_score+=1
        if computer=="Paper":
            print("You lose!!!",player,"cuts",computer)
            player_score+=1
    else:
        print(cpu_score)
        print(player_score)
        break

