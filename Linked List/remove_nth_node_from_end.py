from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build_node(cls, arr: List[int]):
        if not arr:
            return None
        head = cls(arr[0])
        current = head

        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        return head
    
test_node_1 = ListNode.build_node([1,2,3,4,5])


def read_reverse(node: Optional[ListNode]) -> None:
    if not node:
        return
    read_reverse(node.next)
    print(node.val)


read_reverse(test_node_1)