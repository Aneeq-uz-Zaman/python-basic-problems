import random
rNO=random.randint(1,3)
print("Computer's turn Rock(R),Paper(P)&Scissor(S)")
if rNO==1:
    comp="R"
elif rNO==2:
    comp="P"
else:
    comp="S"
player=input("Yours turn Press (P) for Paper,(R) for rock,(S) for scissor : ")
print(f"Computer choose : {comp}")
print(f"You choose : {player}")
if comp==player:
    print("Tie")
if comp=="R":
    if player=="P":
       print("You wins")
    elif player== "S":
        print("Computer wins")
if comp=="P":
    if player=="S":
       print("You wins")
    elif player== "R":
        print("Computer wins")
if comp=="S":
    if player=="R":
       print("You wins")
    elif player== "P":
        print("Computer wins")
