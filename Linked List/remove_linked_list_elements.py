from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build_node(cls, arr: list):
        if not arr:
            return None
        head = cls(arr[0])
        current = head

        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        return head
    


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = ListNode()
        current = new_head
        while head:
            if head.val != val:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        return new_head.next

            





"""
TESTS
"""

test1 = ListNode.build_node([1,2,6,3,4,5,6])
test2 = ListNode.build_node([])
test3 = ListNode.build_node([7,7,7,7])
tests = [test1, test2, test3]        

for t in tests:
    test_case = Solution.removeElements(None,t, 7)
    while test_case:
        print(test_case.val)
        test_case = test_case.next
    print("----")

