My Artificial Buddy
===================

A robot with conversational intelligence.

Designed and Programmed by Osaze Shears.
```
000000000000000000                          000                 000              111           55555555555555
0000 00000000 0000                          000               000               111           55555555555555       
00 000000000000 00                          000             000                111           555
0 000   00   000 0                          000           000                 111           555
00000   00   00000                          000         000                  111           55555555555555           
000000000000000000                          000       000                   111           55555555555555
000000000000000000                          000     000                    111                      555
0000         00000                          000   000                     111                      555
000000     0000000                          000 000        000           111   000     55555555555555
000000000000000000                          000          000           111   000     55555555555555
```

Project Goal
------------
The goal of this project is to create a robot with the ability to talk fluently and accurately with its human user. The project is built in Python an uses the [Python Speech Recognition](https://pypi.python.org/pypi/SpeechRecognition/) library. In addition to this, it also makes use of the  [Speech Synthesis Manager](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/say.1.html) that comes built in with OSX. Essentially the project works by listening for a recognized input from the user and acts according to that input. If the user were to say "What time is it?", the program would process the collected audio by sending it to `Google's Speech Recognition Servers`, and use the results from the server to determine which command to perform.



Current Features
----------------
* Voice Recognition Ability
* Currently Supported Commands
  * "What time is it?"
  * "Show face [Face]" ["greet face", "standard face", "inquisitive face", "aperature face"]
  * "Say [Words]" [Any thing you want it to say]
  * "What is your name?"
  * "Clear!"
  * "Respond silently."
  * "Do not respond silently."
  * "Stop listening!"
  * "Open [Application" [Any application in the directory]
  * "Aperature!"
  * "Let's talk."
  * "Impress my friends!"
  * "What is the temperature?"
  * "Run updated version."
  

Controls
--------
Simply execute the program by navigating to the `\My Artificial Buddy\` directory and typing `python3 mabMain.py` The program will then start listening for user commands. These commands must be on the list of recognized commands, otherwise the program perform the default response.


Planned Additions
-----------------
* More user commands
* Offline support for voice recognition
 * This could possibly be done by using the [NSSpeechRecognizer](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/Speech/Articles/RecognizeSpeech.html) library that comes built in with OSX
* Adjustable sensitivity threshold for collecting sound
* More customability options


Requirements
------------
* `PyAudio`
* A FLAC encoder
* `Python SpeechRecognition Library`
* POSIX Python Module
* An Internet Connection

Recommended Configuration
-------------------------
* Add the alias `mab.run` to your `.bash_profile` which executes `python3 mabMain.py`
 * This allows the "Run updated version" command to execute properly

Change Log
----------
* Version 1.0 - Text Input with Standard Commands
* Version 1.5 - Voice Input replaces Text Input
