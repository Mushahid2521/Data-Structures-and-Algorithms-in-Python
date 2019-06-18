class Node():
    def __init__(self, val):
        self.data = val
        self.next = None


class Que():
    def __init__(self):
        self.head = None
        self.last = None

    def pop(self):
        if self.head == None:
            return None

        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def push(self, val):
        if self.last == None:
            self.head = Node(val)
            self.last = self.head
        else:
            new_node = Node(val)
            self.last.next = new_node
            self.last = new_node



if __name__=="__main__":
    a_que = Que()

    a_que.push(30)
    a_que.push(10)
    a_que.push(20)
    a_que.push(50)

    print(a_que.pop())
    print(a_que.pop())
    print(a_que.pop())
    print(a_que.pop())