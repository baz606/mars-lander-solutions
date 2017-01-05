# This solution belongs to user https://www.codingame.com/profile/4086d9a6ebe1e9b3e58283d6980cf6b3849379
# User Amnesix published it 1 year ago

# -*- coding: utf-8 -*-
from __future__ import print_function
import sys, math

G = 3.711
A = 21.9

# Auto-generated code below aims at helping you parse
# the standard raw_input according to the problem statement.

surfaceN = int(raw_input()) # the number of points used to draw the surface of Mars.

surface = []
indexLand=0
for i in range(surfaceN):
    # landX: X coordinate of a surface point. (0 to 6999)
    # landY: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    landX, landY = [int(j) for j in raw_input().split()]
    surface.append((landX,landY))
    if i > 0 and surface[i-1][1] == landY:
        indexLand = i-1

#print(surface, "-->", indexLand, file=sys.stderr)
cibleX = (surface[indexLand][0]+surface[indexLand+1][0])/2

# game loop
while 1:
    # hSpeed: the horizontal speed (in m/s), can be negative.
    # vSpeed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    X, Y, hSpeed, vSpeed, fuel, rotate, power = [int(i) for i in raw_input().split()]
    
    # rechercher l'altitude max à dépasser
    altitude = 100000
    for i in range(surfaceN):
        if X < surface[i][0] < cibleX or X > surface[i][0] > cibleX:
            print(X, surface[i][0], cibleX, surface[i][1], file=sys.stderr)
            altitude = min(Y - surface[i][1], altitude)
    #print(altitude, cibleX, file=sys.stderr)
            
    dist = abs(X - (surface[indexLand][0]+surface[indexLand+1][0])/2)
    
    if X > surface[indexLand][0] and X < surface[indexLand+1][0]:
        if Y - surface[indexLand][1] < 500:
            rot = 0
        elif hSpeed > 0:
            rot = 30 if hSpeed > 30 else 15
        elif hSpeed < 0:
            rot = -30 if hSpeed < -30 else -15
        else:
            rot = 0
    elif X < surface[indexLand][0]:
        if surface[indexLand][0] - X > 1000:
            vit = 40
        else:
            vit = 18
        if hSpeed < vit:
            rot = -30
        elif hSpeed > vit+3:
            rot = 30
        else:
            rot = 0
    else: # X > surface[indexLand][0]
        if X - surface[indexLand+1][0] > 1000:
            vit = -40
        else:
            vit = -18
        if hSpeed > vit:
            rot = 30
        elif hSpeed < vit-3:
            rot = -30
        else:
            rot = 0

    if vSpeed < -30:
        thr = 4
    elif Y - surface[indexLand][1] < 1000:
        hmin = 300 if dist > 500 else 0
        if Y - surface[indexLand][1] < hmin or vSpeed < -5:
            thr = 4
        else:
            thr = 3
    elif rot != 0 and rot * rotate >= 0:
        thr = 4
    else:
        thr = 0
        
    # !!!
    if altitude < 200:
        rot, thr = 8 if rot > 0 else -8 if rot < 0 else 0, 4
        
    print(rot, thr)
    
