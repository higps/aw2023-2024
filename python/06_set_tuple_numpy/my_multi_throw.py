import numpy as np
from scipy import stats
# 3. Go back to exercise ex3_numb_input.docx question 3, and
# copy the code from my_throw.py and save it as
# my_multi_thow.py.

# a. Change the variables velocities and angles to 3
# random numpy values for each. E.g.
# velocities = np.array([30, 40, 50])
# angels = np.array([40, 45, 50])
# Index 0 now represents the first throw (a throw with
# v=30, a=40), index 1 the second throw… etc.

grav_const = 9.81

# b. Change the np logic such that it can calculate
# multiple throw length based on the numpy array of

# angels and velocities.
# angle = np.array([40,45,50])
# velocity_kmt = np.array([30,40,50])

n = 1000
angle = stats.norm.rvs(loc=48, scale=7, size=n)
                                
velocity_kmt = stats.weibull_max.rvs(2,loc=107, scale=4, size=n)

# while his angle can be simulated using the following
# distribution:


init_hight = 2.0

alpha = np.radians(angle)
velocity_ms_0 = velocity_kmt/3.6
velocity_ms_0x = velocity_ms_0*np.cos(alpha)
velocity_ms_0y = velocity_ms_0*np.sin(alpha)
air_time = (velocity_ms_0y + np.sqrt(velocity_ms_0y**2 + 2*grav_const*init_hight))/grav_const
trhow_distance = velocity_ms_0x*air_time


print('Throw distance [R]:', trhow_distance)
print('Throw distance [R]:', len(trhow_distance))





# c. Install scipy using
# pip install scipy
# using CMD. Import stats from scipy in python by using
# from scipy import stats
# After some testing of the Olympic athlete javelin
# thrower Andreas Thorkildsen in 2008, it turns out that
# his throw velocity follows and can be simulated using
# the following distribution:
# stats.weibull_max.rvs(2,loc=107, scale=4, size=n),
# while his angle can be simulated using the following
# distribution:
# stats.norm.rvs(loc=48, scale=7, size=n)
# where n is the number of simulated values. (the
# functions above returns a numpy array of length n).
# simulate 1000 throws and calculate each throw
# length.



# d. Go back to exercise ex5_list.docx and copy the
# solution-code from question 3.
# and use the code to calculate a 95% numerical
# confidence interval (alpha=0.05) for a random throw
# from Andreas Thorkildsen.
# e. EXTRA Exercise:
# In a competition there are 6 throws but only the
# longest throw matters.
# generate 6000 velocities and angles and reorder them
# into a 2d-array which shape 1000x6 using the reshape
# method.
# again, use the np above and calculate the length of
# the 6000 throw length.
# afterward use the np.max function with the axis input
# and calculate each row max (the max length within
# each game), hench you should now have a simulated
# longest length throw for 6000 games.
# What is now the 95% numerical confidence interval of
# the winning length?