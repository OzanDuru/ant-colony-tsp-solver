# main.py
from src.config import ACOConfig
from src.ant_system import run_aco

if __name__ == "__main__":
    cfg = ACOConfig(
        iterations=150,
        colony_size=50,
        evap_coeff=0.10,
        alpha=9,
        beta=12,
        initial_tau=1e-4,
        Q=0.2,
        el=0.97,
        data_path="data/berlin52.csv",
        random_seed=42
    )
    best_dist, best_tour, _, _ = run_aco(cfg)
    print("\nBitti.")
    print(f"En iyi mesafe: {best_dist:.4f}")
    print(f"Tur (indeksler): {best_tour}")
