# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        current = head

        while current:
            current.val = current.val - 10000
            if current.val <=-10000:
                return True
            current = current.next
        return False