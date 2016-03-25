""" TODO : reentry of placeholder numbers should not be allowes
prints shuld be onto same board
winning and loosing
"""
import subprocess
tttoe = [range(5) for x in range(5)]
subprocess.call("clear")
def printBoard():
	var = ""
	for i in range(5):
		for j in range(5):
			var += tttoe[i][j]
		print var
		var = ""

def boardInit():
	placeHolder = 1
	for i in range(5):
		for j in range(5):
			if i % 2 == 0:
				if j % 2 == 0:
					tttoe[i][j] = str(placeHolder)
					placeHolder += 1
				else:
					tttoe[i][j] = "|"
			else:
				tttoe[i][j] = "-"
boardInit()
printBoard()

placeHolders = { 1 : [0,0],
				 2 : [0,2],
				 3 : [0,4],
				 4 : [2,0],
				 5 : [2,2],
				 6 : [2,4],
				 7 : [4,0],
				 8 : [4,2],
				 9 : [4,4] }

thisRun = placeHolders
for i in range(4):
	x = input("Player 1 What number do you want? ")
	tttoe[placeHolders[x][0]][placeHolders[x][1]] = "X"
	del thisRun[x]
	printBoard()

	o = input("Player 2 What number do you want? ")
	tttoe[placeHolders[o][0]][placeHolders[o][1]] = "O"
	del thisRun[o]
	printBoard()
