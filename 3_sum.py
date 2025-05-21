from itertools import combinations
from typing import List



def threeSum(nums: List[int]) -> List[List[int]]:
    all_combs = combinations(nums, 3)
    result = {
        tuple(sorted(c)) for c in all_combs if sum(c) == 0
    }
    return list(result)





print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,0,0]))
print(threeSum([0,1,1]))

"""
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = [0,1,1]
Output: []

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
"""