from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @classmethod
    def build(cls, arr: List[int]) -> Optional['ListNode']:
        if not arr:
            return None
        result = cls(arr[0])
        current = result

        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        return result
    
test_1 = ListNode.build([2,4,3])
test_2 = ListNode.build([5,6,4])




class Solution:
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        nadwyzka = 0

        while l1 or l2 or nadwyzka:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            suma = val_1 + val_2 + nadwyzka
            print(f"SUMA: {suma}")
            nadwyzka = suma // 10
            current.next = ListNode(suma % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next
    

solution_object = Solution.addTwoNumbers(test_1, test_2)


print("WYNIK:")
while solution_object:
    print(solution_object.val)
    solution_object = solution_object.next



"""
# Intuition
We need to add two numbers represented by linked lists, where each node contains a single digit and digits are stored in reverse order. This is similar to how we do manual addition from right to left, carrying over when the sum exceeds 9.

# Approach
We iterate through both linked lists simultaneously, summing corresponding digits along with any carry from the previous step. We use a dummy head node to simplify result list construction. If one list is shorter, we treat missing values as 0. The loop continues while there are remaining digits or a non-zero carry.

# Complexity
- Time complexity:  
$$O(n)$$, where \( n \) is the length of the longer list.

- Space complexity:  
$$O(n)$$, for the resulting linked list.

# Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        carry = 0

        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            suma = val_1 + val_2 + carry
            current.next = ListNode(suma % 10)
            current = current.next          
            carry = suma // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next
```

"""