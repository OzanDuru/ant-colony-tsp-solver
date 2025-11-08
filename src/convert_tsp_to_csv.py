def convert_tsp_to_csv(tsp_path, csv_path):
    with open(tsp_path, 'r') as f:
        lines = f.readlines()

    coords = []
    reading_coords = False

    for line in lines:
        line = line.strip()
        if line.startswith("NODE_COORD_SECTION"):
            reading_coords = True
            continue
        if line.startswith("EOF"):
            break
        if reading_coords:
            parts = line.split()
            if len(parts) >= 3:
                x, y = float(parts[1]), float(parts[2])
                coords.append((x, y))

    # CSV olarak kaydet
    with open(csv_path, 'w') as out:
        for x, y in coords:
            out.write(f"{x},{y}\n")

    print(f"✅ Dönüştürüldü: {len(coords)} satır kaydedildi -> {csv_path}")

if __name__ == "__main__":
    convert_tsp_to_csv("./data/berlin52.tsp", "./data/berlin52.csv")
