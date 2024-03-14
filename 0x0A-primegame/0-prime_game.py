#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False

    return [i for i, is_prime in enumerate(primes) if is_prime]

def isWinner(x, nums):
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        total_moves = len(primes)

        # If the total number of primes is even, Ben wins
        if total_moves % 2 == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] == wins["Ben"]:
        return None
    elif wins["Maria"] > wins["Ben"]:
        return "Maria"
    else:
        return "Ben"

# Example usage
print("Winner:", isWinner(3, [4, 5, 1]))
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))