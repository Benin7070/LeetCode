from collections import deque
class MinStack:

    def __init__(self):
        self.container=deque()
    def push(self, val: int) -> None:
        self.container.append(val)
    def pop(self) -> None:
        self.container.pop()
    def top(self) -> int:
        return self.container[-1]
    def getMin(self) -> int:
        return min(self.container)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()