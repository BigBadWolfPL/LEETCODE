from typing import Optional, List


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
    

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    current.next = list1 if list1 else list2
    return dummy.next
    

test1 = ListNode.build([1,2,4,8])
test2 = ListNode.build([1,3,4,5,6,7])


result = mergeTwoLists(test1, test2) # Output: [1,1,2,3,4,4,5,6,7]

while result:
    print(result.val)
    result = result.next



"""
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Tworzymy tzw. "sztuczną głowę" (ang. dummy head) – to tymczasowy węzeł początkowy,
    # który ułatwia konstruowanie nowej listy (nie trzeba traktować pierwszego elementu specjalnie).
    dummy = ListNode(-1)
    
    # 'tail' będzie zawsze wskazywał na ostatni element w nowo tworzonej liście.
    # Na początku to jest ten sztuczny węzeł.
    tail = dummy

    # Dopóki obie listy mają jeszcze elementy:
    while list1 and list2:
        # Jeśli wartość w bieżącym węźle listy 1 jest mniejsza,
        # dołącz ją do wyniku (czyli przypnij do tail.next)
        if list1.val < list2.val:
            tail.next = list1       # dołącz węzeł list1 do końca nowej listy
            list1 = list1.next      # przejdź do kolejnego węzła listy 1
        else:
            tail.next = list2       # dołącz węzeł list2 do końca nowej listy
            list2 = list2.next      # przejdź do kolejnego węzła listy 2

        # Przesuń tail do nowo dodanego węzła (ostatniego w wynikowej liście)
        tail = tail.next

    # Po zakończeniu pętli, tylko jedna z list może zawierać jeszcze elementy.
    # Ponieważ obie listy były posortowane, pozostałe elementy też są już na właściwym miejscu.
    # Wystarczy więc dołączyć pozostałość jednej z nich .
    tail.next = list1 if list1 else list2

    # Zwracamy faktyczny początek nowej listy (pomijamy sztuczną głowę)
    return dummy.next

"""