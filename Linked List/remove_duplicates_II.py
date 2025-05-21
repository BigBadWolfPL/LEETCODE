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
    @staticmethod
    def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        unique = []
        counter = dict()
        prev = None
        current = None
        while head:
            prev = head.val
            head = head.next if head else None
            current = head.val if head else None

            counter[prev] = counter.get(prev, 0) + 1
            if prev != current:
                if counter.get(prev) == 1:
                    unique.append(prev)
        if not unique:
            return None
        new_head = ListNode(unique[0])
        new_current = new_head

        for val in unique[1:]:
            new_current.next = ListNode(val)
            new_current = new_current.next
        return new_head


"""
TESTS
"""

test1 = ListNode.build_node([1,2,3,3,4,4,5])
test2 = ListNode.build_node([1,1,1,2,3])
test3 = ListNode.build_node([1,1,1,1,1])
test4 = ListNode.build_node([1,2,3,4,5])
test5 = ListNode.build_node([1,1,3,4,5])
test6 = ListNode.build_node([1,2,3,4,4])
test7 = ListNode.build_node([1,1,2,3,3,4,5,5,6])

tests = [test1, test2, test3, test4, test5, test6, test7]        


for t in tests:
    test_case = Solution.deleteDuplicates(t)
    while test_case:
        print(test_case.val)
        test_case = test_case.next
    print("----")


