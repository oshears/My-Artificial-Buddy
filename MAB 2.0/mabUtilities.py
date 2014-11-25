from os import system
import speech_recognition as sr
import time

class colors:
	MAGENTA = '\x1b[35m'
	BLUE = '\x1b[34m'
	CYAN = '\x1b[36m'
	WHITE = '\x1b[37m'
	GREEN = '\x1b[32m'
	YELLOW = '\x1b[33m'
	RED = '\x1b[31m'
	NOCOL = '\x1b[0m \x1b[49m'

def returnTime():
	fatherTime = ""
	fatherTime = time.strftime("%b:%d:%H:%M:%S")
	fatherTime = fatherTime.split(":")
	return fatherTime

def getTime():
	fatherTime=returnTime()
	print("Time: %s:%s"%(fatherTime[2],fatherTime[3]))
	system("say Current time is %s %s"%(int(fatherTime[2]),fatherTime[3]))
	return

def getName():
	try:
		fileRef = open("./config/mabInfo.txt")
		fileLines = fileRef.readlines()
		fileRef.close()
		name = fileLines[0][:len(fileLines[0])]
	except:
		name = "Isaac"

	return name

def logInput(userInput):
	fatherTime=returnTime()

	fileRef=open("./logfiles/%s_%s.txt"%(fatherTime[0],fatherTime[1]),"a")
	fileRef.write("%s:%s:%s  "%(fatherTime[2],fatherTime[3],fatherTime[4])+userInput+"\n")
	fileRef.close()

def getTemp():
	system("./config/weatherscript.sh > ./temp/weather.txt & ./config/weatherscript.sh")
	system("say -f ./temp/weather.txt")
	system("rm ./temp/weather.txt")

def buildDictionary():
	try:
		fileRef=open("./input_database/standardResponses.csv")
		fileLines = fileRef.readlines()
		fileRef.close()
	except:
		return {}

	stdResponses = {}
	try:
		for lineIndex in range(len(fileLines)):
			fileLines[lineIndex]=fileLines[lineIndex].split("[")
			fileLines[lineIndex]=[fileLines[lineIndex][0],fileLines[lineIndex][1].split(",")]
			lenLast = len(fileLines[lineIndex][1][len(fileLines[lineIndex][1])-1])
			fileLines[lineIndex][1][len(fileLines[lineIndex][1])-1]=fileLines[lineIndex][1][len(fileLines[lineIndex][1])-1][:lenLast-2]
			
			fixed=[]
			for responseElement in fileLines[lineIndex][1]:
				for strIndex in range(len(responseElement)-1,-1,-1):
					if (responseElement[strIndex]=="\""):
						responseElement=responseElement[:strIndex]+responseElement[strIndex+1:]
				fixed.append(responseElement)
			fileLines[lineIndex][1]=fixed

			for strIndex in range(len(fileLines[lineIndex][0])-1,-1,-1):
				if (fileLines[lineIndex][0][strIndex]=="\"" or fileLines[lineIndex][0][strIndex]==","):
					fileLines[lineIndex][0]=fileLines[lineIndex][0][:strIndex]+fileLines[lineIndex][0][strIndex+1:]

			stdResponses.update({fileLines[lineIndex][0]:fileLines[lineIndex][1]})
	except:
		return {}
		
	return stdResponses




