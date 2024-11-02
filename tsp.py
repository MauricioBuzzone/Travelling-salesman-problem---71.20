import numpy as np
import random

# Función principal de optimización por colonia de hormigas
def ant_colony_optimization(num_cities, num_ants, num_iterations, alpha, beta, evaporation, Q, distances):
    # Inicialización de matrices de feromonas y visibilidad
    pheromones = np.ones((num_cities, num_cities)) / num_cities
    visibility = 1 / (distances + np.eye(num_cities))  # Evitar división por 0

    best_path = None
    best_length = float('inf')

    for iteration in range(num_iterations):
        paths = []
        lengths = []
        
        # Cada hormiga construye una solución (camino)
        for ant in range(num_ants):
            path = build_path(num_cities, pheromones, visibility, alpha, beta)
            length = calculate_length(path, distances)
            paths.append(path)
            lengths.append(length)
            
            # Verificar si se encontró una mejor solución
            if length < best_length:
                best_length = length
                best_path = path
        
        # Actualizar feromonas basadas en los caminos de las hormigas
        pheromones = update_pheromones(paths, lengths, pheromones, evaporation, Q)
        
    return best_path, best_length

# Función para calcular la probabilidad de que una hormiga elija la siguiente ciudad
def calculate_probabilities(current_city, unvisited_cities, pheromones, visibility, alpha, beta):
    numerators = np.zeros(len(unvisited_cities))
    for i, city in enumerate(unvisited_cities):
        numerators[i] = (pheromones[current_city][city] ** alpha) * (visibility[current_city][city] ** beta)
    
    total = np.sum(numerators)
    
    # Control para evitar que la suma sea cero
    if total == 0:
        # Si no hay feromonas, elegir aleatoriamente
        return np.ones(len(unvisited_cities)) / len(unvisited_cities)  # Distribución uniforme
    
    probabilities = numerators / total
    return probabilities

# Función para que una hormiga construya un camino
def build_path(num_cities, pheromones, visibility, alpha, beta):
    current_city = random.randint(0, num_cities - 1)
    path = [current_city]
    while len(path) < num_cities:
        unvisited_cities = [city for city in range(num_cities) if city not in path]
        probabilities = calculate_probabilities(current_city, unvisited_cities, pheromones, visibility, alpha, beta)
        next_city = random.choices(unvisited_cities, weights=probabilities)[0]
        path.append(next_city)
        current_city = next_city
    return path

# Función para calcular la longitud total de un camino
def calculate_length(path, distances):
    length = 0
    for i in range(len(path) - 1):
        length += distances[path[i]][path[i + 1]]
    length += distances[path[-1]][path[0]]  # Regreso a la ciudad inicial
    return length

# Función para actualizar las feromonas
def update_pheromones(paths, lengths, pheromones, evaporation, Q):
    pheromones = (1 - evaporation) * pheromones  # Evaporar feromonas
    for path, length in zip(paths, lengths):
        for i in range(len(path) - 1):
            pheromones[path[i]][path[i + 1]] += Q / length
        pheromones[path[-1]][path[0]] += Q / length  # Regreso a la ciudad inicial
    return pheromones