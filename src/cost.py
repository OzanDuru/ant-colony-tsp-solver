import numpy as np

def compute_cost_and_reference(tours: list[list[int]], 
                               distance: np.ndarray,
                               el: float) -> tuple[np.ndarray, np.ndarray]:
    m = len(tours)
    costs = np.zeros(m,dtype=float)
    for i,tour in enumerate(tours): #https://www.geeksforgeeks.org/python/enumerate-in-python/
        total_distance = 0.0
        for j in range(len(tour)-1):#-1 olmasının sebebi son nokta ile başla noktasını ayrıca eklemek, son-nokta ile (sonraki) bağlantı için -1
            current_city = tour[j]
            next_city = tour[j+1]
            distance_between = distance[current_city,next_city]
            total_distance += distance_between
        
        costs[i] = total_distance 



    best = costs.min()
    reference = costs - best * el   
    reference = np.maximum(reference, 1e-12) 
    return costs, reference

