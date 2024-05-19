v = 6.75e-8

density_list = [round(0.54 + i * 0.02, 2) for i in range(int((0.75 - 0.54) / 0.02) + 1)]

#print(density_list)
length_list = []
for density in density_list:
    length_list.append((v / density)**(1/3))

print(length_list)