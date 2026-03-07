# Author: Jigesh Sheoran
# Last Modified : 07 / 03  / 2026
# Experiment: Minimum Number of Platforms

def min_platforms(arrival, departure):
    n = len(arrival)

    arrival.sort()
    departure.sort()

    platforms = 1
    max_platforms = 1

    i = 1
    j = 0

    while i < n and j < n:
        if arrival[i] <= departure[j]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1

        max_platforms = max(max_platforms, platforms)

    return max_platforms


# user input
print("Minimum Number of Platforms Program")

arrival = list(map(int, input("Enter arrival times separated by space:\n").split()))
departure = list(map(int, input("Enter departure times separated by space:\n").split()))

if len(arrival) != len(departure):
    print("Error: Arrival and departure lists must be the same length.")
else:
    result = min_platforms(arrival, departure)
    print("\nMinimum number of platforms required:", result)

print("Program executed successfully.")
