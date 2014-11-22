from os import system
from random import randrange
import mabFaces
import mabConverse
import mabUtilities
import speech_recognition as sr

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

def getMood():
	fatherTime=mabUtilities.returnTime()

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

def respondInput(userInput,areSilent):
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
	elif (userInput=="What is the temperature"):
		mabUtilities.getTemp()
	elif (userInput=="What is your name"):
		system("say My name is %s"%(mabUtilities.getName()))
	elif (userInput=="What time is it"or userInput=="What time is it"):
		mabUtilities.getTime()
	elif (userInput=="Let's talk"):
		mabConverse.converse()
	elif (userInput=="Clear"):
		system("clear & say Done!")
	elif(userInput[0:4]=="Say "):
		try:
			system("say \"%s\""%(userInput[4:]))
		except:
			system("say ...")
	elif(userInput[:9]=="Show face"):
		print("\n"+mabUtilities.bcolors.PURPLE+mabFaces.getFace(userInput[10:]+mabUtilities.bcolors.NOCL))
	elif(userInput[:4]=="Open"):
		system("open%s & say opening"%(userInput[4:]))
	elif (userInput=="Aperature"):
		for line in mabFaces.aperatureFaceArray:
			print(mabUtilities.bcolors.RED+line+mabUtilities.bcolors.NOCL)
		system("say The cake is a lie!")
	elif (userInput=="Stop listening"):
		dormant()
	elif (userInput=="Respond silently"):
		system("say I will listen, but only respond if I know what you said")
		return "silent"
	elif (userInput=="Do not respond silently"):
		system("say I will always respond to what you say")
		return "not silent"
	elif (userInput=="##--(system)error: did not understand response.--##"):
		if not areSilent:
			system("say I am having a hard time understanding you")
	elif (userInput=="Run updated version"):
		try:
			system("osascript -e 'tell application \"Terminal\" to activate' -e 'tell application \"System Events\" to tell process \"Terminal\" to keystroke \"t\" using command down' -e 'tell application \"Terminal\" to do script \"python3 mabMain.py\" in selected tab of the front window'")
		except:
			system("say I am unable to do this right now.")
		return False
	else:
		if not areSilent:
			system("say Ummm, come again?")

	return True
