import random

player1 = input("Select Rock, Paper or Scissor : ").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Player2 has selected:", player2)

while True:
    if player1 == "rock" and player2 == "paper":
        print("Player2 Won")
        break
    elif player1 == "paper" and player2 == "scissor":
        print("Player2 Won")
        break
    elif player1 == "scissor" and player2 == "rock":
        print("Player2 Won")
        break
    elif player1 == player2:
        print("Tie")
        break
    else:
        print("Player1 Won")
        break
