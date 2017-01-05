# This solution belongs to user https://www.codingame.com/profile/8fe6daf329d120f0e3014777bebfec313384001
# User Ryba published it over 1 year ago

import sys
import math

surface_n = int(raw_input()) # the number of points used to draw the surface of Mars.
x1 = x2 = yr = 0
f = False
for i in xrange(surface_n):
    land_x, land_y = [int(j) for j in raw_input().split()]
    if land_y == yr:
        x2 = land_x
        f = True
    if not f:
        x2 = x1
        x1 = land_x
        yr = land_y

xl = (x1 + x2)/2
# game loop
while 1:
     # h_speed: the horizontal speed (in m/s), can be negative.
     # v_speed: the vertical speed (in m/s), can be negative.
     # fuel: the quantity of remaining fuel in liters.
     # rotate: the rotation angle in degrees (-90 to 90).
     # power: the thrust power (0 to 4).
     
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in raw_input().split()]
    print >> sys.stderr, yr
    lim = 25*abs(2*xl-x)/xl
    sig = -1 if x<xl else 1
    
    if x<x1 or x>x2:
        rot = 30*(h_speed+sig*lim)/45
        if v_speed < -10 or y-yr<250: pow = 4
        else: pow = 2
    
    else:
        if abs(h_speed) > 5: rot = (h_speed)
        else: rot = 0
        if y - yr < 50: rot = 0
        if v_speed < -20:
            pow = 4
        else: pow = 0
        
    print rot, pow
