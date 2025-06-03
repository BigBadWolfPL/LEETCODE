from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build(cls, arr: List[int]):
        if not arr:
            return
        head = cls(arr[0])
        current = head

        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        return head


class Solution:
    @staticmethod
    def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        nodes_sum = 0
        head = head.next

        while head:
            nodes_sum = 0
            while head.val != 0:
                nodes_sum += head.val
                head = head.next
            current.next = ListNode(nodes_sum)
            current = current.next

            head = head.next
        return dummy.next
























"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        modify = head.next  # Start from the node after the initial 0
        next_sum = modify

        while next_sum:
            total = 0
            # Find the sum of all nodes until you encounter a 0.
            while next_sum.val != 0:
                total += next_sum.val
                next_sum = next_sum.next

            # Assign the sum to the current node's value.
            modify.val = total
            # Move next_sum to the first non-zero value of the next block.
            next_sum = next_sum.next
            # Move modify also to this node.
            modify.next = next_sum
            modify = modify.next

        return head.next  # Skip the initial 0 node
"""







case1 = Solution.mergeNodes(ListNode.build([0,3,1,0,4,5,2,0])) # [4, 11]
print("---")
case2 = Solution.mergeNodes(ListNode.build([0,1,0,3,0,2,2,0])) # [1, 3, 4]

while case1:
    print(case1.val)
    case1 = case1.next

print("---")

while case2:
    print(case2.val)
    case2 = case2.next