"""
554. Brick Wall
https://leetcode.com/problems/brick-wall/

There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.
"""

# Solve later
def leastBricks(wall):
        ROWS = len(wall)
        bricksInRow = sum(wall[0])
        validCols = [ROWS] * (bricksInRow - 1)

        for r in range(ROWS):
            cur = 0
            for b in wall[r]:
                cur += b
                # print(b)
                if cur < len(validCols):
                    validCols[cur] -= 1
        # print(validCols)
        return min(validCols) 

if __name__ == "__main__":
    # wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    wall = [[1],[1],[1]]
    res = leastBricks(wall)
    print(res)