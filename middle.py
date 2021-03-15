# Middle of a Linked List

# Basic Linked list operations

# When you submit this, you need to remove the argument 'self' from some function calls, I don't know why 

# https://leetcode.com/problems/middle-of-the-linked-list/submissions/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import math


class Solution(object):

    def node(self, front, index):
        if front is None:
            return None

        cur = front
        i = 0

        while i != index and cur.next is not None:
            cur = cur.next
            i += 1

        if i == index:
            return cur
        elif i != index and cur.next is None:
            return None

    def length(self, front):
        if front is None:
            l = 0
        else:
            l = 1
            cur = front
            while cur.next is not None:
                cur = cur.next
                l += 1

        return l

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_length = self.length(self, head)
        if head_length == 0:
            return None
        else:
            middle = math.floor(head_length / 2)  # 2*middle = head_length or 2*middle + 1 = head_length

        return self.node(self, head, middle)  # regard 'middle' as a 'zero index'


front = None
print(f"{'Len':<15}: {Solution.length(Solution, front=front)}")
print(f"{'Node (None)':<15}: {Solution.node(Solution, front=front, index=0)}")
print(f"{'Middle (None)':<15}: {Solution.middleNode(Solution, head=front)}")
print()

front = ListNode(val=0, next=None)
print(f"{'Len':<15}: {Solution.length(Solution, front=front)}")
print(f"{'Node (0)':<15}: {Solution.node(Solution, front=front, index=0).val}")
print(f"{'Middle':<15}: {Solution.middleNode(Solution, head=front).val}")
print()

front = ListNode(val=0, next=None)
front.next = ListNode(val=1, next=None)
print(f"{'Len':<15}: {Solution.length(Solution, front=front)}")
print(f"{'Node (0)':<15}: {Solution.node(Solution, front=front, index=0).val}")
print(f"{'Middle':<15}: {Solution.middleNode(Solution, head=front).val}")
print()

front = ListNode(val=0, next=None)
front.next = ListNode(val=1, next=None)
front.next.next = ListNode(val=2, next=None)
print(f"{'Len':<15}: {Solution.length(Solution, front=front)}")
print(f"{'Node (1)':<15}: {Solution.node(Solution, front=front, index=1).val}")
print(f"{'Middle':<15}: {Solution.middleNode(Solution, head=front).val}")
print()

front = ListNode(val=0, next=None)
front.next = ListNode(val=1, next=None)
front.next.next = ListNode(val=2, next=None)
front.next.next.next = ListNode(val=3, next=None)
print(f"{'Len':<15}: {Solution.length(Solution, front=front)}")
print(f"{'Node (3)':<15}: {Solution.node(Solution, front=front, index=3).val}")
print(f"{'Middle':<15}: {Solution.middleNode(Solution, head=front).val}")
print()
