from typing import Optional, List


def main():
    test_1 = ListNode.build([2,4,3])
    test_2 = ListNode.build([5,6,4])

    result_obj = Solution.addTwoNumbers(test_1, test_2)
    #result_obj
#
    while result_obj:
        print(result_obj.val)
        result_obj = result_obj.next



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def bulid(cls, arr: List[int]) -> Optional['ListNode']:
        if not arr:
            return None
        head = cls(arr[0])
        current = head

        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        return head



class Solution:
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)  # Tworzymy "sztuczny" pierwszy węzeł. Ułatwia operowanie na liście.
        current = result      # Wskaźnik do końca naszej budowanej listy wynikowej
        carry = 0            # Przeniesienie (np. 5 + 7 = 12 => zapisujemy 2, przenosimy 1)

        # Dopóki mamy coś do dodania (czyli l1, l2 lub przeniesienie)
        while l1 or l2 or carry:
            # Pobieramy wartość z l1 lub 0, jeśli już się skończyła podobnie l2
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0

            # Suma dwóch cyfr + przeniesienie z poprzedniego kroku
            total = val_l1 + val_l2 + carry
            print(f"l1.val = {l1.val}, l2.val = {l2.val} | TOTAL: {total}")

            # Nowe przeniesienie: ile "dziesiątek" w tej sumie?
            carry = total // 10
            print(f"Carry: {carry}")

            # Tworzymy nowy węzeł z cyfrą jedności i dokładamy do listy wynikowej
            current.next = ListNode(total % 10)

            # Przesuwamy wskaźnik w naszej nowej liście wynikowej
            current = current.next

            # Przesuwamy l1 i l2 (jeśli się nie skończyły)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Zwracamy listę wynikową — pomijając sztuczny początek
        return result.next




if __name__ == "__main__":
    main()
"""
class Solution:
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr_l1, arr_l2 = [], []
        while l1:
            arr_l1.append(l1.val)
            l1 = l1.next
        while l2:
            arr_l2.append(l2.val)
            l2 = l2.next
        temp = int("".join((str(x) for x in arr_l1[::-1]))) + int("".join((str(x) for x in arr_l2[::-1])))

        result = [int(x) for x in str(temp)[::-1]]
        return ListNode.build(result)

"""

"""
@classmethod
def build_node(cls, arr: List[int]) -> Optional['ListNode']:
    # Jeśli lista wejściowa jest pusta, nie tworzymy żadnego węzła — zwracamy None.
    if not arr:
        return None

    # Tworzymy pierwszy węzeł (głowę listy) z pierwszego elementu tablicy `arr`.
    # `cls` odnosi się do samej klasy (ListNode), dzięki czemu metoda zadziała też w klasach pochodnych.
    first = cls(arr[0])

    # `current` wskazuje na ostatni utworzony węzeł — na początku jest to `first`.
    # Będziemy go przesuwać, by dodawać kolejne węzły.
    current = first

    # Iterujemy po pozostałych elementach tablicy (czyli od drugiego do ostatniego)
    for num in arr[1:]:
        # Tworzymy nowy węzeł z bieżącą wartością `num` i podłączamy go do `current.next`
        current.next = cls(num)

        # Przesuwamy `current` do nowo utworzonego węzła, żeby kolejne były do niego dołączane
        current = current.next

    # Zwracamy wskaźnik na pierwszy element listy, od którego możemy dotrzeć do wszystkich kolejnych
    return first

"""

"""
Input: l1 = [2,4,3], l2 = [5,6,4]

Output: [7,0,8]

Explanation: 342 + 465 = 807.
"""