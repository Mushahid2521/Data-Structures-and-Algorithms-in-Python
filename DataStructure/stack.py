class Node():
    def __init__(self, val):
        self.data = val
        self.next = None


class Stack():
    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head == None:
            self.head = Node(val)

        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head == None:
            return None

        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def retData(self):
        return self.head.data

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False