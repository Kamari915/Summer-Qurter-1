def Rps():
    print("Weelcome to rock, paper sissiors!")
    player1 =input("player1 please enter your name:")
    player2 =input("player2 please enter your name:")

    p1_Choice = input(f"{player1}, choose betwen rock, paper sissiors")

    while not isvalidmove(p1_Choice):
        print("invalidmove!please try again")
        p1_Choice = input(f"{player1}, choose betwen rock, paper sissiors")

    p2_Choice = input(f"{player2}, choose betwen rock, paper sissiors")

    while not isvalidmove(p2_Choice):
        print("invalidmove! please try again")
        p2_Choice = input(f"{player2}, choose betwen rock, paper sissiors")

    if p1_Choice == p2_Choice:
        print("it's a draw!")

    if p1_Choice == "rock" and p2_Choice =="sissiors":
        print(f"Rock beats sissiors, {player1} wins!")

    elif p1_Choice == "paper" and p2_Choice =="rock":
        print(f"paper beats rock, {player1} wins!")

    elif p1_Choice == "sissiors" and p2_Choice =="paper":
        print(f"sissiors beats paper, {player1} wins!")

    elif p2_Choice == "rock" and p1_Choice =="sissiors":
        print(f"Rock beats sissiors, {player2} wins!")

    elif p2_Choice == "paper" and p1_Choice =="rock":
        print(f"paper beats rock, {player2} wins!")
         
    elif p2_Choice == "sissiors" and p1_Choice =="paper":
        print(f"sissiors beats paper, {player2} wins!")

def isvalidmove(playermove):
   validMoves=["rock", "paper", "sissiors"] 

   if playermove in validMoves:
       return True
   else:
       return False 

Rps()