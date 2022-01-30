import random
ch = ['rock','paper','scissor']
userscore = 0
compuscore = 0
ties = 0
while True:
    user = input ("Enter your choice (rock/paper/scissor): ").lower()
    compu = random.choice(ch)
    print (f"User chose {user} and computer chose {compu}.")
    if user == compu:
        print ("Tie")
        ties += 1
        print (f"User score is {userscore} and computer score is {compuscore}. No. of ties: {ties}")
    elif (user == 'rock' and compu == 'scissor') or (user == 'paper' and compu == 'rock') or (user == 'scissor' and compu == 'paper'):
        print ("User wins")
        userscore += 1
        print (f"User score is {userscore} and computer score is {compuscore}. No. of ties: {ties}")
    else:
        print ("Computer wins")
        compuscore += 1
        print (f"User score is {userscore} and computer score is {compuscore}. No. of ties: {ties}")
    choice = input("Press enter key to continue or input 'quit' to stop: ").lower()
    if choice == 'quit':
        break

# Create two lists/teams of players, print the winner from each team
#['A', 'B', 'C'] vs ['X','Y','Z']
#Random player from each list plays against each other
#Player A wins over Player Y
