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
        while head:
            start_section = head
            end_section = head
            print(f"Start_SECTION: {start_section.val}")   
            for _ in range(k-1):
                end_section = end_section.next if end_section else None
                if end_section:
                    print(f"END SECTION: {end_section.val}")
            head = end_section.next if end_section else None

            if not end_section:
                break



"""
🔁 Podpowiedź:
Aby odwrócić grupę między start_section a end_section in-place, potrzebujesz trzech wskaźników:

prev – zaczyna jako None, będzie przesuwany po każdym węźle,

curr – zaczyna jako start_section, to aktualny węzeł do przestawienia,

next – tymczasowy wskaźnik na curr.next, aby nie stracić dostępu do reszty listy.

🔧 Działanie:
Wykonaj k razy:


next = curr.next
curr.next = prev
prev = curr
curr = next
Po zakończeniu:

prev wskazuje na nowy początek odwróconej sekcji,

start_section (czyli dawny początek) będzie teraz końcem i trzeba go połączyć z kolejnym węzłem po end_section.

To lokalne odwrócenie możesz wykonywać w każdej iteracji pętli głównej.


"""
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        while head:
            start_section = head
            print(f"Start_SECTION: {start_section.val}")
            for _ in range(k-1):
                head = head.next if head else None
                if head:
                    print(f"NEXT NODE: {head.val}")
                start_section = head
                if not head:
                    break
                print("----")
            head = start_section.next if start_section else None





Mam listę jednokierunkową (ListNode) o nazwie test_case:
1 -> 2 -> 3 -> 4 -> 5

klasycznie odczytuje taką listę w pętli while:

while test_case:
    print(test_case.val)
    test_case = test_case.next


Jak mogę odczytać ją od końca?
5 -> 4 -> 3 -> 2 -> 1

nie tworząc przy tym dodatkowych struktur ...

test1 = ListNode.build_node([1,2,3,4,5])

tests = [test1]        



def print_reversed(node):
    if node is None:
        return
    print_reversed(node.next)
    print(node.val)

print_reversed(test1)
"""              
        




"""
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
"""

test1 = ListNode.build_node([1,2,3,4,5])

tests = [test1]        


for t in tests:
    test_case = Solution.reverseKGroup(None,t, 4)
    while test_case:
        print(test_case.val)
        test_case = test_case.next
    print("----")

