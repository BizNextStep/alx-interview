#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Helper function to calculate primes up to max_n using Sieve of Eratosthenes"""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

def isWinner(x, nums):
    """Determines the winner of the game"""
    if x <= 0 or not nums:
        return None

    # Determine the maximum number n in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Number of primes up to n determines the total moves possible
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

