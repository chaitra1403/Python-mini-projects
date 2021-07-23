#import required libraries

import random #random number generator form 1 to 3
import matplotlib.pyplot as plt #to plot the graph of scores
import pylab as p

#declare list to store the score of user and computer initial score is 0 for each
data=[0,0]
print("Winning Rules of the Rock paper scissor game as follows: \n\vRock vs paper->paper wins \n\vRock vs scissor->Rock wins\n\vpaper vs scissor->scissor wins \n")

while True:
	print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 
	choice = int(input("User turn: "))
	while choice > 3 or choice < 1:
		choice = int(input("enter valid input: "))
	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'

	print("user choice is: " + choice_name)

	print("\nNow its computer turn.......")
	comp_choice = random.randint(1, 3) #computer chooses a random number(1,3)

	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'

	print("Computer choice is: " + comp_choice_name)
	print(choice_name + " V/s " + comp_choice_name)

	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):
		print("paper wins => ", end = "")
		result = "paper"
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)):
		print("Rock wins =>", end = "")
		result = "Rock"
	elif((choice==1 and comp_choice==1) or (choice==2 and comp_choice==2) or (choice==3 and comp_choice==3)):
		print("ITS A DRAW")
		result="draw"
	else:
		print("scissor wins =>", end = "")
		result = "scissor"
	if result == choice_name:
		print("<== User wins ==>")
		data[0]=data[0]+1
	else:
		if(not(result=="draw")):
			print("<== Computer wins ==>")
			data[1]=data[1]+1
	print("Do you want to play again? (Y/N)")
	ans = input()
	if ans == 'n' or ans == 'N':
		break

print("\nThanks for playing")
if(data[0]>data[1]):
	print("-------------------User is the Winner---------------------------\n")
else:
	print("-------------------Computer is the winner-----------------------\n")

print("User Wins {} times".format(data[0]))
print("Computer wins {} times".format(data[1]))
dat=[1,2]
da=[data[0],data[1]]
labe=["wins","lost"]
p.bar(dat,da,align="center")
p.xticks(dat,labe)
p.show()


