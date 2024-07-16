'''
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/description/

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

'''

from collections import deque
def orangesRotting(grid):
    ROWS = len(grid)
    COLS = len(grid[0])

    q = deque()
    visited = set()
    freshOranges = 0

    def checkAndAppendFreshOrange(r, c):
        nonlocal freshOranges
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1 or (r,c) in visited:
            return
        q.append((r, c))
        visited.add((r, c))
        freshOranges -= 1

    # init bfs starting points (all already rotten oranges)
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 2:
                q.append((r,c))
                visited.add((r,c))
            if grid[r][c] == 1:
                freshOranges += 1
    
    if not q: return -1
    minutesElapsed = 0    
    while q and freshOranges > 0:
        qLen = len(q)
        while qLen > 0:
            r, c = q.popleft()
            adj = [[-1, 0], [0, 1], [1, 0], [0 ,- 1]]
            for x, y in adj:
                checkAndAppendFreshOrange(r + x , c + y)
            qLen -= 1
        minutesElapsed += 1
    return minutesElapsed if freshOranges == 0 else -1





if __name__ == "__main__":
   grid = [[2,1,1],[1,1,0],[0,1,1]]
   print(orangesRotting(grid))