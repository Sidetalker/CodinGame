import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in input().split()]

thorX = TX
thorY = TY

# game loop
while 1:
	E = int(input()) # The level of Thor's remaining energy, representing the number of moves he can still make.
	
	if thorX < LX and thorY > LY:
		print("NE")
		thorX += 1
		thorY -= 1
	elif thorX > LX and thorY > LY:
		print("NW")
		thorX -= 1
		thorY -= 1
	elif thorX < LX and thorY < LY:
		print("SE")
		thorX += 1
		thorY += 1
	elif thorX > LX and thorY < LY:
		print("SW")
		thorX -= 1
		thorY += 1
	elif thorX == LX and thorY < LY:
		print("S")
		thorY += 1
	elif thorX == LX and thorY > LY:
		print("N")
		thorY -= 1
	elif thorX < LX and thorY == LY:
		print("E")
		thorX += 1
	elif thorX > LX and thorY == LY:
		print("W")
		thorX -= 1
	else:
		print("N")