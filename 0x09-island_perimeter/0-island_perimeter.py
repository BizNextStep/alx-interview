#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water
                                    and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the current cell's perimeter contribution
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1  # Top
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1  # Bottom
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1  # Left
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1  # Right

    return perimeter

