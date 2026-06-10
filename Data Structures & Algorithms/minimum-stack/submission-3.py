class MinStack:  

    def __init__(self):
        self.minVal=float('inf')
        self.stack=[]

    def push(self, val: int) -> None:
        if val<self.minVal:
            self.minVal=val
        self.stack.append((val,self.minVal))

    def pop(self) -> None:
        self.stack.pop()

        if self.stack:
            self.minVal=self.stack[-1][1]
        else:
            self.minVal=float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
