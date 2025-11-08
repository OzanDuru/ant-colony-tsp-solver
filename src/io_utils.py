#Veri okuma, mesafe ve heuristic hazırlığı
import numpy as np
import pandas as pd

def load_berlin52_csv(path: str ) -> tuple[np.ndarray, np.ndarray]:
    df=pd.read_csv(path,header=None,names=['x','y'])
    x = df['x'].to_numpy(dtype=float)
    y = df['y'].to_numpy(dtype=float)
    return x, y


def build_distance_matrix(x : np.ndarray , y : np.ndarray)-> np.ndarray:
    num_cities = len (x)
    dx =x.reshape((num_cities,1)) - x.reshape((1,num_cities)) #Bütün şehir çiftleri arasındaki x farkları
    dy =y.reshape((num_cities,1)) - y.reshape((1,num_cities))

    distance = np.sqrt(dx*dx + dy*dy) #Öklidyen mesafe
    np.fill_diagonal(distance,0.0) #Kendine uzaklık sonsuz olsun
    return distance


def build_eta_from_distance(distance: np.ndarray) -> np.ndarray:
    with np.errstate(divide='ignore'):
        eta = 1.0 / distance

    eta[~np.isfinite(eta)] = 0.0 # Sonsuzluk ve NaN değerlerini 0 yap

    return eta


def init_tau(n: int , initial_tau: float) -> np.ndarray:
    return np.full((n,n), initial_tau, dtype=float)
    
    

        