
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def findMiddle(self):
        node = self
        cnt = 0
        while node!= None:
            cnt+=1
            node = node.next

        node = self
        for i in range(int(cnt/2)):
            node = node.next

        return node

    def findMiddleFast(self):
        fast = self
        slow = self

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.val)
        return slow


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.findMiddle()
node1.findMiddleFast()