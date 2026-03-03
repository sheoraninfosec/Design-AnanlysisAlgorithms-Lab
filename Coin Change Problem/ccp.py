# Author: Jigesh Sheoran
# Last Modified : 03 / 03 / 2026
# Experiment: Coin Change Problem (Minimum Coins)

def coin_change(coins, amount):
    # Initialize DP array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Fill DP array
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]


# user input
print("Coin Change Problem Program")

coins = list(map(int, input("Enter coin denominations separated by space:\n").split()))
amount = int(input("Enter target amount:\n"))

result = coin_change(coins, amount)

if result != -1:
    print("\nMinimum number of coins required:", result)
else:
    print("\nAmount cannot be formed with given coins.")

print("Program executed successfully.")
