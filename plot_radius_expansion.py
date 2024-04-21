import numpy as np
import matplotlib.pyplot as plt

def calculate_radius_multiplier(time, is_radius_expansion_rate_change, radius_expansion_acceleration=0, radius_expansion_rate=0, radius_multiplier_max=2, delta_time=0, radius_expansion_rate_min = 100):
    if is_radius_expansion_rate_change:
        radius_expansion_rate_ini = radius_expansion_rate
        radius_expansion_rate += radius_expansion_acceleration * time

        if radius_expansion_rate > radius_expansion_rate_min:
            radius_multiplier = 1.0 + time * (radius_expansion_rate + radius_expansion_rate_ini) * 0.5
        else:
            time_needed = (radius_expansion_rate_min - radius_expansion_rate_ini) / radius_expansion_acceleration
            radius_multiplier_part_1 = time_needed * (radius_expansion_rate_min + radius_expansion_rate_ini) * 0.5
            radius_multiplier_part_2 = (time - time_needed) * radius_expansion_rate_min
            radius_multiplier = 1.0 + radius_multiplier_part_1 + radius_multiplier_part_2
    else:
        radius_multiplier = 1.0 + time * radius_expansion_rate_min

    if radius_multiplier > radius_multiplier_max:
        radius_multiplier = radius_multiplier_max

    return radius_multiplier

def plot_radius_multiplier(time_range, radius_multiplier_func, title):
    time_values = np.linspace(time_range[0], time_range[1], 100)
    radius_multiplier_values = [radius_multiplier_func(t) for t in time_values]

    plt.plot(time_values, radius_multiplier_values, 'o-')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Radius Multiplier')
    plt.grid(True)
    plt.show()

is_radius_expansion_rate_change = True
radius_expansion_acceleration_list = ['-4e5', '-5e5', '-6e5']
radius_expansion_rate = 1000
radius_expansion_rate_min = 100
radius_multiplier_max = 2
delta_time=2e-9
time_range = [0, 0.012]
time_values = np.linspace(time_range[0], time_range[1], 100)
for radius_expansion_acceleration in radius_expansion_acceleration_list:
    radius_multiplier_values_list = []
    my_label = 'Nonlinear, a = ' + radius_expansion_acceleration
    radius_expansion_acceleration = float(radius_expansion_acceleration)
    for t in time_values:
        value = calculate_radius_multiplier(t, is_radius_expansion_rate_change, radius_expansion_acceleration, radius_expansion_rate, radius_multiplier_max, delta_time, radius_expansion_rate_min)
        radius_multiplier_values_list.append(value/2)
    plt.plot(time_values, radius_multiplier_values_list, '-', linewidth = 3, label = my_label)
    #for i in range(len(time_values)):
    #    print(str(time_values[i]) +  ' ' + str(radius_multiplier_values_list[i]))

is_radius_expansion_rate_change=False
radius_expansion_rate_min_list = [100, 150, 200]
for radius_expansion_rate_min in radius_expansion_rate_min_list:
    radius_multiplier_values_list = []
    my_label = 'Linear, v = ' + str(radius_expansion_rate_min)
    for t in time_values:
        value = calculate_radius_multiplier(t, is_radius_expansion_rate_change, radius_expansion_acceleration, radius_expansion_rate, radius_multiplier_max, delta_time, radius_expansion_rate_min)
        radius_multiplier_values_list.append(value/2)
    plt.plot(time_values, radius_multiplier_values_list, '--', linewidth = 3, label = my_label)

plt.xlim(0.0, 0.012)
plt.ylim(0.5, 1.1)
plt.xlabel('Time / s')
plt.ylabel('Radius multiplier')
plt.grid(True)
plt.legend()
plt.show()
