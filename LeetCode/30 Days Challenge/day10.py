class MinStack(object):

    def __init__(self):
        self.array = [None] * (1000000)
        self.pos = -1

    def push(self, x):
        if self.pos <0:
            m = x
        else:
            m = self.array[self.pos][1]
        if x < m:
            m = x
        self.pos += 1
        self.array[self.pos] = [x, m]

    def pop(self):
        if self.pos >= 0:
            self.pos -= 1

    def top(self):
        return self.array[self.pos][0]

    def getMin(self):
        return self.array[self.pos][1]


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
# obj.push(10)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# [-3,-2,-5,4]