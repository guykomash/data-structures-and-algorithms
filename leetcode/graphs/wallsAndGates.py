'''
286. Walls and Gates

You are given a m x n 2D rooms initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

Example 2:
Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]

'''

import unittest
from collections import deque


def wallsAndGates(rooms):
    ROWS = len(rooms)
    COLS = len(rooms[0])

    q = deque()
    visited = set()
    
    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] == 0:
                q.append((r, c))
                visited.add((r, c))
    
    def addEmptyRoom(r, c, dist):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS:
            return
        if (r,c) in visited:
            return
        if rooms[r][c] == -1 or rooms[r][c] == 0:
            return
        
        visited.add((r,c))
        q.append((r,c))
        rooms[r][c] = dist

    dist = 1
    while q:
        qLen = len(q)
        while qLen > 0:
            r, c = q.popleft()
            addEmptyRoom(r + 1, c, dist)
            addEmptyRoom(r - 1, c, dist)
            addEmptyRoom(r, c + 1, dist)
            addEmptyRoom(r, c - 1, dist)
            qLen -= 1
        dist += 1
    
    return rooms

class Test(unittest.TestCase):
    def test1(self):
        rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
        output = [ [3,-1,0,1],  [2,2,1,-1],  [1,-1,2,-1],  [0,-1,3,4]]
        self.assertEqual(wallsAndGates(rooms), output)

    def test2(self):
        rooms = [[0,-1], [2147483647,2147483647]]
        output = [[0,-1], [1,2]]
        self.assertEqual(wallsAndGates(rooms), output)


if __name__ == "__main__":
    unittest.main()