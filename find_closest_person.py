class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        cx, cy = abs(x - z), abs(y - z)
        return 1 if cx < cy else 2 if cy < cx else 0


case_1 = Solution()


assert case_1.findClosest(2, 7, 4) == 1
assert case_1.findClosest(1, 5, 3) == 0
