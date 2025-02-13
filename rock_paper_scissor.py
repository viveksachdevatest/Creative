import random

apr = ("rock", "paper", "scissor")
comp = random.choice(apr)

user = str(input("provide your input from rock, paper, scissor \n"))
user = user.lower()
print(user)

if ((user != "rock") and (user != "scissor") and (user != "paper")):
    print(f"incorrect input, kindly try again \n")
    exit()

print(f"computer choose {comp}")
if (user == "rock"):
    if (comp == "rock"):
        print(f"It's a tie \n")
        exit()
    elif (comp == "paper"):
        print(f"You lose and Computer wins \n")
        exit()
    else:
        print(f"You Win and Computer loses \n")
        exit()
elif (user == "paper"):
    if (comp == "paper"):
        print(f"It's a tie \n")
        exit()
    elif (comp == "scissor"):
        print(f"You lose and Computer wins \n")
        exit()
    else:
        print(f"You Win and Computer loses \n")
        exit()
else:
    if(comp=="scissor"):
        print(f"It's a tie \n")
        exit()
    elif(comp == "rock"):
        print(f"You lose and Computer wins \n")
        exit()
    else:
        print(f"You Win and Computer loses \n")
        exit()

