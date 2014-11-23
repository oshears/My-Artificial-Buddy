import mabResponses
import mabFaces
import mabUtilities
from os import system
from random import randrange
import speech_recognition as sr

def randomGreet():

	print(mabUtilities.bcolors.GREEN + mabFaces.greetFace + mabUtilities.bcolors.NOCL)
	system("say Good day o sa zee")

	choice = randrange(1,4) 

	print(mabUtilities.bcolors.BLUE + mabFaces.standardFace + mabUtilities.bcolors.NOCL)

	if choice == 1:
		system("say Is there anything I can help you with?")
	elif choice == 2:
		system("say What can I do for you today?")
	elif choice == 3:
		system("say How may I be of service?")
	return


def collectInput(isSilent):

	r = sr.Recognizer()

	r.energy_threshold = 3000

	r.pause_threshold = 1.2

	with sr.Microphone() as source:
		audio = r.listen(source)

	try:
		userInput = r.recognize(audio)
	except KeyError:
		userInput = "No internet"
	except LookupError:
		userInput = "##--(system)error: did not understand response.--##"


	#userInput = ""
	
	#userInput=str(input())

	mabUtilities.logInput(userInput)

	userInput=userInput.capitalize()
		
	return mabResponses.respondInput(userInput,isSilent)
		

def main ():

	randomGreet()
	
	living = True

	silentResponse = False

	while (living!=False):

		living=collectInput(silentResponse)

		if (living=="silent"):
			silentResponse=True
			living=True

		if (living=="not silent"):
			silentResponse=False
			living=True
