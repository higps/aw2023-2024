# Make a program called my_throw.py which takes as input by the user
# an angle (in degrees), velocity (in km/h) and initiation height (in meter).
# Calculate and print the following information:
import math
# angle = float(input("Enter angle: "))
# velocity = float(input("Enter velocity: "))
# initiation_height = float(input("Enter initiation height: "))
def calc_throw(angle, velocity, initiation_height, b_print):
    # The throw angle using radians
    # α = math.radians(θ)
    # where θ is the throw angle in degrees.
    throw_angle = math.radians(angle)
    if(b_print):print(f"i Throw angle: {throw_angle:.2f}")

    # The throw velocity in meter/second
    throw_velocity = velocity/3.6
    if(b_print):print(f"ii Throw velocity: {throw_velocity:.2f}")

    # The throw velocity in the horizontal direction (in m/s), given by

    throw_velocity_horizontal = throw_velocity * math.cos(throw_angle)
    if(b_print):print(f"iii Throw velocity horizontal: {throw_velocity_horizontal:.2f}")

    # The throw velocity in the vertical direction, given by

    throw_velocity_vertical = throw_velocity * math.sin(throw_angle)
    if(b_print):print(f"iv Throw velocity vertical: {throw_velocity_vertical:.2f}")

    # Ball air time
    g = 9.81
    ball_air_time = (throw_velocity_vertical + (math.sqrt((throw_velocity_vertical ** 2) + 2 * g * initiation_height))) / g
    if(b_print):print(f"v Ball air time: {ball_air_time:.2f}")

    # The throw distance, given by:

    throw_distance = throw_velocity_horizontal * ball_air_time
    if(b_print):print(f"vi Throw Distance: {throw_distance:.2f}")
    return throw_distance


angle = 30.0
velocity = 50.0
initiation_height = 2.0
standard_throw = calc_throw(angle, velocity, initiation_height, False)

print(f"Standard throw {standard_throw:.2f}")

#d It’s a common knowledge that throwing a ball at 45degrees angle
# gives the longest throw. But is that also true when you are standing
# up (h0>0)? Try h0=2, is the longest throw also at 45degrees, or will it
# be higher/lower (don’t need the optimal angle, just if a higher or
# lower degree is better)?

throw1 = calc_throw(46, 50, 2, False)
throw2 = calc_throw(45, 50, 2, False)
print(f"Throw1 {throw1:.2f}")
print(f"Throw2 {throw2:.2f}")