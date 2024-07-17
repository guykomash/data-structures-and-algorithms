'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/description/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

def numIslands(grid):
    ROWS = len(grid)
    COLS = len(grid[0])

    visited = set()
    
    
    def dfs(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS:
            return
        
        if (r,c) in visited: 
            return

        if grid[r][c] == "0":
            return
        
        visited.add((r,c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    res = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r,c) not in visited:
                dfs(r,c)
                res += 1

    return res






if __name__ == "__main__":
    grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


print(numIslands(grid1))
print(numIslands(grid2))