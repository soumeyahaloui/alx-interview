#!/usr/bin/python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes_up_to_n(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def isWinner(x, nums):
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = get_primes_up_to_n(n)
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