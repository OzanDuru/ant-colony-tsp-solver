#Karınca turları (olasılıksal seçim)

import numpy as np

def construct_ant_tours(colony_size: int,
                        num_cities: int,
                        tau: np.ndarray,
                        eta: np.ndarray,
                        alpha: float,
                        beta: float) -> list[list[int]]:
    tours: list[list[int]] = []
    for _ in range(colony_size): #bu döngü her karınca için bir tur oluşturur
        start=np.random.randint(0,num_cities)
        tour = [start]
        visited = set([start])

        for _ in range(num_cities - 1): #kalan şehirleri ziyaret et
            current_city = tour[-1] #en son ziyaret edilen şehir
            attractiveness = (tau[current_city, :]**alpha) * (eta[current_city, :]**beta)
            # Ziyaret edilen şehirlerin attractiveness nı  sıfırla
            if visited: #zaten 0 dı ama koruyucu olsun diye ekledik
                idx = np.fromiter(visited, dtype=int)
                attractiveness[idx] = 0.0
            
            s =attractiveness.sum()
            if s <= 0.0:#bazen olsaılk 0 olabiliyor ve o noktafda tüm şehirler anlamasız gelebiliyor öyle bir durumda gidilmemmiş şehirleirden ilkini seçemek için bir kontrol ekliyoruz
                remaining = list(set(range(num_cities)) - visited) 
                next_city = remaining[0]#gidilmemiş şehirlerden ilkini seç
            else:
                probs = attractiveness / s
                next_city = np.random.choice(num_cities, p=probs) #https://www.geeksforgeeks.org/python/random-choices-method-in-python/


            tour.append(next_city)
            visited.add(next_city)

        tour.append(start) #başlangıç şehrine dön
        tours.append(tour)

    return tours



            
