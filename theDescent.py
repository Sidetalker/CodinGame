import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1:
    SX, SY = [int(i) for i in input().split()]
    highest = 0
    current = -1
    
    for i in range(8):
        MH = int(input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if MH > highest:
            current = i
            highest = MH
            
    if SX == current:
        print("FIRE")
    else:
        print("HOLD")