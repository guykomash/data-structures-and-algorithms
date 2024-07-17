class MinStack:

    def __init__(self):
        self.stack = []
        self.minHistory = []

    def push(self, val: int) -> None:
        if not self.minHistory or val <= self.minHistory[-1]:
            self.minHistory.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack: return
        if self.stack[-1] == self.minHistory[-1]:
            self.minHistory.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHistory[-1]
