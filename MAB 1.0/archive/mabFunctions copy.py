from os import system
from random import randrange
import time
import mabFaces
import mabConverse

def returnTime():
	fatherTime = ""
	fatherTime = time.strftime("%b:%d:%H:%M:%S")
	fatherTime = fatherTime.split(":")
	return fatherTime

def loginput(userInput):
	fatherTime=returnTime()

	fileRef=open("./logfiles/%s_%s.txt"%(fatherTime[0],fatherTime[1]),"a")
	fileRef.write("%s:%s:%s  "%(fatherTime[2],fatherTime[3],fatherTime[4])+userInput+"\n")
	fileRef.close()



def getName():
	try:
		fileRef = open("./config/mabInfo.txt")
		fileLines = fileRef.readlines()
		name = fileLines[0][:len(fileLines[0])]
		fileLines.close()
	except:
		name = "Isaac"

	return name


def getMood():
	fatherTime=returnTime()
	
	if (int(fatherTime[2])<12):
		system("say I am having a great morning!")
	elif(int(fatherTime[2])<18):
		system("say I am having a great afternoon!")
	elif(int(fatherTime[2])<21):
		system("say I am having a great evening!")
	else:
		system("say I am having a great night!")

	return

def getTime():
	fatherTime=returnTime()
	print("Time: %s:%s"%(fatherTime[2],fatherTime[3]))
	system("say Current time is %s %s"%(fatherTime[2],fatherTime[3]))
	return


def respondInput(userInput):
	if (userInput=="How is your day?" or userInput=="How was your day?" 
		or userInput=="How are you?" or userInput=="How are you"):
		getMood()
		return True
	elif (userInput=="Impress my friends"):
		system("say watch the train go by... choo choo & sl")
		return True
	elif (userInput=="Goodbye" or userInput=="Quit" or userInput=="Bye" or userInput=="See ya"):
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
	elif (userInput=="What time is it?"or userInput=="What time is it"):
		getTime()
		return True
	elif (userInput=="Lets talk"):
		mabConverse.converse()
		return True
	elif (userInput=="Clear"):
		system("clear & say Done!")
		return True
	elif(userInput[0:4]=="Say "):
		try:
			system("say %s"%(userInput[4:]))
		except:
			system("say ...")
		return True
	elif(userInput[:9]=="Show face"):
		print("\n"+mabFaces.getFace(userInput[10:]))
		return True
	elif(userInput[:4]=="Open"):
		system("open%s & say opening"%(userInput[4:]))
		return True
	else:
		system("say I did not recognize your input.")
		return True


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
	
	loginput(userInput)

	userInput=userInput.capitalize()
		
	return respondInput(userInput)
		

def main ():

	randomGreet()
	
	living = True

	while (living):
		living=collectInput()

