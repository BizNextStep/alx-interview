#!/usr/bin/python3
'''Prime game module.
'''

def isWinner(x, nums):
    '''Determines the winner from an array of games played
    '''
    # Check for invalid input
    if x < 1 or not nums:
        return None
    # Initialize scores for Maria and Ben
    maria, ben = 0, 0

    # Find the maximum number in nums
    max_n = max(nums)
    # Create a list to mark prime numbers
    primes = [True for _ in range(1, max_n + 1, 1)]
    primes[0] = False
    # Implement the Sieve of Eratosthenes to find all primes up to max_n
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, max_n + 1, i):
            primes[j - 1] = False

    # Evaluate each game to determine the winner
    for _, n in zip(range(x), nums):
        # Count the number of primes up to n
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        # Update scores based on the count of primes
        ben += primes_count % 2 == 0
        maria += primes_count % 2 == 1

    # Determine the overall winner
    if maria == ben:
        return None
    return 'Maria' if maria > ben else 'Ben'
