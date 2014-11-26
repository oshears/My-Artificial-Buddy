questionFace=(  "000000000000000000\n"
				"0000 00000000 0000\n"
				"00 000000000000 00\n"
				"0 000   00   000 0\n"
				"00000   00   00000\n"
				"000000000000000000\n"
				"000000      000000\n"
				"00000 000000 00000\n"
				"000000000000000000\n"
				"000000000000000000\n")


happyFace = (	"000000000000000000\n"
				"0000 00000000 0000\n"
				"00 000000000000 00\n"
				"0 000   00   000 0\n"
				"00000   00   00000\n"
				"000000000000000000\n"
				"000000000000000000\n"
				"0000         00000\n"
				"000000     0000000\n"
				"000000000000000000\n")


standardFace = ("000000000000000000\n"
				"00       00      0\n"
				"000000000000000000\n"
				"00000   00   00000\n"
				"00000   00   00000\n"
				"000000000000000000\n"
				"000000000000000000\n"
				"0000          0000\n"
				"000000000000000000\n"
				"000000000000000000\n")


aperatureFace =('             .,-:;//;:=,\n'
				'          . :H@@@MM@M#H/.,+%;,\n'
				'       ,/X+ +M@@M@MM%=,-%HMMM@X/,\n'
				'     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-\n'
				'    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.\n'
				'  ,%MM@@MH ,@%=             .---=-=:=,.\n'
				'  =@#@@@MX.,                -%HX$$%%%:;\n'
				' =-./@M@M$                   .;@MMMM@MM:\n'
				' X@/ -$MM/                    . +MM@@@M$\n'
				',@M@H: :@:                    . =X#@@@@-\n'
				',@@@MMX, .                    /H- ;@M@M=\n'
				'.H@@@@M@+,                    %MM+..%#$.\n'
				' /MMMM@MMH/.                  XM@MH; =;\n'
				'  /%+%$XHH@$=              , .H@@@@MX,\n'
				'   .=--------.           -%H.,@@@@@MX,\n'
				'   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.\n'
				'     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=\n'
				'       =%@M@M#@$-.=$@MM@@@M; %M%=\n'
				'         ,:+$+-,/H#MMMMMMM@= =,\n'
				'               =++%%%%+/:-.')


def getFace(face):

	if ("happy face" in face):
		return happyFace
	
	if ("question face" in face):
		return questionFace

	if ("standard face" in face):
		return standardFace

	if ("aperature face" in face):
		return aperatureFace

	return standardFace