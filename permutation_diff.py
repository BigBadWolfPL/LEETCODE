class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_positions = {v: k for k, v in enumerate(s)}
        return sum(abs(s_positions[letter] - idx) for idx, letter in enumerate(t))

print(Solution.findPermutationDifference(None, "abc", "bac"))