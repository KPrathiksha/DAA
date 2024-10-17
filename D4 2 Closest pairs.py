import math
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def closest_pair(points):
    min_distance = float('inf')
    closest_points = (None, None)    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_points = (points[i], points[j]) 
    return closest_points
points = [(10, 0), (11, 5), (5, 3), (9, 3.5), (15, 3), (12.5, 7), (6, 6.5), (7.5, 4.5)]
closest_points = closest_pair(points)
print("Closest pair of points:", closest_points)
def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
def convex_hull(points):
    n = len(points)
    if n < 3:
        return []
    hull = []  
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(n):
                    if k != i and k != j:
                        if orientation(points[i], points[j], points[k]) == 0:
                            hull.append(points[i])
                            hull.append(points[j])
                            hull.append(points[k])   
    return list(set(hull))
points = [(10, 0), (11, 5), (5, 3), (9, 3.5), (15, 3), (12.5, 7), (6, 6.5), (7.5, 4.5)]
hull_points = convex_hull(points)
print("Convex Hull points:", hull_points)
