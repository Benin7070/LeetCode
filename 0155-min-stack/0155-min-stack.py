from collections import deque
class MinStack:

    def __init__(self):
        self.container=deque()
        self.min_con=deque()
    def push(self, val: int) -> None:
        self.container.append(val)
        if not self.min_con or val<=self.min_con[-1]:
            self.min_con.append(val) 
    def pop(self) -> None:
        val=self.container.pop()
        if val==self.min_con[-1]:
            self.min_con.pop()
    def top(self) -> int:
        return self.container[-1]
    def getMin(self) -> int:
        return self.min_con[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()