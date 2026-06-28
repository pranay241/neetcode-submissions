class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a placeholder dummy node to start the merged list
        dummy = ListNode(-1)
        tail = dummy

        # 2. Compare nodes from both lists and attach the smaller one
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next  # Move list1 pointer forward
            else:
                tail.next = list2
                list2 = list2.next  # Move list2 pointer forward
            
            tail = tail.next  # Move the merged list tail forward

        # 3. Append the remaining elements of the non-empty list
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # The actual merged list starts after the dummy node
        return dummy.next