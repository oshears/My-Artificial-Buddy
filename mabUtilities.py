from os import system
from random import randrange
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
		name = fileLines[0][:len(fileLines[0])]
		fileLines.close()
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
