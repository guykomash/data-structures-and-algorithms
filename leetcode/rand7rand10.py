import random
class Solution:
    def __init__(self):
        self.board = [[None for i in range(7)] for i in range(7)]
        n = 0
        for r in range(7):
            for c in range(7):
                self.board[r][c] = n % 10
                n += 1

    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = self.rand7() - 1
            col = self.rand7() - 1
            if row < 5 or row == 5 and col < 5:
                return self.board[row][col] + 1

    def rand7(self):
        return random.randint(1, 7)
    

class Solution2:
    def __init__(self):
        self.array = [0] * 25
        i = 0
        n = 1
        while i <= 20:
            self.array[i] = n
            n = n + 1
            if n == 8:
                n = 1
            i = i + 1

    def rand7(self):
        while True:
            code1 = self.rand5() - 1
            code2 = self.rand5() - 1
            if code1 < 4 or code1 == 4 and code2 == 0:
                 return self.array[code1 * 5 + code2]
           
    def rand5(self):
        return random.randint(1, 5)
    
    def rand25(self):
        array25 = [0] * 25
        for i in range(len(array25)):
            array25[i] = i + 1

        code1 = self.rand5() - 1
        code2 = self.rand5() - 1

        return array25[code1 * 5 + code2]


class Solution3:
    def __init__(self):
        self.board = [[None for i in range(5)] for i in range(5)]
        n = 0
        for r in range(5):
            for c in range(5):
                self.board[r][c] = n % 7
                n += 1
        print(self.board)
    def rand7(self):
        """
        :rtype: int
        """
        while True:
            row = self.rand5() - 1
            col = self.rand5() - 1
            if row < 5 or row == 5 and col < 5:
                return self.board[row][col] + 1

    
    def rand5(self):
        return random.randint(1, 5)
    
if __name__ == "__main__":
    sol = Solution2()
    results = {}
    for i in range(100000):
        val = sol.rand25()
        results[val] = 1 + results.get(val, 0)
    # print(results.items())
    formated = sorted(list(results.items()), key= lambda x :x[0])
    print(formated)