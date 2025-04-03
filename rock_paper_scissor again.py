import random

choice = ("rock", "paper", "scissor")
user_input = input("Kindly input your choice from rock, paper, scissor \n")
user = str(user_input)

if user != "rock" and user != "paper" and user != "scissor":
    print(f"You have input incorrect values \n")
    exit()
else:
    print(f" Correct input from user, proceeding forward")

comp = random.choice(choice)
print(f" computer choose {comp}")

if user == comp:
    print(f"It's a tie between you and computer")
    exit()
elif (user == "rock" and comp == "scissor") or (user == "scissor" and comp == "paper") or (user == "paper" and comp == "rock"):
    print(f"You input {user} and computer selected {comp}. You win \n")
    exit()
else:
    print(f"You input {user} and computer selected {comp}. You lose \n")
    exit()