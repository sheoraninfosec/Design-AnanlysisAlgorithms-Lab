# Author: Jigesh Sheoran
# Last Modififed : 06 / 03 / 2026
# Experiment: Activity Selection Problem

def activity_selection(start, finish):
    n = len(start)

    activities = list(zip(start, finish))
    activities.sort(key=lambda x: x[1])  # sort by finish time

    selected = [activities[0]]

    last_finish = activities[0][1]

    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]

    return selected


# user input 
print("Activity Selection Problem Program")

n = int(input("Enter number of activities:\n"))

print("Enter start times separated by space:")
start = list(map(int, input().split()))

print("Enter finish times separated by space:")
finish = list(map(int, input().split()))

selected = activity_selection(start, finish)

print("\nSelected Activities (start, finish):")
for act in selected:
    print(act)

print("Program executed successfully.")
