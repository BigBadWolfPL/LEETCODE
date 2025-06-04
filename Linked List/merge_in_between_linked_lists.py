from typing import List


def main():
    Solution.mergeInBetween(node1, 3, 4, node2)



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
    

node1 = ListNode.build([10,1,13,6,9,5])
node2 = ListNode.build([1000000,1000001,1000002])




class Solution:
    @staticmethod
    def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        while list1 or list2:
            v1 = list1.val if list1 else "Koniec węzła n1"
            v2 = list2.val if list2 else "Koniec węzła n2"

            print(f"Node1: {v1} | Node2: {v2}")

            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None




if __name__ == "__main__":
    main()