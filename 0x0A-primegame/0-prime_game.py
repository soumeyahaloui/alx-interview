#!/usr/bin/python3

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def isWinner(x, nums):
    # Define a function to check if there are primes left in the list
    def primes_left(nums):
        for num in nums:
            if is_prime(num):
                return True
        return False
    
    # Iterate over each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = generate_primes(n)
        # If there are no primes left, Maria loses
        if not primes_left(primes):
            ben_wins += 1
        else:
            # If the number of primes is even, Maria wins, otherwise Ben wins
            if len(primes) % 2 == 0:
                maria_wins += 1
            else:
                ben_wins += 1
    
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))