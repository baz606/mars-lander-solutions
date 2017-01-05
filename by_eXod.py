# This solution belongs to user https://www.codingame.com/profile/d3629ca7ea9f246d1b7f03624c916e32376474
# User Ryba published it over 1 year ago

import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # the number of points used to draw the surface of Mars.

surf_x = []
surf_y = []

x_target = 0
y_target = 0

high_vert = []


def regulator_y(y_cur, y_limit, y_speed):
    speed = 0

    global y_target


    if (y_speed <= -30):
        speed = 4

    if -30 <= y_speed < 0:
        speed = 2

    if  y_speed > 0:
        speed = 0

    if y_limit != y_target:
        if abs(y_limit - y_cur) < 500:
            speed = 4
        elif abs(y_limit - y_cur) < 1500:
            if speed < 3:
                speed = 3
        elif abs(y_limit - y_cur) < 3000:
            if speed < 2:
                speed = 2
        elif abs(y_limit - y_cur) < 5000:
            pass

    return speed


def regulator_x(x_cur, x_speed):
    angl = 0
    speed = 0
    close_to_tar = False

    global x_target

    if abs(x_target - x_cur) < 500:
        angl = 0
    elif abs(x_target - x_cur) < 1500:
        angl = 30
    elif abs(x_target - x_cur) < 3000:
        angl = 60
    elif abs(x_target - x_cur) < 5000:
        angl = 90

    if (abs(x_target - x_cur) < 600) or (abs(x_speed) > 40):
        close_to_tar = True

    if close_to_tar:
        if (abs(x_speed) >= 16):
            speed = 4
            angl = 60

        if 5 <= abs(x_speed) < 16:
            speed = 2
            angl = 20

        if  abs(x_speed) < 5:
            speed = 0
            angl = 0

    if (x_target - x_cur > 0 ) and not close_to_tar:
        angl = -angl

    if close_to_tar:
        if (x_speed < 0):
            angl = -angl

    return angl, speed


def set_ver():
    global high_vert
    global surf_y

    tmp_surf_y = []

    #for x in surf_x:

    for i in xrange(1, len(surf_y)-1):
        if (surf_y[i] > surf_y[i-1]) and (surf_y[i] > surf_y[i+1]):
            high_vert.append([surf_x[i], surf_y[i]])

    return

def get_cur_lim(x_cur, y_cur):
    y_r = y_target

    if abs(x_target - x_cur) > 600:
        for el in high_vert:
            if (el[0] > x_cur):
                y_r = el[1]
                break

    print >> sys.stderr, "y_r: {0}".format(y_r)
    return y_r

def close_to_ground(y_cur):
    if abs(y_cur - y_target) < 100:
        return  True
    else:
        return False

def too_far(x_cur):
    return abs(x_cur - x_target) > 500

def over_target(y_cur, y_speed, x_cur):
    return ((abs(y_cur - y_target) < 600) or (y_cur <= y_target) or (abs(get_cur_lim(x_cur, y_cur) - y_cur) < 600) ) and (y_speed < 5) and too_far(x_cur)

for i in xrange(N):
    # LAND_X: X coordinate of a surface point. (0 to 6999)
    # LAND_Y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    LAND_X, LAND_Y = [int(i) for i in raw_input().split()]

    surf_x.append(LAND_X)
    surf_y.append(LAND_Y)

    if len(surf_y) >= 2:
        if LAND_Y == surf_y[-2]:
            x_target = surf_x[-2] + abs(LAND_X - surf_x[-2]) // 2
            y_target = LAND_Y


set_ver()

print >> sys.stderr, "x_surf: {0}".format(surf_x)
print >> sys.stderr, "y_surf: {0}".format(surf_y)
print >> sys.stderr, "x_tar: {0}".format(x_target)
print >> sys.stderr, "y_tar: {0}".format(y_target)
print >> sys.stderr, "high_vert: {0}".format(high_vert)



# game loop
while 1:
    # HS: the horizontal speed (in m/s), can be negative.
    # VS: the vertical speed (in m/s), can be negative.
    # F: the quantity of remaining fuel in liters.
    # R: the rotation angle in degrees (-90 to 90).
    # P: the thrust power (0 to 4).
    X, Y, HS, VS, F, R, P = [int(i) for i in raw_input().split()]

    angl = 0
    power = 0

    angl, x_pow = regulator_x(X, HS)

    y_pow = regulator_y(Y, get_cur_lim(X, Y), VS)

    if (y_pow == 4) and (VS < -35):
        angl = 0

    power = max(x_pow, y_pow)

    if close_to_ground(Y):
        angl = 0

    if over_target(Y, VS, X):
        angl = 0
        power = 4


    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    print "{0} {1}".format(angl, power) # R P. R is the desired rotation angle. P is the desired thrust power.
