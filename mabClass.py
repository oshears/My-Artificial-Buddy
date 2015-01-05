import mabUtilities
import mabResponses
import mabFaces
import mabUtilities
from os import system
from random import randrange
import speech_recognition as sr

class MAB:
	
	def __init__(self):
		self.responseDatabase=mabUtilities.buildDictionary()
		try:
			fileRef = open("./config/mabInfo.txt")
			fileLines = fileRef.readlines()
			fileRef.close()
			self.inputType = fileLines[1][:len(fileLines[1])]
		except:
			self.inputType = "Text"
		print("Input type is %s"%(self.inputType))

	def rebuildDatabase(self):
		self.responseDatabase=mabUtilities.buildDictionary()

	def standardResponse(self,userInput):
		if (userInput in self.responseDatabase.keys()):
			responseIndex = randrange(0,len(self.responseDatabase[userInput]))
			return self.responseDatabase[userInput][responseIndex] 
		return ("I have run into an error...")

	def randomGreet(self):

		print(mabUtilities.colors.GREEN + mabFaces.happyFace + mabUtilities.colors.NOCOL)
		system("say Good day o saah zee")

		choice = randrange(1,4) 

		print(mabUtilities.colors.BLUE + mabFaces.standardFace + mabUtilities.colors.NOCOL)

		if choice == 1:
			system("say Is there anything I can help you with?")
		elif choice == 2:
			system("say What can I do for you today?")
		elif choice == 3:
			system("say How may I be of service?")
		return


	def collectInput(self,isSilent):
		if (self.inputType=="VocalInput"):
			r = sr.Recognizer()

			r.energy_threshold = 3000

			r.pause_threshold = 1.5

			with sr.Microphone() as source:
				audio = r.listen(source)

			try:
				userInput = r.recognize(audio)
			except KeyError:
				userInput = "N01nt3rn31"
			except LookupError:
				userInput = "##--(system)error: did not understand response.--##"

		else:
			userInput = ""
			userInput=str(input())

		mabUtilities.logInput(userInput)

		userInput=userInput.capitalize()
			
		return mabResponses.respondInput(self,userInput,isSilent)

	def definedResponse(self,userInput):

		choiceIndex = randrange(0,len(self.responseDatabase[userInput]))

		response = self.responseDatabase[userInput][choiceIndex]


		return response

	def main (self):

		self.randomGreet()
		
		living = True

		silentResponse = False

		while (living!=False):

			living=self.collectInput(silentResponse)

			if (living=="silent"):
				silentResponse=True
				living=True

			if (living=="not silent"):
				silentResponse=False
				living=True
