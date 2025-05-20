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
    

test1 = ListNode.build_node([1,2,3,3,4,4,5]) # [1,2,5]
test2 = ListNode.build_node([1,1,1,2,3]) # [2,3]


class Solution:
    def deleteDuplicates(head: Optional[ListNode]):
        prev = None
        current = None
        while head:
            prev = head.val
            head = head.next
            current = head.val if head else None
            if prev == current:
                head = head.next
                continue
            else:
                print(prev)
            
case_1 = Solution.deleteDuplicates(test1)
print("---")
case_2 = Solution.deleteDuplicates(test2)

#while test:
#    print(test.val)
#    test = test.next