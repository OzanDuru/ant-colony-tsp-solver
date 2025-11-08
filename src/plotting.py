# src/plotting.py
import numpy as np
import matplotlib.pyplot as plt

def plot_best_route(x: np.ndarray, y: np.ndarray, tour: list[int], best_distance: float):
    plt.figure(figsize=(6,6))
    plt.scatter(x, y, marker='o')
    xs = [x[i] for i in tour]
    ys = [y[i] for i in tour]
    plt.plot(xs, ys, linestyle='--', marker='o')
    plt.title(f"En İyi Tur (Maliyet = {best_distance:.2f})")
    plt.xlabel("X"); plt.ylabel("Y")
    plt.tight_layout(); plt.show()

def plot_convergence(best_progress: list[float], avg_progress: list[float]):
    iters = range(1, len(best_progress)+1)
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.plot(iters, best_progress, label="Best-so-far")
    plt.plot(iters, avg_progress, label="Ortalama")
    plt.xlabel("İterasyon"); plt.ylabel("Mesafe"); plt.title("Yakınsama (Best & Ortalama)")
    plt.legend()

    plt.subplot(1,2,2)
    plt.plot(iters, best_progress)
    plt.xlabel("İterasyon"); plt.ylabel("Best-so-far")
    plt.title("En İyi Tur Mesafesi")
    plt.tight_layout()
    plt.savefig("best_route.png", dpi=150, bbox_inches="tight")
    plt.close()

