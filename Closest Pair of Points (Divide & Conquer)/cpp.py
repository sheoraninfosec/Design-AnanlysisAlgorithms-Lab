# Author: Jigesh Sheoran
# Last Modified : 26 / 02 / 2026
# Experiment: Closest Pair of Points

import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def brute_force(points):
    min_dist = float('inf')
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, distance(points[i], points[j]))

    return min_dist


def strip_closest(strip, d):
    min_dist = d
    strip.sort(key=lambda x: x[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            min_dist = min(min_dist, distance(strip[i], strip[j]))

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

    strip = []
    for point in points:
        if abs(point[0] - mid_point[0]) < d:
            strip.append(point)

    return min(d, strip_closest(strip, d))


def closest_pair(points):
    points.sort(key=lambda x: x[0])
    return closest_util(points)


# user input 
print("Closest Pair of Points Program")

n = int(input("Enter number of points:\n"))

points = []
print("Enter points as x y:")
for _ in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

result = closest_pair(points)

print("\nMinimum Distance:", result)
print("Program executed successfully.")
