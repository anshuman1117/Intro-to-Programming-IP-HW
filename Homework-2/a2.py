# ANSHUMAN SINGH
# 2017025
# Section A - Group 2

import random
import gvb

#Assignment-2, Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.

Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.

Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""
"""
# There are 2 players: player1 and player2
player1=1  : Has now been declared in another module gvb.py
player2=2  : Has now been declared in another module gvb.py


# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2

tile1= 0     : Has now been declared in another module gvb.py
tile2= 0	 : Has now been declared in another module gvb.py	
tile3= 0	 : Has now been declared in another module gvb.py
tile4= 0	 : Has now been declared in another module gvb.py
tile5= 0	 : Has now been declared in another module gvb.py
tile6= 0	 : Has now been declared in another module gvb.py
tile7= 0	 : Has now been declared in another module gvb.py
tile8= 0	 : Has now been declared in another module gvb.py
tile9= 0	 : Has now been declared in another module gvb.py
"""
# turn variable defines whose turn is now
#turn = player1 : Has now been declared in another module gvb.py

def validBoard():
	""" Return True if board state is valid.
		
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""
	if(gvb.tick1>=gvb.tick2):
		return True
	else:
		return False

def validmove(move):
	"""
	 Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
	A move is valid if the corresponding tile for the move is not ticked."""
	
	if(move == 1 and gvb.tile1 == 0):
		return True
	elif(move == 2 and gvb.tile2 == 0):
		return True
	elif(move == 3 and gvb.tile3 == 0):
		return True
	elif(move == 4 and gvb.tile4 == 0):
		return True
	elif(move == 5 and gvb.tile5 == 0):
		return True
	elif(move == 6 and gvb.tile6 == 0):
		return True
	elif(move == 7 and gvb.tile7 == 0):
		return True
	elif(move == 8 and gvb.tile8 == 0):
		return True
	elif(move == 9 and gvb.tile9 == 0):
		return True
	else:
		return False


def takeStrategicMove():
	""" Returns a tile number from the set of unchecked tiles
	using some rules.
	"""
	if(gvb.turn==gvb.player1):
		

		if(gvb.tile3!=2 and gvb.tile1 == 1 and gvb.tile2 == 1):
			return(3)
		elif(gvb.tile2!=2 and gvb.tile1==1 and gvb.tile3==1):
			return(2)
		elif(gvb.tile1!=2 and gvb.tile2==1 and gvb.tile3 == 1):
			return(1)

		elif(gvb.tile6!=2 and gvb.tile4 == 1 and gvb.tile5 == 1):
			return(6)
		elif(gvb.tile5!=2 and gvb.tile4==1 and gvb.tile6==1):
			return(5)
		elif(gvb.tile4!=2 and gvb.tile5==1 and gvb.tile6 == 1):
			return(4)

		elif(gvb.tile8!=2 and gvb.tile9 == 1 and gvb.tile7 == 1):
			return(8)
		elif(gvb.tile7!=2 and gvb.tile9==1 and gvb.tile8==1):
			return(7)
		elif(gvb.tile9!=2 and gvb.tile7==1 and gvb.tile8 ==1):
			return(9)

		elif(gvb.tile7!=2 and gvb.tile1 == 1 and gvb.tile4 == 1):
			return(7)
		elif(gvb.tile4!=2 and gvb.tile1==1 and gvb.tile7==1):
			return(4)
		elif(gvb.tile1!=2 and gvb.tile4==1 and gvb.tile7 == 1):
			return(1)

		elif(gvb.tile8!=2 and gvb.tile5 == 1 and gvb.tile2 == 1):
			return(8)
		elif(gvb.tile2!=2 and gvb.tile5==1 and gvb.tile8==1):
			return(2)
		elif(gvb.tile5!=2 and gvb.tile2==1 and gvb.tile8 == 1):
			return(5)

		elif(gvb.tile9!=2 and gvb.tile3 == 1 and gvb.tile6 == 1):
			return(9)
		elif(gvb.tile3!=2 and gvb.tile6==1 and gvb.tile9==1):
			return(3)
		elif(gvb.tile6!=2 and gvb.tile3==1 and gvb.tile9 == 1):
			return(6)

		elif(gvb.tile9!=2 and gvb.tile1 == 1 and gvb.tile5 == 1):
			return(9)
		elif(gvb.tile5!=2 and gvb.tile1==1 and gvb.tile9==1):
			return(5)
		elif(gvb.tile1!=2 and gvb.tile5==1 and gvb.tile9 ==1):
			return(1)

		elif(gvb.tile7!=2 and gvb.tile3 == 1 and gvb.tile5 ==1):
			return(7)
		elif(gvb.tile5!=2 and gvb.tile3==1 and gvb.tile7==1):
			return(5)
		elif(gvb.tile3!=2 and gvb.tile5==1 and gvb.tile7 == 1):
			return(3)
		elif(gvb.tile3!=1 and gvb.tile1 == 2 and gvb.tile2 == 2):
			return(3)
		elif(gvb.tile2!=1 and gvb.tile1==2 and gvb.tile3==2) :
			return(2)
		elif(gvb.tile1!=1 and gvb.tile2==2 and gvb.tile3 == 2):
			return(1)

		elif(gvb.tile6!=1 and gvb.tile4 == 2 and gvb.tile5 == 2):
			return(6)
		elif(gvb.tile5!=1 and gvb.tile4==2 and gvb.tile6==2):
			return(5)
		elif(gvb.tile4!=1 and gvb.tile5==2 and gvb.tile6 == 2):
			return(4)

		elif(gvb.tile8!=1 and gvb.tile7 == 2 and gvb.tile9 == 2):
			return(8)
		elif(gvb.tile7!=1 and gvb.tile9==2 and gvb.tile8==2):
			return(7)
		elif(gvb.tile9!=1 and gvb.tile7==2 and gvb.tile8 ==2):
			return(9)

		elif(gvb.tile7!=1 and gvb.tile1 == 2 and gvb.tile4 == 2):
			return(7)
		elif(gvb.tile4!=1 and gvb.tile1==2 and gvb.tile7==2):
			return(4)
		elif(gvb.tile1!=1 and gvb.tile4==2 and gvb.tile7 == 2):
			return(1)

		elif(gvb.tile8!=1 and gvb.tile5 == 2 and gvb.tile2 == 2):
			return(8)
		elif(gvb.tile2!=1 and gvb.tile5==2 and gvb.tile8==2):
			return(2)
		elif(gvb.tile5!=1 and gvb.tile2==2 and gvb.tile8 == 2):
			return(5)

		elif(gvb.tile9!=1 and gvb.tile3 == 2 and gvb.tile6 == 2):
			return(9)
		elif(gvb.tile3!=1 and gvb.tile6==2 and gvb.tile9==2):
			return(3)
		elif(gvb.tile6!=1 and gvb.tile3==2 and gvb.tile9 == 2):
			return(6)

		elif(gvb.tile9!=9 and gvb.tile1 == 2 and gvb.tile5 == 2):
			return(9)
		elif(gvb.tile5!=5 and gvb.tile1==2 and gvb.tile9==2):
			return(5)
		elif(gvb.tile1!=1 and gvb.tile5==2 and gvb.tile9 == 2):
			return(1)

		elif(gvb.tile7!=1 and gvb.tile3 == 2 and gvb.tile5 == 2):
			return(7)
		elif(gvb.tile5!=1 and gvb.tile3==2 and gvb.tile7==2):
			return(5)
		elif(gvb.tile3!=1 and gvb.tile5==2 and gvb.tile7 == 2):
			return(3)

		elif(gvb.tile5 == 0):
			return(5)
		elif(gvb.tile1 == gvb.tile3 == gvb.tile7 == gvb.tile9 == 0):
			o = random.randint(1,4)
			if(o==1 and gvb.tile1 == 0):
				return(1)
			elif(o==2 and gvb.tile3==0):
				return(3)
			elif(o==3 and gvb.tile7==0):
				return(7)
			elif(o==4 and gvb.tile9==0):
				return(9)
		elif(gvb.tile1==0 or gvb.tile7==0 or gvb.tile3 ==0 or gvb.tile9 == 0):
			if(gvb.tile1==0):
				return(1)
			elif(gvb.tile7==0):
				return(7)
			elif(gvb.tile3==0):
				return(3)
			elif(gvb.tile9==0):
				return(9)
		elif(gvb.tile1==0 and gvb.tile9==0):
			#i = random.randint(1,4)
			if(gvb.tile2==0):
				return(2)
			elif(gvb.tile4==0):
				return(4)
			elif(gvb.tile6==0):
				return(6)
			elif(gvb.tile8==0):
				return(8)
		elif(gvb.tile3==0 and gvb.tile7==0):
			#i = random.randint(1,4)
			if(gvb.tile2==0):
				return(2)
			elif(gvb.tile4==0):
				return(4)
			elif(gvb.tile6==0):
				return(6)
			elif(gvb.tile8==0):
				return(8)
		elif(gvb.tile1==0 and gvb.tile3==0):
			#i = random.randint(1,4)
			if(gvb.tile2==0):
				return(2)
			elif(gvb.tile4==0):
				return(4)
			elif(gvb.tile6==0):
				return(6)
			elif(gvb.tile8==0):
				return(8)
		elif(gvb.tile7==0 and gvb.tile9==0):
			#i = random.randint(1,4)
			if(gvb.tile2==0):
				return(2)
			elif(gvb.tile4==0):
				return(4)
			elif(gvb.tile6==0):
				return(6)
			elif(gvb.tile8==0):
				return(8)
		elif(gvb.tile1 == gvb.tile3 == gvb.tile8 == 2):
			if(gvb.tile4==0):
				return(4)
			elif(gvb.tile6==0):
				return(6)
		elif(gvb.tile2 == gvb.tile7 == gvb.tile9 == 2):
			if(gvb.tile4==0):
				return(4)
			if(gvb.tile6==0):
				return(6)
		elif(gvb.tile1 == gvb.tile7 == gvb.tile6 == 2 or gvb.tile3 == gvb.tile4 == gvb.tile9 == 2):
			if(gvb.tile2==0):
				return(2)
			elif(gvb.tile8==0):
				return(8)
	if(gvb.turn==gvb.player2):
		

		if(gvb.tile3!=1 and gvb.tile1 == 2 and gvb.tile2 ==2):
			return(3)
		elif(gvb.tile2!=1 and gvb.tile1==2 and gvb.tile3==2):
			return(2)
		elif(gvb.tile1!=1 and gvb.tile2==2 and gvb.tile3 ==2):
			return(1)

		elif(gvb.tile6!=1 and gvb.tile4 == 2 and gvb.tile5 ==2):
			return(6)
		elif(gvb.tile5!=1 and gvb.tile4==2 and gvb.tile6==2):
			return(5)
		elif(gvb.tile4!=1 and gvb.tile5==2 and gvb.tile6 == 2):
			return(4)

		elif(gvb.tile8!=1 and gvb.tile9 == 2 and gvb.tile7 == 2):
			return(8)
		elif(gvb.tile7!=1 and gvb.tile9==2 and gvb.tile8==2):
			return(7)
		elif(gvb.tile9!=1 and gvb.tile7==2 and gvb.tile8 ==2):
			return(9)

		elif(gvb.tile7!=1 and gvb.tile1 == 2 and gvb.tile4 == 2):
			return(7)
		elif(gvb.tile4!=1 and gvb.tile1==2 and gvb.tile7==2):
			return(4)
		elif(gvb.tile1!=1 and gvb.tile4==2 and gvb.tile7 == 2):
			return(1)

		elif(gvb.tile8!=1 and gvb.tile5 == 2 and gvb.tile2 ==2):
			return(8)
		elif(gvb.tile2!=1 and gvb.tile5==2 and gvb.tile8==2):
			return(2)
		elif(gvb.tile5!=1 and gvb.tile2==2 and gvb.tile8 == 2):
			return(5)

		elif(gvb.tile9!=1 and gvb.tile3 == 2 and gvb.tile6 == 2):
			return(9)
		elif(gvb.tile3!=1 and gvb.tile6==2 and gvb.tile9==2):
			return(3)
		elif(gvb.tile6!=1 and gvb.tile3==2 and gvb.tile9 == 2):
			return(6)

		elif(gvb.tile9!=1 and gvb.tile1 == 2 and gvb.tile5 == 2):
			return(9)
		elif(gvb.tile5!=1 and gvb.tile1==2 and gvb.tile9==2):
			return(5)
		elif(gvb.tile1!=1 and gvb.tile5==2 and gvb.tile9 ==2):
			return(1)

		elif(gvb.tile7!=1 and gvb.tile3 == 2 and gvb.tile5 ==2):
			return(7)
		elif(gvb.tile5!=1 and gvb.tile3==2 and gvb.tile7==2):
			return(5)
		elif(gvb.tile3!=1 and gvb.tile5==2 and gvb.tile7 == 2):
			return(3)




		elif(gvb.tile3!=2 and gvb.tile1 == 1 and gvb.tile2 == 1):
			return(3)
		elif(gvb.tile2!=2 and gvb.tile1==1 and gvb.tile3==1):
			return(2)
		elif(gvb.tile1!=2 and gvb.tile2==1 and gvb.tile3 == 1):
			return(1)

		elif(gvb.tile6!=2 and gvb.tile4 == 1 and gvb.tile5 == 1):
			return(6)
		elif(gvb.tile5!=2 and gvb.tile4==1 and gvb.tile6==1):
			return(5)
		elif(gvb.tile4!=2 and gvb.tile5==1 and gvb.tile6 == 1):
			return(4)

		elif(gvb.tile8!=2 and gvb.tile7 == 1 and gvb.tile9 == 1):
			return(8)
		elif(gvb.tile7!=2 and gvb.tile9==1 and gvb.tile8==1):
			return(7)
		elif(gvb.tile9!=2 and gvb.tile7==1 and gvb.tile8 ==1):
			return(9)

		elif(gvb.tile7!=2 and gvb.tile1 == 1 and gvb.tile4 == 1):
			return(7)
		elif(gvb.tile4!=2 and gvb.tile1==1 and gvb.tile7==1):
			return(4)
		elif(gvb.tile1!=2 and gvb.tile4==1 and gvb.tile7 == 1):
			return(1)

		elif(gvb.tile8!=2 and gvb.tile5 == 1 and gvb.tile2 == 1):
			return(8)
		elif(gvb.tile2!=2 and gvb.tile5==1 and gvb.tile8==1):
			return(2)
		elif(gvb.tile5!=2 and gvb.tile2==1 and gvb.tile8 == 1):
			return(5)

		elif(gvb.tile9!=2 and gvb.tile3 == 1 and gvb.tile6 == 1):
			return(9)
		elif(gvb.tile3!=2 and gvb.tile6==1 and gvb.tile9==1):
			return(3)
		elif(gvb.tile6!=2 and gvb.tile3==1 and gvb.tile9 == 1):
			return(6)

		elif(gvb.tile9!=2 and gvb.tile1 ==1 and gvb.tile5 == 1):
			return(9)
		elif(gvb.tile5!=2 and gvb.tile1==1 and gvb.tile9==1):
			return(5)
		elif(gvb.tile1!=2 and gvb.tile5==1 and gvb.tile9 == 1):
			return(1)

		elif(gvb.tile7!=2 and gvb.tile3 == 1 and gvb.tile5 == 1):
			return(7)
		elif(gvb.tile5!=2 and gvb.tile3==1 and gvb.tile7==1):
			return(5)
		elif(gvb.tile3!=2 and gvb.tile5==1 and gvb.tile7 == 1):
			return(3)





		elif(gvb.tile5 == 0):
			return(5)
		elif(gvb.tile1 == gvb.tile3 == gvb.tile7 == gvb.tile9 == 0):
			o = random.randint(1,4)
			if(o==1 and gvb.tile1 == 0):
				return(1)
			elif(o==2 and gvb.tile3==0):
				return(3)
			elif(o==3 and gvb.tile7==0):
				return(7)
			elif(o==4 and gvb.tile9==0):
				return(9)
		elif(gvb.tile1==0 or gvb.tile7==0 or gvb.tile3 ==0 or gvb.tile9 == 0):
			if(gvb.tile1==0):
				return(1)
			elif(gvb.tile7==0):
				return(7)
			elif(gvb.tile3==0):
				return(3)
			elif(gvb.tile9==0):
				return(9)
		elif(gvb.tile1==0 and gvb.tile9==0):
			#i = random.randint(1,4)
			if(gvb.tile2==0):
				return(2)
			elif(gvb.tile4==0):
				return(4)
			elif(gvb.tile6==0):
				return(6)
			elif(gvb.tile8==0):
				return(8)
		elif(gvb.tile3==0 and gvb.tile7==0):
			#i = random.randint(1,4)
			if(gvb.tile2==0):
				return(2)
			elif(gvb.tile4==0):
				return(4)
			elif(gvb.tile6==0):
				return(6)
			elif(gvb.tile8==0):
				return(8)
		elif(gvb.tile1==0 and gvb.tile3==0):
			#i = random.randint(1,4)
			if(gvb.tile2==0):
				return(2)
			elif(gvb.tile4==0):
				return(4)
			elif(gvb.tile6==0):
				return(6)
			elif(gvb.tile8==0):
				return(8)
		elif(gvb.tile7==0 and gvb.tile9==0):
			#i = random.randint(1,4)
			if(gvb.tile2==0):
				return(2)
			elif(gvb.tile4==0):
				return(4)
			elif(gvb.tile6==0):
				return(6)
			elif(gvb.tile8==0):
				return(8)
		elif(gvb.tile1 == gvb.tile3 == gvb.tile8 == 1):
			if(gvb.tile4==0):
				return(4)
			elif(gvb.tile6==0):
				return(6)
		elif(gvb.tile2 == gvb.tile7 == gvb.tile9 == 1):
			if(gvb.tile4==0):
				return(4)
			if(gvb.tile6==0):
				return(6)
		elif(gvb.tile1 == gvb.tile7 == gvb.tile6 == 1 or gvb.tile3 == gvb.tile4 == gvb.tile9 == 1):
			if(gvb.tile2==0):
				return(2)
			elif(gvb.tile8==0):
				return(8)
def takeNaiveMove():
	
	""" Returns a tile number randomly from the set of unchecked tile with uniform probability distribution.    
	"""
	gvb.s = ""
	if(gvb.tile1==0):
		gvb.s = gvb.s + '1'
	if (gvb.tile2==0):
		gvb.s = gvb.s + '2'
	if (gvb.tile3==0):
		gvb.s = gvb.s + '3'
	if (gvb.tile4==0):
		gvb.s = gvb.s + '4'
	if (gvb.tile5==0):
		gvb.s = gvb.s + '5'
	if (gvb.tile6==0):
		gvb.s = gvb.s + '6'
	if (gvb.tile7==0):
		gvb.s = gvb.s + '7'
	if (gvb.tile8==0):
		gvb.s = gvb.s + '8'
	if (gvb.tile9==0):
		gvb.s = gvb.s + '9'
	#print(gvb.s)  # Statement to check the proper working of the function.
	
	i = random.randint(0,len(gvb.s)-1)
	b = gvb.s[i]
	return(int(b))




def buddhu():
	"""
	FUNCTION MADE BY ME TO MAKE MY LIFE EASIER
	Changes the value of the tile to the number of the corresponding player from the tile number returned by the takeNaiveMove() function. Works as and when the players turn is the corresponding one.
	"""
	x = takeNaiveMove()
	#print(x)
	if(gvb.turn == gvb.player1):
		if(validmove(1)==True and x==1):
			gvb.tile1 = 1
		elif(validmove(2)==True and x==2):
			gvb.tile2 = 1
		elif( validmove(3)==True and x==3):
			gvb.tile3 = 1
		elif(validmove(4)==True and x==4):
			gvb.tile4 = 1
		elif(validmove(5)==True and x==5):
			gvb.tile5 = 1
		elif(validmove(6)==True and x==6):
			gvb.tile6 = 1
		elif(validmove(7)==True and x==7):
			gvb.tile7 = 1
		elif(validmove(8)==True and x==8):
			gvb.tile8 = 1
		elif(validmove(9)==True and x==9):
			gvb.tile9 = 1
		#print(gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)
																#def buddhu2():
	                                                                  #x = takeNaiveMove()
	
	elif(gvb.turn==gvb.player2):                                                                  #print(x)
		if(validmove(1)==True and x==1):
			gvb.tile1 = 2
		elif(validmove(2)==True and x==2):
			gvb.tile2 = 2
		elif( validmove(3)==True and x==3):
			gvb.tile3 = 2
		elif(validmove(4)==True and x==4):
			gvb.tile4 = 2
		elif(validmove(5)==True and x==5):
			gvb.tile5 = 2
		elif(validmove(6)==True and x==6):
			gvb.tile6 = 2
		elif(validmove(7)==True and x==7):
			gvb.tile7 = 2
		elif(validmove(8)==True and x==8):
			gvb.tile8 = 2
		elif(validmove(9)==True and x==9):
			gvb.tile9 = 2
		#rint(gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)



def smart1():
	"""
	FUNCTION MADE BY ME TO MAKE MY LIFE EASIER
	Changes the number of the tile favorable to player 1 using the value returned by the takeStrategicMove function.
	"""
	y = takeStrategicMove()
	#print(y)
	if(validmove(1)==True and y==1):
		gvb.tile1 = 1
	elif(validmove(2)==True and y==2):
		gvb.tile2 = 1
	elif( validmove(3)==True and y==3):
		gvb.tile3 = 1
	elif(validmove(4)==True and y==4):
		gvb.tile4 = 1
	elif(validmove(5)==True and y==5):
		gvb.tile5 = 1
	elif(validmove(6)==True and y==6):
		gvb.tile6 = 1
	elif(validmove(7)==True and y==7):
		gvb.tile7 = 1
	elif(validmove(8)==True and y==8):
		gvb.tile8 = 1
	elif(validmove(9)==True and y==9):
		gvb.tile9 = 1
	#print(gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)

def smart2():
	"""
	FUNCTION MADE BY ME TO MAKE MY LIFE EASIER
	Changes the number of the tile favorable to player 2 using the value returned by the takeStrategicMove function.
	"""
	z = takeStrategicMove()
	#print(type(x))
                                                                 #print(x)
	if(validmove(1)==True and z==1):
		gvb.tile1 = 2
	elif(validmove(2)==True and z==2):
		gvb.tile2 = 2
	elif( validmove(3)==True and z==3):
		gvb.tile3 = 2
	elif(validmove(4)==True and z==4):
		gvb.tile4 = 2
	elif(validmove(5)==True and z==5):
		gvb.tile5 = 2
	elif(validmove(6)==True and z==6):
		gvb.tile6 = 2
	elif(validmove(7)==True and z==7):
		gvb.tile7 = 2
	elif(validmove(8)==True and z==8):
		gvb.tile8 = 2
	elif(validmove(9)==True and z==9):
		gvb.tile9 = 2
	#print(gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9) # To chech whether the function is working properly.

def win():
	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
	"""
	if(gvb.tile1 == gvb.tile2 == gvb.tile3 == 1 or gvb.tile1 == gvb.tile2 == gvb.tile3 == 2):
		return True
	elif(gvb.tile4 == gvb.tile5 == gvb.tile6 == 1 or gvb.tile4 ==gvb.tile5 == gvb.tile6 == 2):
		return True
	elif(gvb.tile7 == gvb.tile8 == gvb.tile9==1 or gvb.tile7 == gvb.tile8 == gvb.tile9 == 2):
		return True
	elif(gvb.tile1 == gvb.tile4 == gvb.tile7==1 or gvb.tile1 == gvb.tile4 == gvb.tile7 == 2):
		return True
	elif(gvb.tile2 == gvb.tile5 == gvb.tile8==1 or gvb.tile2 == gvb.tile5 == gvb.tile8 == 2):
		return True
	elif(gvb.tile3 == gvb.tile6 == gvb.tile9==1 or gvb.tile3 == gvb.tile6 == gvb.tile9 == 2):
		return True
	elif(gvb.tile1 == gvb.tile5 == gvb.tile9==1 or gvb.tile1 == gvb.tile5 == gvb.tile9 == 2):
		return True
	elif(gvb.tile3 == gvb.tile5 == gvb.tile7==1 or gvb.tile3 == gvb.tile5 == gvb.tile7 == 2):
		return True
	else:
		return False

