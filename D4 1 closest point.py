import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def brute_force(points):
    min_dist = float("inf")
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, dist(points[i], points[j]))
    return min_dist

def strip_closest(strip, d):
    strip.sort(key=lambda point: point[1])  # Sort by y-coordinate
    min_dist = d

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            min_dist = min(min_dist, dist(strip[i], strip[j]))
    return min_dist

def closest_util(points):
    n = len(points)
    if n <= 3:
        return brute_force(points)

    mid = n // 2
    mid_point = points[mid]

    dl = closest_util(points[:mid])
    dr = closest_util(points[mid:])
    d = min(dl, dr)

    # Points within the vertical strip
    strip = [p for p in points if abs(p[0] - mid_point[0]) < d]
    return min(d, strip_closest(strip, d))

def closest(points):
    points.sort()  # Sort by x-coordinate
    return closest_util(points)

# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("The smallest distance is", closest(points))
