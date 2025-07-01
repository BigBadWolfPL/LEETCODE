from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build(cls, arr):
        if not arr:
            return
        head = cls(arr[0])
        current = head

        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        return head


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        prev = None

        while head:
            if head.val != prev:
                prev = head.val
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        return dummy.next
    
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head and head.next:
            if head.val != head.next.val:
                print(head.val)
            head = head.next
        if head:
            print(head.val)

"""

"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # pomijamy duplikat
            else:
                current = current.next  # przechodzimy dalej tylko jeśli nie ma duplikatu
        return head

"""





first_node = ListNode.build([0,0,0,0,0,1,1,2,3,4,5,5,5])
sol = Solution.deleteDuplicates(None, first_node)



while sol:
    print(sol.val)
    sol = sol.next
