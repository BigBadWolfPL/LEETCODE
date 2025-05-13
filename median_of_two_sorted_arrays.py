from typing import List


def main():
    findMedianSortedArrays(test_1, test_2)




def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    print("działa")
    pass










test_1 = [1,3]
test_2 = [3]



def binary_search(arr: List[int], searched: int) -> str:
    start = 0
    end = len(arr) - 1
    count = 0
    while start <= end:
        count += 1
        middle = (end + start) // 2
        if searched == arr[middle]:
            return f"Znaleziono: {searched}, operacje: {count}"
        elif searched < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return f"Brak {searched} w przeszukiwanej liście"


if __name__ == "__main__":
    main()