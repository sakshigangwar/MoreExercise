import random


def win():
    print("you win!")


def lose():
    print("you lose")


while True:
    player_choise=input("what do you pic?(rock,paper,scissor)=")
    player_choise.strip()
    moves=["rock","paper","scissor"]
    random_move=random.randint(0,2)
    computer_choice=moves[random_move]
    print(computer_choice)
    if player_choise==computer_choice:
        print("draw!")
    elif moves=="rock" and computer_choice=="scissors":
        win()
    elif player_choise=="paper" and computer_choice=="scissors":
        lose()
    elif player_choise=="scissors" and computer_choice=="paper":
        win()
    elif player_choise=="scissor" and computer_choice=="rock":
        lose()
    elif player_choise=="paper" and computer_choice=="rock":
        win()
    elif player_choise=="scissor" and computer_choice=="rock":
        lose()
    aGain=input("Do you want to play again?(y or n) ")
    if aGain=="n":
        break


        
