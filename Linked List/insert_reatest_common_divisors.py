from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build_ll(cls, arr: List[int]):
        if not arr:
            return None
        head = cls(arr[0])
        current = head

        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        return head
    

test1 = ListNode.build_ll([18,6,10,3])
test2 = ListNode.build_ll([7])


class Solution:
    @staticmethod
    def insertGreatestCommonDivisors(head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while head:
            val1 = head.val
            current.next = head
            current = current.next
            head = head.next
            if head:
                val2 = head.val
                while val2 != 0:
                    val1, val2 = val2, val1 % val2
                current.next = ListNode(val1)
                current = current.next
        return dummy.next


sol1 = Solution.insertGreatestCommonDivisors(test1)


"""
Output: [18,6,6,2,10,1,3]
"""

while sol1:
    print(sol1.val)
    sol1 = sol1.next


"""
class Solution:
    @staticmethod
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while head:
            val1 = head.val
            current.next = ListNode(val1)
            current = current.next
            head = head.next
            if head:
                val2 = head.val
                while val2 != 0:
                    val1, val2 = val2, val1 % val2
                current.next = ListNode(val1)
                current = current.next
        return dummy.next


"""