import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(input()) # the number of points used to draw the surface of Mars.
zoneWidth = 0
zoneHeight = 0
zoneStart = 0

for i in range(N):
	# LAND_X: X coordinate of a surface point. (0 to 6999)
	# LAND_Y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
	LAND_X, LAND_Y = [int(i) for i in input().split()]

	if zoneWidth >= 1000:
		continue

	if LAND_Y == zoneHeight:
		zoneWidth += LAND_X - zoneWidth
	else:
		zoneHeight = LAND_Y
		zoneWidth = 0
		zoneStart = LAND_X

print("zoneHeight:", zoneHeight, file=sys.stderr)
print("zoneWidth:", zoneWidth, file=sys.stderr)
print("zoneStart:", zoneStart, file=sys.stderr)

landingTarget = -1
vMax = 40
hMax = 20
commandQueue = []

# game loop
while 1:
	# HS: the horizontal speed (in m/s), can be negative.
	# VS: the vertical speed (in m/s), can be negative.
	# F: the quantity of remaining fuel in liters.
	# R: the rotation angle in degrees (-90 to 90).
	# P: the thrust power (0 to 4).
	X, Y, HS, VS, F, R, P = [int(i) for i in input().split()]

	if landingTarget == -1:
		if zoneStart > X:
			landingTarget = zoneStart
		if X > zoneStart and X <= zoneStart + zoneWidth:
			landingTarget = X
		else:
			landingTarget = zoneStart + zoneWidth

		print("landingTarget:", landingTarget, file=sys.stderr)

	vForce = P * math.sin(-R)	# m/s^2
	hForce = P * math.cos(-R)	# m/s^2
	hSpeed = HS 				# m/s
	vSpeed = VS 				# m/s
	vertDif = Y - zoneHeight	# m
	horDif = X - zoneStart

	vForce -= 3.711		# Account for moon gravity

	if R > 0:
		hForce *= -1

	# Calculate time to zero hSpeed
	changeInSpeed = -hSpeed
	curTime = 0
	curSpeed = hSpeed
	curThrust = P
	curAngle = R
	curForce = hForce

	while hSpeed > 1 or hSpeed < 1:
		forceMod = 0

		if curForce > 0:
			tempTime = 0
			tempSpeed = 0
			


		curTime++

		curForce



		curSpeed += curForce




	yImpactVelocity = -math.sqrt(abs(math.pow(vSpeed, 2) + 2 * vForce * vertDif))
	timeToImpact = -(yImpactVelocity - vSpeed) / vForce

	newR = 5
	newP = 3

	commandQueue.insert(0, (1,1))

	print("vForce:", vForce, file=sys.stderr)
	print("hForce:", hForce, file=sys.stderr)
	print("vertDif:", vertDif, file=sys.stderr)
	print("horDif:", horDif, file=sys.stderr)
	print("yImpactVelocity:", yImpactVelocity, file=sys.stderr)
	print("timeToImpact:", timeToImpact, file=sys.stderr)
	print("newR:", newR, file=sys.stderr)
	print("newP:", newP, file=sys.stderr)

	if len(commandQueue) > 0:
		result = commandQueue.pop()
		print(result[0], result[1])
	else: 
		print(0, 0)

