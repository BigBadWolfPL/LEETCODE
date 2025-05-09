from typing import List

test_1 = ["flower","flow","flight"]
test_2 = ["dog","racecar","car"]


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    min_len = min(len(w) for w in strs)
    for idx in range(min_len):
        for word in strs:
            if strs[0][idx] != word[idx]:
                return strs[0][:idx]
    return strs[0][:min_len]

print(longestCommonPrefix(test_1)) # "fl"
print(longestCommonPrefix(test_2)) # ""


"""
from typing import List

test_1 = ["flower","flow","flight"]
test_2 = ["dog","racecar","car"]


def longestCommonPrefix(strs: List[str]) -> str:
    min_len = min(len(w) for w in strs)
    for idx in range(min_len):
        previous = strs[0]
        for word in strs:
            if previous[idx] != word[idx]:
                return strs[0][:idx]
            previous = word
        

print(longestCommonPrefix(test_1)) # "fl"
print(longestCommonPrefix(test_2)) # ""

"""