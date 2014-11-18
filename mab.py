from os import system
from random import randrange
from multiprocessing import Process
import time

def getName():
	try:
		fileRef = open("mabInfo.txt")
		fileLines = fileRef.readlines()
		name = fileLines[0][:len(fileLines[0])]
	except:
		name = "Isaac"

	return name

def getMood():

	system("say I am having a great day today!")

def getTime():
	fatherTime = ""
	fatherTime = time.strftime("%I:%M:%S")
	fatherTime = fatherTime.split(":")
	fatherTime = [int(fatherTime[0]),int(fatherTime[1]),int(fatherTime[2])]
	print("Time: %s:%s"%(fatherTime[0],fatherTime[1]))
	system("say Current time is %s %s"%(fatherTime[0],fatherTime[1]))


def respondInput(userInput):
	
	if (userInput=="How is your day?"):
		getMood()
		return True
	elif (userInput=="Impress my friends"):
		system("say watch the train go by... choo choo & sl")
		return True
	elif (userInput=="Goodbye" or userInput=="Quit" or userInput=="Bye"):
		system("say See you soon!")
		return False
	elif (userInput=="What is my current location?"):
		system("say I am not yet able to determine your location"+
		 "However, that feature will be coming soon")
		return True
	elif (userInput=="What is the weather?"):
		system("say I am not yet able to determine the weather"+
			"However, that feature will be coming soon")
		return True
	elif (userInput=="What is your name?"):
		system("say My name is %s"%(getName()))
		return True
	elif (userInput=="What time is it?"):
		getTime()
		return True
	else:
		system("say I did not recognize your input.")
		return True

def randomGreet():

	system("say Good day o sa zee")

	choice = randrange(1,4) 

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
		
	userInput=userInput.capitalize()
		
	return respondInput(userInput)
		

def main ():

	randomGreet()
	
	living = True

	while (living):
		living=collectInput()

##Run the program

main()