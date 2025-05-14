from typing import List
import itertools


test_1 = [5,1,6] # 28
test_2 = [3,4,5,6,7,8] # 480



def subsetXORSum(nums: List[int]) -> int:
    result = 0
    for i in range(len(nums)+1):
        for sub in itertools.combinations(nums, i):
            xor = 0
            for num in sub:
                xor ^= num
            result += xor
    return result


print(subsetXORSum(test_1))
print(subsetXORSum(test_2))





"""
Example 2:

Input: nums = [5,1,6]
Output: 28
Explanation: The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
"""