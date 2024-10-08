#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Sort coins in descending order to start with the largest coin
    coins.sort(reverse=True)
    
    count = 0
    for coin in coins:
        if total == 0:
            break
        count += total // coin
        total %= coin
    
    if total != 0:
        return -1
    
    return count

