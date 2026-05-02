# A salesman needs to visit a set of cities exactly once and return to the original city. 
#The task is to find the shortest possible route that the salesman can take to visit all the cities and return to the starting city.
import numpy as np
import random

# Step 1: Distance Matrix (Example: 5 cities)

distances = np.array([
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
])

num_cities = len(distances)
num_ants = 10
num_iterations = 50

# ACO parameters
alpha = 1       # importance of pheromone
beta = 2        # importance of distance
evaporation = 0.5
Q = 100

# Initialize pheromone matrix
pheromone = np.ones((num_cities, num_cities))

# Step 2: Function to calculate total distance

def total_distance(path):
    dist = 0
    for i in range(len(path) - 1):
        dist += distances[path[i]][path[i+1]]
    dist += distances[path[-1]][path[0]]  # return to start
    return dist

# Step 3: ACO Algorithm

best_path = None
best_length = float('inf')

for iteration in range(num_iterations):
    all_paths = []
    all_lengths = []

    for ant in range(num_ants):
        visited = [False]*num_cities
        path = []

        # Start from random city
        current_city = random.randint(0, num_cities-1)
        path.append(current_city)
        visited[current_city] = True

        # Visit all cities
        for _ in range(num_cities - 1):
            probabilities = []
            for city in range(num_cities):
                if not visited[city]:
                    tau = pheromone[current_city][city] ** alpha
                    eta = (1 / distances[current_city][city]) ** beta
                    probabilities.append(tau * eta)
                else:
                    probabilities.append(0)

            probabilities = np.array(probabilities)
            probabilities = probabilities / probabilities.sum()

            next_city = np.random.choice(range(num_cities), p=probabilities)
            path.append(next_city)
            visited[next_city] = True
            current_city = next_city

        length = total_distance(path)
        all_paths.append(path)
        all_lengths.append(length)

        if length < best_length:
            best_length = length
            best_path = path

    # Step 4: Pheromone Update
    
    pheromone *= (1 - evaporation)

    for path, length in zip(all_paths, all_lengths):
        for i in range(len(path) - 1):
            a = path[i]
            b = path[i+1]
            pheromone[a][b] += Q / length
            pheromone[b][a] += Q / length   # ✅ FIX: update reverse direction
        
        # return to start
        a = path[-1]
        b = path[0]
        pheromone[a][b] += Q / length
        pheromone[b][a] += Q / length   # ✅ FIX: update reverse direction

# Step 5: Output Best Route

print("Best path:", best_path)
print("Shortest distance:", best_length)
