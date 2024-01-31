import math

grav_const = 9.81

angle_str = input('Input the throw angle (degrees): ')
velocity_kmt_str = input('Input the throw velocity (km/t): ')
init_hight_str = input('Input the initial hight (m): ')

angle = float(angle_str)
velocity_kmt = float(velocity_kmt_str)
init_hight = float(init_hight_str)

alpha = math.radians(angle)
velocity_ms_0 = velocity_kmt/3.6
velocity_ms_0x = velocity_ms_0*math.cos(alpha)
velocity_ms_0y = velocity_ms_0*math.sin(alpha)
air_time = (velocity_ms_0y + math.sqrt(velocity_ms_0y**2 + 2*grav_const*init_hight))/grav_const
trhow_distance = velocity_ms_0x*air_time

print(f'Throw angle in radians [alpha]: {alpha:.2f}')
print(f'Throw velocity in m/s [v_0]: {round(velocity_ms_0, 2)}')
print(f'Throw velocity in the horizontal direction [v_x]: {velocity_ms_0x:.2f}')
print(f'Throw velocity in the vertical direction [v_y]: {round(velocity_ms_0y,2)}')
print(f'Airtime [t]: {air_time:.2f}')
print(f'Throw distance [R]: {round(trhow_distance,2)}')