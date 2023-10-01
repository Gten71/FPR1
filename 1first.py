def closest_city_distance(distances):
    min_distance = min(distances)
    return min_distance

distances = [100, 200, 150, 300, 250, 180, 120, 220, 190, 280, 240, 210, 270, 320, 170]
result = closest_city_distance(distances)
print(f"Расстояние до ближайшего города: {result} км")
