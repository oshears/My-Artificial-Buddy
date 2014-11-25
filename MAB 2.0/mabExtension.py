from Foundation import *
import AppKit
import sys
import mabClass
import mabResponses

class SRDelegate(NSObject):

	myBuddy=mabClass.MAB()

	def speechRecognizer_didRecognizeCommand_(self,sender,cmd):
		print ("speechRecognizer_didRecognizeCommand_", cmd)

		if (cmd == "Quit the test."):
			sys.exit()
		mabResponses.respondInput(self.myBuddy,cmd,False)




recog = AppKit.NSSpeechRecognizer.alloc().init()
recog.setCommands_( [
		"Test the speech recognizer.",
		"What is the airspeed velocity of an unladen swallow?",
		"What is your quest?",
		"What is the capital of Assyria?",
		"Quit the test.",
		"I LOVE YOU!",
		"How is your day"
		"How was your day",
		"How are you",
		"Impress my friends",
		"Goodbye",
		"Quit",
		"Bye",
		"See ya",
		"What is my current location",
		"What is the temperature",
		"What is your name",
		"What time is it",
		"Let's talk",
		"Clear",
		"Say testing",
		"Are you better than siri",
		"Aperature",
		"Stop listening",
		"Respond silently",
		"Shut up",
		"Do not respond silently",
		"Rebuild database"
		])
		
recog.setListensInForegroundOnly_(False)
d = SRDelegate.alloc().init()
recog.setDelegate_(d)


print ("Listening...")
recog.startListening()

# Now we need to enter the run loop...
runLoop = NSRunLoop.currentRunLoop()
runLoop.run()