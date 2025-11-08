import numpy as np

def update_pheromone(tau: np.ndarray,
                     tours: list[list[int]],
                     reference: np.ndarray,
                     evap_coeff: float,
                     Q: float,
                     symmetric: bool = False) -> np.ndarray:
    new_tau = tau.copy()
    for k, tour in enumerate(tours):
        ref = float(reference[k])
        if ref <= 1e-12:
            ref = 1e-12
        delta = Q / ref
        
        for j in range(len(tour)-1):#bu kapalı bir tur olduğu için son nokta ile başla noktasını ayrıca eklemeye gerek yok
            i_city,j_city = tour[j],tour[j+1]
            new_tau[i_city,j_city] = (1 - evap_coeff) * new_tau[i_city,j_city] + delta
            if symmetric:
                 new_tau[j_city, i_city] = (1 - evap_coeff) * new_tau[j_city, i_city] + delta

    return new_tau
