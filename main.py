import sys
import numpy as np
from tsp import ant_colony_optimization
from csvReader import read


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <ruta_del_archivo_csv>")
    else:
        ruta_archivo = sys.argv[1]
        places = read(ruta_archivo)
        print(places)
"""
# Example usage
CITIES = 10
ANTS = 100
ITERS = 100
ALPHA = 1
BETA = 2
EVAPORATION = 0.5
Q = 100

# Generate random distances between cities
np.random.seed(42)
distances = np.random.randint(10, 100, size=(CITIES, CITIES))
np.fill_diagonal(distances, 0)

# Run the ACO algorithm
def run_multiple_configurations(num_cities, distances):
    results = []

    for num_ants in range(10, 51, 5):
            for alpha in range(0, 6, 1):
                for beta in range(1, 6, 1):
                    for evaporation in np.arange(0.1, 1.0, 0.1):
                        for Q in [1,10,20,30,40,50,60,70,80,90,100]:
                            # Ejecutar ACO con los parámetros actuales
                            best_path, best_length = ant_colony_optimization(
                                num_cities=num_cities,
                                num_ants=num_ants,
                                num_iterations=ITERS,
                                alpha=alpha,
                                beta=beta,
                                evaporation=evaporation,
                                Q=Q,
                                distances=distances
                            )
                            # Almacenar los resultados
                            results.append({
                                'num_ants': num_ants,
                                'num_iterations': ITERS,
                                'alpha': alpha,
                                'beta': beta,
                                'evaporation': evaporation,
                                'Q': Q,
                                'best_path': best_path,
                                'best_length': best_length
                            })
                            print(f"Run with ants={num_ants}, iters={ITERS}, alpha={alpha}, beta={beta}, evap={evaporation}, Q={Q} -> Best Length: {best_length}")
    
    return results

# Ejecutar múltiples configuraciones
# results = run_multiple_configurations(CITIES, distances)
# best_result = min(results, key=lambda x: x['best_length'])

best_result, best_length = ant_colony_optimization(
                                num_cities=CITIES,
                                num_ants=ANTS,
                                num_iterations=ITERS,
                                alpha=ALPHA,
                                beta=BETA,
                                evaporation=EVAPORATION,
                                Q=Q,
                                distances=distances
                            )
print("\nBest configuration found:")
print(best_result)
"""
