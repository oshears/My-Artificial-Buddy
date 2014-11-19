import mabResponses
import mabFaces
from os import system
from random import randrange

def randomGreet():

	print(mabFaces.greetFace)
	system("say Good day o sa zee")

	choice = randrange(1,4) 

	print(mabFaces.standardFace)

	if choice == 1:
		system("say Is there anything I can help you with?")
	elif choice == 2:
		system("say What can I do for you today?")
	elif choice == 3:
		system("say How may I be of service?")
	return


def collectInput():
	
	userInput = ""
	
	userInput=str(input())
	
	mabResponses.loginput(userInput)

	userInput=userInput.capitalize()
		
	return mabResponses.respondInput(userInput)
		

def main ():

	randomGreet()
	
	living = True

	while (living):
		living=collectInput()

