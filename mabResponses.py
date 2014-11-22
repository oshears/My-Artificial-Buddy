from os import system
from random import randrange
import time
import mabFaces
import mabConverse
import speech_recognition as sr

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

def dormant():
	system("say I will stop listening to you for now")
	ignoring=True

	r = sr.Recognizer()

	while ignoring:
		ignoreR = sr.Recognizer()
		with sr.Microphone() as source:
			ignoreAudio = ignoreR.listen(source)

		try:
			ignoreInput = ignoreR.recognize(ignoreAudio)

		except LookupError:
			ignoreInput = None
		
		if ignoreInput == "start listening":
			ignoring = False
			system("say I am listening to you")

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

	if (int(fatherTime[2])<3):
		system("say I am having a great night!")
	elif (int(fatherTime[2])<12):
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
	if (userInput=="How is your day" or userInput=="How was your day" or userInput=="How are you"):
		getMood()
	elif (userInput=="Impress my friends"):
		system("say watch the train go by... choo choo & sl")
	elif (userInput=="Goodbye" or userInput=="Quit" or userInput=="Bye" or userInput=="See ya"):
		system("say See you soon!")
		return False
	elif (userInput=="What is my current location"):
		system("say I am not yet able to determine your location"+
		 "However, that feature will be coming soon")
	elif (userInput=="What is the weather"):
		system("say I am not yet able to determine the weather"+
			"However, that feature will be coming soon")
	elif (userInput=="What is your name"):
		system("say My name is %s"%(getName()))
	elif (userInput=="What time is it"or userInput=="What time is it"):
		getTime()
	elif (userInput=="Let's talk"):
		mabConverse.converse()
	elif (userInput=="Clear"):
		system("clear & say Done!")
	elif(userInput[0:4]=="Say "):
		try:
			system("say %s"%(userInput[4:]))
		except:
			system("say ...")
	elif(userInput[:9]=="Show face"):
		print("\n"+mabFaces.getFace(userInput[10:]))
	elif(userInput[:4]=="Open"):
		system("open%s & say opening"%(userInput[4:]))
	elif (userInput=="Aperature"):
		for line in mabFaces.aperatureFaceArray:
			print(line)
		system("say The cake is a lie!")
	elif (userInput=="Stop listening"):
		dormant()
	elif (userInput=="Respond silently"):
		system("I will listen, but only respond if I know what you said")
	else:
		system("say Come again?")
		
	return True
