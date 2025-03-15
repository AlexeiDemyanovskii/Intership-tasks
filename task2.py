import sys

def read_circle(file_path):
    with open(circle_values_jason, 'r') as file:
        center = list(map(float, file.readline().strip().split()))
        radius = float(file.readline().strip())
        return center, radius

def read_points(values.json):
    with open(values_jason, 'r') as file:
        points = [list(map(float, line.strip().split())) for line in file]
        return points

def point_circle_position(center, radius, point):
    x0, y0 = center
    x, y = point
    distance_squared = (x - x0) ** 2 + (y - y0) ** 2
    radius_squared = radius ** 2

    if distance_squared < radius_squared:
        return 1  # Внутри
    elif distance_squared == radius_squared:
        return 0  # На окружности
    else:
        return 2  # Снаружи

def main(circle_file_path, points_values_jason):
    center, radius = read_circle(circle_values_jason)
    points = read_points(points_values_jason)

    for point in points:
        position = point_circle_position(center, radius, point)
        print(position)

if __name__ == "__main__":
    circle_values_jason = sys.argv[1]
    points_file_path = sys.argv[2]
    main(circle_values_jason, points_values_jason)