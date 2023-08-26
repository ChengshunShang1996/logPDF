import numpy as np

# Start with an empty array for particle positions
particle_positions = np.empty((0, 3))

print(particle_positions)

# Add three particles to the array
particle1 = np.array([0.1, 0.2, 0.3])
particle2 = np.array([0.4, 0.5, 0.6])
particle3 = np.array([0.7, 0.8, 0.9])

particle_positions = particle1

#particle_positions = np.vstack((particle_positions, particle1))
#particle_positions = np.vstack((particle_positions, particle2))
#particle_positions = np.vstack((particle_positions, particle3))

print("Particle Positions:")
print(particle_positions)