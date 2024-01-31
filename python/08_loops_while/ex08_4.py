# The year is 2008, right before the start of the Beijing
# summer Olympics.
# Andreas Thorkildsen and Tero Pitkamaki are the favorites
# for the javelin competition.
# While practicing running up to the Olympics, they were
# both carefully measuring their performance by throw
# velocity and throw angle (see image below):


# By testing hundreds of athletes, it turns out that throw
# velocity follows a Weibull distribution, while the angle
# follows a normal distribution.
# Using the velocity and angle data obtained running up to
# the Olympics each of the distribution for Thorkildsen
# and Pitkamaki can be estimated by:
# Using the distributions above, “throw_distance” and
# import scipy.stats as stats
# # Thorkildsen single throw velocity and angle:
# thorkildsen _velocity = stats.weibull_max.rvs(2, loc=107, scale=4, size=1)[0]
# thorkildsen _angle = stats.norm.rvs(48, 7, 1)[0]
# # Pitkamaki single throw velocity and angle:
# pitkamaki _velocity = stats.weibull_max.rvs(2, loc=106.5, scale=3, size=1)[0]
# pitkamaki _angle = stats.norm.rvs(45.5, 4, 1)[0]
# “quantile” functions from ex_7_functions.docx exercise 4
# and 5:
# 

import math
import scipy.stats as stats

def kmh_to_ms(velocity):
    return velocity / 3.6

def velocity_decomposition(velocity, throw_angle):
    throw_velocity = kmh_to_ms(velocity)
    horiztonal = throw_velocity * math.cos(throw_angle)
    vertical = throw_velocity * math.sin(throw_angle)
    return horiztonal, vertical


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

#angle = 30.0
#velocity = 50.0
initiation_height = 1.8
#standard_throw = throw_distance(angle, velocity, initiation_height)


# a).
# Create the functions “thorkildsen_throw()”
# and “pitkamaki_throw()”, which takes no inputs and
# returns a single throw distance for each of the
# athletes-functions


def thorkildsen_throw():
    # Thorkildsen single throw velocity and angle:
    thorkildsen_velocity = stats.weibull_max.rvs(2, loc=107, scale=4, size=1)[0]
    thorkildsen_angle = stats.norm.rvs(48, 7, 1)[0]
    return throw_distance(thorkildsen_velocity, thorkildsen_angle, initiation_height)

def pitkamaki_throw():
    # Pitkamaki single throw velocity and angle:
    pitkamaki_velocity = stats.weibull_max.rvs(2, loc=106.5, scale=3, size=1)[0]
    pitkamaki_angle = stats.norm.rvs(45.5, 4, 1)[0]
    return throw_distance(pitkamaki_velocity, pitkamaki_angle, initiation_height)

print(pitkamaki_throw(), thorkildsen_throw())
# b)
# In javelin competition you only care about the longest
# of 6 throws. Write a
# “thorkildsen_competion_best(numb_throw=6)” and
# “pitkamaki_competion_best(numb_throw=6)” that
# takes one input, number of throw which default to 6
# and return the best of those throws using the
# functions in question a)
