#!/usr/bin/python3
"""
Module for calculating the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the given total amount.

    Args:
        coins (list of int): The values of the coins in possession.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total amount.
             Returns -1 if the total cannot be met by any number of coins.
    """
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
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))     # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
