# Prime Game

## Description

This project implements a game called "Prime Game" where two players, Maria and Ben, take turns picking prime numbers from a set of consecutive integers starting from 1 up to and including `n`. Once a prime number is chosen, that number and all its multiples are removed from the set. The player who cannot make a move loses the game. 

The function `isWinner(x, nums)` determines the winner after `x` rounds of the game, where `n` (the maximum number for each round) is provided in the list `nums`. Maria always goes first, and both players play optimally.

## Function Prototype

```python
def isWinner(x, nums):
    # Your code here

