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
    

test1 = ListNode.build_node([1,2,3,3,4,4,5])
test2 = ListNode.build_node([1,1,1,2,3])
test3 = ListNode.build_node([1,1,1,1,1])
test4 = ListNode.build_node([1,2,3,4,5])
test5 = ListNode.build_node([1,1,3,4,5])
test6 = ListNode.build_node([1,2,3,4,4])
test7 = ListNode.build_node([1,1,2,3,3,4,5,5,6])



class Solution:
    def deleteDuplicates(head: Optional[ListNode]):
        result = []
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
                    result.append(prev)
        return result

            

print(f"Case 1: {[1,2,5] == Solution.deleteDuplicates(test1)}")
print(f"case 2: {[2,3]== Solution.deleteDuplicates(test2)}")
print(f"Case 3: {[] == Solution.deleteDuplicates(test3)}")
print(f"Case 4: {[1,2,3,4,5] == Solution.deleteDuplicates(test4)}")
print(f"Case 5: {[3,4,5] == Solution.deleteDuplicates(test5)}")
print(f"Case 6: {[1,2,3] == Solution.deleteDuplicates(test6)}")
print(f"Case 7: {[2,4,6] == Solution.deleteDuplicates(test7)}")


#while case_1:
#    print(case_1.val)
#    case_1 = case_1.next