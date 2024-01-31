# a)
# Go back to ex3_numb_input.docx exercise 2 (NOT the
# numpy exercise from ex6_set_tuple_numpy.docx
# exercise 3) and encapsulate the calculation logic into
# a function called “throw_distance” which takes 3
# inputs, “velocity”, “angle”, “init_height”.
# Set init_height default to 1.8. The function should
# return throw length.
import math


#b)
# Write a new function called “kmh_to_ms” which
# takes as input a velocity in km/h and return the m/s.
# Change the code in “throw_distance” such that it
# uses the “kmh_to_ms” function.
def kmh_to_ms(velocity):
    return velocity / 3.6

# c)
#  Write a new function called
# “velocity_decomposition”. The function should take
# two inputs “velocity” and “angle”, and return two
# values, the horizontal and vertical velocity.
# Change the code in “throw_distance” such that it
# uses the “velocity_decomposition” function.

def velocity_decomposition(velocity, throw_angle):
    throw_velocity = kmh_to_ms(velocity)
    horiztonal = throw_velocity * math.cos(throw_angle)
    vertical = throw_velocity * math.sin(throw_angle)
    return horiztonal, vertical


# d)
# Write a new function called “airtime” which takes as
# input the velocity in vertical direction “velocity_y”,
# “init_height” and gravitation “g” (with default 9.81)
# and returns the airtime.
# Change the code in “throw_distance” such that it
# uses the “airtime” function.

def airtime(vertical_y, init_height, g=9.81):
    return (vertical_y + (math.sqrt((vertical_y ** 2) + 2 * g * initiation_height))) / g

def throw_distance(angle, velocity, initiation_height:float)->float:
    
    throw_angle = math.radians(angle)
    #if(b_print):print(f"i Throw angle: {throw_angle:.2f}")

    throw_velocity = kmh_to_ms(velocity)
   # if(b_print):print(f"ii Throw velocity: {throw_velocity:.2f}")
    decomp = velocity_decomposition(throw_velocity, throw_angle)

    throw_velocity_horizontal = decomp[0]
  #  if(b_print):print(f"iii Throw velocity horizontal: {throw_velocity_horizontal:.2f}")

    throw_velocity_vertical = decomp[1]
   # if(b_print):print(f"iv Throw velocity vertical: {throw_velocity_vertical:.2f}")
    g = 9.81
    ball_air_time = airtime(throw_velocity_vertical, initiation_height)
  #  if(b_print):print(f"v Ball air time: {ball_air_time:.2f}")

    throw_length = throw_velocity_horizontal * ball_air_time
   # if(b_print):print(f"vi Throw Distance: {throw_distance:.2f}")
    return throw_length

angle = 30.0
velocity = 50.0
initiation_height = 1.8
standard_throw = throw_distance(angle, velocity, initiation_height)

print(f"Standard throw {standard_throw:.2f}")

# e)
# Create a new function called “throw_possition”,
# which takes the same inputs as “throw_distance”
# with an extra variable called “time”.
# The function should return the distance
# (horizontal velocity * time), only if the input “time” is
# smaller than “airtime”, else just the result of
# “throw_distance” without the time parameters.
# Try to reuse the sub functions above instead of
# rewriting logic 