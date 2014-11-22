from os import system
from random import randrange
import speech_recognition as sr
import time

class bcolors:
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	NOCL = '\033[0m'

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