from typing import List, Optional
import unittest


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



class Solution:
    def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        while head:
            first = head
            if first:
                for _ in range(n):
                    previous = head.val if head else None
                    head = head.next if head else None  
                    
                    f_val = head.next.val if head else None
                    print(f"Second: {previous}, First: {f_val}")
            head = head.next if head else None

            
            
            #head = head.next

s

result_1 = Solution.removeNthFromEnd(test_node_1, 2)

while result_1:
    print(result_1.val)
    result_1 = result_1.next


'''
TESTS

class Solution:
    def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = []
        while head:
            result.append(head.val)
            head = head.next

        if not result or len(result) == 1:
            return None
        result.pop(-n)
        
        new_head = ListNode(result[0])
        current = new_head

        for val in result[1:]:
            current.next = ListNode(val)
            current = current.next
        return new_head



class TestRemoveNthFromEnd(unittest.TestCase):
    def test_val_in_list(self):
        tested = Solution.removeNthFromEnd(ListNode.build_node([1,2,3,4,5]), 2)
        expected = ListNode.build_node([1,2,3,5])

        while tested or expected:
            test_val = tested.val if tested else None
            exp_val = expected.val if expected else None

            self.assertEqual(test_val, exp_val, f"Difrent values: {test_val} != {exp_val}")
            tested = tested.next if tested else None
            expected = expected.next if expected else None


    def test_one_element_one_remove(self):
        tested = Solution.removeNthFromEnd(ListNode.build_node([1]), 1)
        test_val = tested.val if tested else None
        self.assertEqual(test_val, None, f"Result not None: {test_val}")

if __name__ == "__main__":
    unittest.main()

'''


"""

def read_reverse(node: Optional[ListNode], c=0) -> None:
    if not node:
        return
    c += 1
    print(c, node.val)
    read_reverse(node.next, c)
    print(node.val, c)


read_reverse(test_node_1)

"""


