import sys
import math

def computing(x, h_speed, h_diff, direction, range_array):
    if h_speed > 0 and direction == "left":
        h_speed = 0 - h_speed 
    elif h_speed < 0 and direction == "left":
        h_speed = abs(h_speed)
    distance = 0
    precomputed = {"acclrt": -1, "slwdn": -1, "final speed": 1000, "prob diff": 7000}
    for indx,v in enumerate(range_array):
        distance += v + h_speed
        prob_dist = distance
        for indx_slow,vslow in enumerate(range_array):
            final_speed = v + h_speed - vslow
            prob_dist += final_speed
            prob_differ = prob_dist - h_diff
            if abs(precomputed["final speed"]) > abs(final_speed) and abs(precomputed["prob diff"]) > abs(prob_differ):
                precomputed = {"acceleration": indx, "slowdown": indx_slow, "final speed": final_speed, "prob diff": prob_differ}
            elif abs(final_speed) < 5 and abs(precomputed["prob diff"]) > abs(prob_differ):
                precomputed = {"acceleration": indx, "slowdown": indx_slow, "final speed": final_speed, "prob diff": prob_differ}
    print >> sys.stderr,precomputed
    return precomputed


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

range_30_4 = [x_1 for x_1 in range(1, 1000, 2)]
range_30_4 = [0] + range_30_4

range_15_4 = [x_2 for x_2 in range(1, 1000)]
range_15_4 = [0] + range_15_4

prev_point = None
x_surf = None
surface_n = int(raw_input())  # the number of points used to draw the surface of Mars.

for i in xrange(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in raw_input().split()]
    #print >> sys.stderr, land_x, land_y 
    if prev_point:
        if prev_point["y"] == land_y:
            x_surf = [prev_point["x"], land_x]
            plateau_hight = land_y
        else:
            prev_point = {"y": land_y, "x": land_x}
    else:
        prev_point = {"y": land_y, "x": land_x}
if x_surf:
    safe_area = x_surf[1] - x_surf[0]
    mid_safe = safe_area / 2
    prefer_point = x_surf[0] + mid_safe
else:
    prefer_point = 3500
    
print >> sys.stderr,"Landing point", prefer_point


iteration = 0

# game loop
while True:
    iteration += 1
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in raw_input().split()]
    

    if iteration == 1:
        
        if x < prefer_point:
            direction = "right" # h_speed+ angle-
            current_program = "acceleration" 
            print >> sys.stderr, "acceleration started"
        elif x > prefer_point:
            direction = "left" # h_speed- angle+
            current_program = "acceleration"
            print >> sys.stderr, "acceleration started"
        else:
            direction = "here"
            current_program = "descend"
            print >> sys.stderr, "descend started"
            h_diff = 0

        h_diff = abs(prefer_point - x)
        if plateau_hight > 1900:
            precomputed = computing(x, h_speed, h_diff, direction, range_15_4)
            current_program = "highground"
            print >> sys.stderr,precomputed
            
        else:
            precomputed = computing(x, h_speed, h_diff, direction, range_30_4)
        if precomputed["acceleration"] == 0:
            current_program = "slowdown"
            print >> sys.stderr, "slowdown started"
            
        starting_point = iteration
            
    if y < 900 and abs(h_speed) < 8 and abs(prefer_point - x) < 500:
        current_program = "descend"
        print >> sys.stderr, "foced descend"
        
    
    
    if current_program == "acceleration":
        if iteration - starting_point <= precomputed["acceleration"]:
            if direction == "right":
                print "-30 4"
            else:
                print "30 4"
        else:
            current_program = "slowdown"
            starting_point = iteration
            print >> sys.stderr,"slowdown started"
            print "0 0"
            
        
    elif current_program == "slowdown":
        h_diff = abs(prefer_point - x)
        
        if iteration - starting_point <= precomputed["slowdown"]:
            if iteration == starting_point or iteration == starting_point + 1:
                if h_speed < 0:
                    slowd_dir = "-30 4"
                elif h_speed > 0:
                    slowd_dir = "30 4"
            print >> sys.stderr, "slowdown in progress"
            
            print slowd_dir

        elif h_diff > 200:
            if x < prefer_point:
                direction = "right"
            elif x > prefer_point:
                direction = "left"
            
            precomputed = computing(x, h_speed, h_diff, direction, range_30_4)
            if precomputed["acceleration"] == 0:
                current_program = "slowdown"
                starting_point = iteration
                print >> sys.stderr, "addition slowdown started"
                print "0 4"
            else:
                current_program = "acceleration"
                starting_point = iteration
                print >> sys.stderr, "acceleration started"
            print "0 4"
        else:
            current_program = "descend"
            print >> sys.stderr, "descend started"
            print "0 0"
        
    elif current_program == "descend":
        if v_speed > -30:
            print "0 3"
        else:
            print "0 4"
            
    elif current_program == "highground":
        print >> sys.stderr,precomputed
        if iteration < precomputed["acceleration"] - 3: # 29
            print "15 4"
        elif precomputed["acceleration"] - 3 <= iteration < precomputed["slowdown"] + precomputed["acceleration"] - 10:
            print "-15 4"
        else:
            print "0 3"
            
