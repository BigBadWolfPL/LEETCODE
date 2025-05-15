from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def build(cls, arr: List[int]):
        if not arr:
            return None
        head = cls(arr[0])
        current = head

        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        return head



node_1 = ListNode.build([2,4,3])
node_2 = ListNode.build([5,6,4,2])


while node_1 or node_2:
    val_1 = node_1.val if node_1 else 0
    val_2 = node_2.val if node_2 else 0

    print(f"VAL 1: {val_1} VAL 2: {val_2}")

    node_1 = node_1.next if node_1 else None
    node_2 = node_2.next if node_2 else None
