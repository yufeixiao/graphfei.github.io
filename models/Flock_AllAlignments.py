# generated by GPT. 
# from first read, it seems that there is no true_direction parameter, and no periodic boundary for the neighbor selection. 

import numpy as np

# Parameters and Constants
N = 100  # Total number of particles
ratio_informed = 0.1  # Ratio of informed individuals
external_info_strength = 0.2  # Strength of external information

social_influence_weights = np.random.rand(N)  # Random social influence weights for each individual

interaction_mode = 2  # Interaction mode: 1 (Metric), 2 (Topological - KNN), 3 (Topological - Voronoi)
interaction_threshold = 10.0  # Distance threshold for metric interaction
k_neighbors = 5  # Number of neighbors for KNN interaction

alignment_strength = 0.1  # Strength of alignment behavior during interaction

# Particle Data Structure
class Particle:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.informed = np.random.rand() < ratio_informed

# Initialize particles
particles = [Particle(np.random.rand(), np.random.rand(), np.random.rand() * 2 * np.pi) for _ in range(N)]

# Update function for Informed Individuals
def update_informed():
    for particle in particles:
        if particle.informed:
            # Update based on external information
            particle.angle += external_info_strength * (np.random.rand() * 2 * np.pi - particle.angle)

# Update function for Swarming Interaction
def update_swarming():
    for particle in particles:
        neighbors = get_neighbors(particle)

        if len(neighbors) > 0:
            # Update based on the average orientation of neighbors
            average_orientation = np.mean([neighbor.angle for neighbor in neighbors])
            particle.angle += alignment_strength * (average_orientation - particle.angle)

# Function to get neighbors based on interaction mode
def get_neighbors(particle):
    if interaction_mode == 1:  # Metric Interaction
        return [neighbor for neighbor in particles if np.linalg.norm([particle.x - neighbor.x, particle.y - neighbor.y]) < interaction_threshold]
    elif interaction_mode == 2:  # Topological - KNN Interaction
        distances = [np.linalg.norm([particle.x - neighbor.x, particle.y - neighbor.y]) for neighbor in particles]
        sorted_indices = np.argsort(distances)
        return [particles[i] for i in sorted_indices[1:k_neighbors + 1]]  # Exclude itself
    elif interaction_mode == 3:  # Topological - Voronoi Interaction
        # Implement Voronoi interaction (not included in this basic example)
        pass

# Main simulation loop
for _ in range(num_steps):  # Define num_steps according to your simulation duration
    update_informed()
    update_swarming()
    # Additional steps for visualization or data collection, if needed
