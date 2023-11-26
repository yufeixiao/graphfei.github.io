# Natural language

## (1) informed individual
in a system of N particles, each particle has a base level of information about its environment and the group's objective. this is similar to how a school of fish that is migrating has a goal of going to the migratory destination, or the school of fish that is foraging has a goal of finding clumps of shrimps and recruiting the group to exploit that food site. 

we are considering 2 minimal modes where individuals calibrate their information to the environment: (1) each individual has an inherent level of sensitivity to the true right direction, which persists to affect the orientation of the individual without changing over time from neighbor influence, and this is parameterized by the ratio of individuals who are informed, and the strength of this external information or belief compared to the influence of neighbors.  the individuals who are informed are randomly assigned instead of based on original location in the system, because the system is supposedly an infinite canvas. (2) individuals have different levels of social influence over others, meaning that some individuals can have a higher weight in the alignment of a neighbor than others. this doesn't affect the individual's orientation itself. this mechanism is borrowing from observations that some animals who are more senior or higher in the hierarchy can affect more members through closer proximity to many others or higher channel sensitivity of others towards them. 

## (2) swarming
at each time step, the particles can interact in an infinite size system (with periodic boundary). 
there are 3 modes of interaction: (1) metric (parameterized by distance threshold), (3) topological (KNN, parameterized by K), (3) topological (Voronoi). I'm not including the topological (Delaunay triangle) mode or the vision based mode (parameterized by loss over distance). 
the interaction with neighbors affects the orientation of the particles, parameterized by an alignment strength (but not by repulsion and attraction).

we are interested in how the swarming (and furthermore, the different modes of interaction) affects the role of information processing in the group -- does its mechanism for integrating information change? is it still through clustering? is the overall accuracy and efficiency of the information-processing group increasing or decreasing when the group can swarm, compared to when the group is static? we are not exploring the effect of 1D vs 2D vs 3D space, or position-based instead of direction-based sites. 

# Formal
## Parameters and Constants:
Informed Individual:
- N: Total number of particles
- ratio_informed: Ratio of informed individuals in the system
- external_info_strength: Strength of external information compared to neighbor influence

Social Influence:
- social_influence_weights: Array representing the social influence weights of each individual

Swarming Interaction:
- interaction_mode: Metric (1), Topological - KNN (2), Topological - Voronoi (3)
- interaction_threshold: Distance threshold for metric interaction
- k_neighbors: Number of neighbors for KNN interaction

Alignment Strength:
- alignment_strength: Strength of alignment behavior during interaction

# Formulas:
Informed Individual: 
- Each particle's orientation is influenced by both external information and the average orientation of its neighbors.

Social Influence:
- Weighted average of neighbors' orientations, where weights are given by social_influence_weights.

Swarming Interaction:
- Depending on the interaction mode, calculate neighbors and update the orientation based on the average of their orientations.
