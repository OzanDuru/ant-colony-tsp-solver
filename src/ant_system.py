import numpy as np
from .config import ACOConfig
from .io_utils import load_berlin52_csv,build_distance_matrix,build_eta_from_distance,init_tau
from .tour_construction import construct_ant_tours
from .cost import compute_cost_and_reference
from .pheromone import update_pheromone
from .plotting import plot_convergence,plot_best_route


def run_aco(cfg :ACOConfig): # Main function to run the Ant Colony Optimization algorithm

    if cfg.random_seed is not None:# Set random seed for reproducibility
        np.random.seed(cfg.random_seed) #https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html

    x,y = load_berlin52_csv(cfg.data_path) # Load city coordinates

    n= len(x) # Number of cities
    
    distance_matrix = build_distance_matrix(x,y)
    eta=build_eta_from_distance(distance_matrix) # Build heuristic information (eta)
    tau = init_tau(n,cfg.initial_tau) # Initialize pheromone matrix

    best_dist = float("inf") # Initialize best distance to infinity
    best_tour: list[int] | None = None # Initialize best tour
    best_progress: list[float] = [] 
    avg_progress: list[float] = []

    for it in range(1 , cfg.iterations + 1):
        tours = construct_ant_tours(cfg.colony_size, n, tau, eta, cfg.alpha, cfg.beta)
        costs, reference = compute_cost_and_reference(tours, distance_matrix, cfg.el)
        tau = update_pheromone(tau, tours,reference,cfg.evap_coeff,cfg.Q,symmetric=False)

        idx = int(np.argmin(costs)) # Index of the best tour in this iteration
        iter_best = float(costs[idx]) # Cost of the best tour in this iteration (cost ,float sayı)
        iter_best_tour = tours[idx] # Tour of the best ant in this iteration ( liste )

        if iter_best < best_dist:
            best_dist = iter_best
            best_tour = iter_best_tour

        best_progress.append(best_dist)
        avg_progress.append(float(costs.mean()))
        if it == 1 or it % 50 == 0 or it == cfg.iterations:
            print(f"[{it:03d}] best-so-far={best_dist:.4f}  iter-best={iter_best:.4f}  mean={costs.mean():.4f}")


    

    if best_tour is not None:
        plot_best_route(x, y, best_tour, best_dist)
    plot_convergence(best_progress, avg_progress)

    return best_dist, best_tour, best_progress, avg_progress    
    


       
