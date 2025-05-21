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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = []
        while head:
            temp = []
            for _ in range(k):
                if not head:
                    break
                temp.append(head.val)
                head = head.next
            if len(temp) == k:
                result.extend(reversed(temp))
            elif temp:
                result.extend(temp)
                break
        if not result:
            return None
        new_head = ListNode(result[0])
        current = new_head

        for val in result[1:]:
            current.next = ListNode(val)
            current = current.next
        return new_head



"""
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
"""

test1 = ListNode.build_node([1,2,3,4,5])

tests = [test1]        


for t in tests:
    test_case = Solution.reverseKGroup(None,t, 2)
    while test_case:
        print(test_case.val)
        test_case = test_case.next
    print("----")

