from dataclasses import dataclass #https://www.geeksforgeeks.org/python/understanding-python-dataclasses/

@dataclass
class ACOConfig:
    iterations: int = 100
    colony_size: int = 50
    evap_coeff: float = 0.10
    alpha: float = 9.0
    beta: float = 12.0
    initial_tau: float = 1e-4
    Q: float = 0.2 # Pheromone deposit factor
    el: float = 0.97 # Elitism factor
    data_path: str = "./data/berlin52.csv"
    random_seed: int | None = 42 # Set to None for true randomness