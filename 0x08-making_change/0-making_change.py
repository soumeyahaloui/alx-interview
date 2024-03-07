def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins needed to make each amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Base case: 0 coins needed to make 0

    # Iterate through each coin value
    for coin in coins:
        # Update min_coins for each amount from coin to total
        for amount in range(coin, total + 1):
            min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    # If min_coins[total] is still float('inf'), total cannot be met
    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]

# Test cases
print(makeChange([1, 2, 25], 37))     # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
