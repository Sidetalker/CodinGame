import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(input()) # the length of the road before the gap.
G = int(input()) # the length of the gap.
L = int(input()) # the length of the landing platform.

jumped = False

# game loop
while 1:
	S = int(input()) # the motorbike's speed.
	X = int(input()) # the position on the road of the motorbike.

	print("R:", R, file=sys.stderr)
	print("G:", G, file=sys.stderr)
	print("L:", L, file=sys.stderr)
	print("S:", S, file=sys.stderr)
	print("X:", X, file=sys.stderr)

	if jumped:
		print("SLOW")
		continue

	if S > 0:
		offset = (R - X - 1) % S
	else:
		offset = 0

	if S < G + 1:
		print("SPEED")
	elif S > G + 1:
		print("SLOW")
	else:
		if X == R - offset - 1:
			print("JUMP")
			jumped = True
		elif offset > 0:
			print("SPEED")
		else:
			print("WAIT")

	print("offset:", offset, file=sys.stderr)