# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    # Use a stack to move from left to right. Then pop from right and check again with traversing
    stck = []
    head = l
    while head != None:
        stck.append(head.value)
        head = head.next

    while l != None:
        if stck.pop(-1) != l.value:
            return False
        l = l.next

    return True

