class Stack():
    def __init__(self, maxLen):
        self.index = -1
        self.stack = [None for i in range(maxLen)]

    def push(self, val):
        self.index+=1
        self.stack[self.index] = val

    def pop(self):
        last_item = self.stack[self.index]
        self.index-=1
        return last_item

    def pick(self):
        return self.stack[self.index]

    def isEmpty(self):
        return self.index == -1



def isBalanced(s):

    if(s== ""): return "Yes"

    stck = Stack(len(s))

    for c in s:
        if c=="(" or c=="[":
            stck.push(c)

        else:

            if stck.isEmpty(): return "No"
            if c==")" and stck.pick()!="(": return "No"
            if c=="]" and stck.pick()!="[": return "No"

            stck.pop()

    if stck.isEmpty():
        return "Yes"

    return "No"




if __name__=="__main__":

    T = int(input())

    for i in range(0,T):

        string = str(input())

        print(isBalanced(string))

