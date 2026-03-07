# Author: Jigesh Sheoran
# Last Modfiied : 07 / 03 / 2026
# Experiment: Rat in a Maze

def is_safe(maze, x, y, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1


def solve_maze(maze, x, y, solution, n):
    if x == n - 1 and y == n - 1:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y, n):
        solution[x][y] = 1

        # Move Down
        if solve_maze(maze, x + 1, y, solution, n):
            return True

        # Move Right
        if solve_maze(maze, x, y + 1, solution, n):
            return True

        # Backtrack
        solution[x][y] = 0
        return False

    return False


def print_solution(solution):
    for row in solution:
        print(" ".join(map(str, row)))


# user input
print("Rat in a Maze Program")

n = int(input("Enter size of maze (n for n×n):\n"))

print("Enter maze matrix (1 = open path, 0 = blocked):")
maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))

solution = [[0] * n for _ in range(n)]

if solve_maze(maze, 0, 0, solution, n):
    print("\nPath for the rat:")
    print_solution(solution)
else:
    print("\nNo path exists.")
