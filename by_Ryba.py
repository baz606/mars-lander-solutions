# This solution belongs to user https://www.codingame.com/profile/1740c592502790b499b47e5574e4e8e88598561
# User Ryba published it about 2 months ago

import sys
import math


###############################    
def get_surface(surface_coords):
    surface = []
    b = surface_coords[0]
    e = surface_coords[1]
    counter = 1
    for i in xrange(0, 7000):
        if i > e[0]:
            counter += 1
            b = e
            e = surface_coords[counter]
        delta_x_100 = e[0] - b[0]
        delta_x = i - b[0]
        delta_y_100 = e[1] - b[1]
        delta_y = float(delta_x) / delta_x_100 * delta_y_100
        surface.append(b[1] + delta_y)
    
    return surface
    
def get_landing_coords(surface_coords):
    height = -1
    b = None
    e = None
    for i in xrange(1, surface_n):
        if surface_coords[i][1] == surface_coords[i-1][1]:
            height = surface_coords[i][1]
            b = surface_coords[i-1]
            e = surface_coords[i]
            break

    return b[0], b[1], e[0], e[1]

def get_max_height(surface, x_begin, landing_x1, landing_x2):
    if x_begin < landing_x1:
        x_range = xrange(x_begin, landing_x1 + 1)
    elif x_begin > landing_x2:
        x_range = xrange(x_begin, landing_x2 - 1, -1)
    else:
        return surface[landing_x1 + 1]
    
    max_h = 0
    for i in x_range:
        if surface[i] > max_h:
            max_h = surface[i]
    return max_h
    
def get_max_h_speed(x, land_x1, land_x2):
    if x < land_x1 - 1000:
        return 50
    elif x > land_x2 + 1000:
        return -50
    elif x < land_x1:
        return 20
    elif x > land_x2:
        return -20
    elif x < (land_x1 + land_x2) / 2.0:
        return 10
    else:
        return -10

def get_angle(x, y, land_x1, land_x2, v_speed, h_speed, max_speed):
    height = get_max_height(surface, x, land_x1, land_x2)
    
    if y - height < 200:
        return 0
    
    if abs(h_speed) > abs(max_speed):
        speed_diff = abs(h_speed - max_speed)
        angle = speed_diff * 1.5 if speed_diff * 1.5 < 60 else 60
        angle = angle if h_speed > 0 else -1 * angle
        return int(angle)
    elif x <= land_x1 + 400:
        return -15
    elif x >= land_x2 - 400:
        return 15
    else:
        return 0
    
def get_thrust(v_speed, h_speed, max_speed, y):
    if y > 2800:
        return 1
    elif  v_speed < -30 or abs(h_speed) > abs(max_speed):
        return 4
    else:
        return 3
###############################################

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
surface_coords = []
surface_n = int(raw_input())  # the number of points used to draw the surface of Mars.
for i in xrange(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    surface_coords.append( [int(j) for j in raw_input().split()] )


land_x1, land_y1, land_x2, land_y2 = get_landing_coords(surface_coords)    
surface = get_surface(surface_coords)

# for i in surface_coords:
#     print >> sys.stderr, i[1], surface[i[0]]

# game loop
direction = 0
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    # print >> sys.stderr, land_x1, land_x2, direction, h_speed
    
    max_height = get_max_height(surface, x, land_x1, land_x2)
    max_h_speed = get_max_h_speed(x, land_x1, land_x2)
    
    angle = get_angle(x, y, land_x1, land_x2, v_speed, h_speed, max_h_speed)
    thrust = get_thrust(v_speed, h_speed, max_h_speed, y)
    
    
    
    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    print "{} {}".format(angle, thrust)
    
    
