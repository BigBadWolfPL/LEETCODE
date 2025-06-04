from typing import List
from datetime import datetime


def main():
    t1 = datetime.now()
    node1 = ListNode.build([10,1,13,6,9,5])
    node2 = ListNode.build([1000000,1000001,1000002])
    for _ in range(1):
        result = Solution.mergeInBetween(node1, 3, 4, node2)
        
        while result:
            print(result.val)
            result = result.next
    t2 = datetime.now()

    print(f"TIME= {t2-t1}")


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
    def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        cut = 0
        while list1:
            cut += 1
            current.next = list1
            current = current.next
            if cut == a:
                for _ in range(b-a+1):
                    list1 = list1.next
                while list2:
                    current.next = list2
                    current = current.next
                    list2 = list2.next
            list1 = list1.next
        return dummy.next
    

"""
class Solution:
    @staticmethod
    def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Krok 1: znajdź węzeł przed `a`
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next

        # Krok 2: znajdź węzeł po `b`
        after_b = prev_a
        for _ in range(b - a + 2):
            after_b = after_b.next

        # Krok 3: połącz prev_a z list2
        prev_a.next = list2

        # Krok 4: znajdź koniec list2 i połącz z after_b
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = after_b

        return list1


"""

if __name__ == "__main__":
    main()