def game(gametype):
	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
	
		gametype defines three types of games described above.
		i.e., game1, game2, game3
	"""
	flag = 0 # Default return Value is 0 
	if(gametype==1):
		gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
		for i in range(0,9):
			if(gvb.turn==gvb.player1):
				buddhu()
				#print("A",gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)
				gvb.turn = gvb.player2
				#print(gvb.turn)
				if(win()==True):
					#print(win())
					flag+=1
					#print(flag)
					break
					

			elif(gvb.turn==gvb.player2):
				buddhu()
				#print("B",gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)
				gvb.turn = gvb.player1
				#print(gvb.turn)
				if(win()==True):
					#print(win())
					flag+=2
					#print(flag)
					break
		#print(flag)
		return(flag)
	elif(gametype==2):
		gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
		for i in range(0,9):# Game cannot run more than nine times
			if(gvb.turn==gvb.player1):
				buddhu()
				#print("A",gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)
				gvb.turn = gvb.player2
				#print(gvb.turn)
				if(win()==True):
					#print(win())
					flag+=1
					#print(flag)
					break
					

			elif(gvb.turn==gvb.player2):
				smart2()
				#print("B",gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)
				gvb.turn = gvb.player1
				#print(gvb.turn)
				if(win()==True):
					#print(win())
					flag+=2
					#print(flag)
					break
	
		return(flag)
	elif(gametype==3):
		gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9 # Initializing the value for every loop
		for i in range(0,9):
			gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
			if(gvb.turn==gvb.player1):
				smart1()
				#print("A",gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)
				gvb.turn = gvb.player2
				#print(gvb.turn)
				if(win()==True):
					#print(win())
					flag+=1
					#print(flag)
					break
					

			elif(gvb.turn==gvb.player2):
				smart2()
				#print("B",gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)
				gvb.turn = gvb.player1
				#print(gvb.turn)
				if(win()==True):
					#print(win())
					flag+=2
					#print(flag)
					break
	
		return(flag)

def game1(n):
	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	count = 0
	for i in range(0,n):
		x = game(1)
		#print(x)
		if(x==1):
			count = count + 1
	#print(count)
	prob = count/n
	return(prob)


def game2(n):
	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	count = 0
	for i in range(0,n):
		x = game(2)
		if(x==1):
			count = count + 1
	prob = count/n
	return(prob)

def game3(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	count = 0
	for i in range(0,n):
		x = game(3)
		if(x==1):
			count = count + 1
	prob = count/n
	return(prob)



# Random code below to test the correctness of the program. NOT PART OF MAIN PROGRAM. Not to be evaluated.


"""
#for i in range(9):	
#x = game1(1000)
#print(x)
#print("gap")
for i in range(9):
	buddhu()
	print("A",gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)
	gvb.turn = gvb.player2
	if(win()==True):
		break

	buddhu()
	if(win()==True):
		break
	gvb.turn = gvb.player1
	
	print("B",gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)
	print(gvb.turn)
	#print(gvb.tile1,gvb.tile2,gvb.tile3,gvb.tile4,gvb.tile5,gvb.tile6,gvb.tile7,gvb.tile8,gvb.tile9)


	"""












