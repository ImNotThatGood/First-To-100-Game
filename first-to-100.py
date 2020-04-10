# Watch this video before playing: https://www.youtube.com/watch?v=dUXW3Kh_kxo&t=
# The computer will always win so it's not much fun

import os
import time
import random
from termcolor import colored

num = 0
botNum = 0
playerNum = 0
series = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100]
clear = lambda: os.system("clear")
debounce = True
decide = 0
winner = 0

while(True):
	decide = input("Do you want to go 'first' or 'second': ")

	if(decide == "first"):
		decide = "player"
		break
	elif(decide == "second"):
		decide = "bot"
		break
	else:
		print(colored("Enter either the word 'first' or 'second'", "red"))

while(num < 100):

	clear()

	if(decide == 'player'):

		print("Current Number: {0}".format(num))
		print("")

		if(num != 0):
			print("The computer chose: {0}".format(botNum))
			print("")

		while(True):
			while(True):
				try:
					playerNum = int(input("Enter a number between 1-10: "))
				except ValueError:
					print(colored("Do not enter letters or special characters", "red"))
				else:
					break

			if(playerNum >= 1 and playerNum <=10):
				break
			else:
				print(colored("Only enter a number from 1-10", "red"))

		num = num + playerNum

		if(num >= 100):
			winner = "player"
			break

		decide = "bot"
		clear()
	else:
		print("Current Number: {0}".format(num))
		print("")
		print("You chose: {0}".format(playerNum))
		print("")
		print("The computer is choosing...")

		if(num == 0):
			botNum = 1
			debounce = False
		elif(not debounce):
			botNum = 11 - playerNum
		elif(debounce):
			for i in series:
				minNum = i - num
				if(minNum >= 0 and minNum <= 10):
					botNum = minNum
					debounce = False
		else:
			botNum = random.randint(1, 10)

		num = num + botNum
		time.sleep(2)
		decide = "player"

		if(num >= 100):
			winner = "bot"
			break

clear()

if(winner == "player"):
	print(colored("You Won!", "green"))
else:
	print(colored("The Computer Won!", "green"))
