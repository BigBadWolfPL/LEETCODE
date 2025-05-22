from typing import List
import unittest


class Solution:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i


class TestRemoveElement(unittest.TestCase):
    def test_empty(self):
        nums = []
        val = 1
        result = Solution.removeElement(nums, val)
        self.assertEqual(result, 0)
        self.assertEqual(nums[:result], [])

    def test_no_val_in_list(self):
        nums = [1, 2, 3, 4]
        val = 5
        result = Solution.removeElement(nums, val)
        self.assertEqual(result, 4)
        self.assertEqual(nums[:result], [1, 2, 3, 4])

    def test_all_val_in_list(self):
        nums = [7, 7, 7, 7]
        val = 7
        result = Solution.removeElement(nums, val)
        self.assertEqual(result, 0)
        self.assertEqual(nums[:result], [])

    def test_some_val_in_list(self):
        nums = [3, 2, 2, 3]
        val = 3
        result = Solution.removeElement(nums, val)
        self.assertEqual(result, 2)
        self.assertTrue(all(x != val for x in nums[:result]))
        self.assertCountEqual(nums[:result], [2, 2])

    def test_val_at_start(self):
        nums = [4, 1, 2, 3]
        val = 4
        result = Solution.removeElement(nums, val)
        self.assertEqual(result, 3)
        self.assertTrue(all(x != val for x in nums[:result]))

    def test_val_at_end(self):
        nums = [1, 2, 3, 4]
        val = 4
        result = Solution.removeElement(nums, val)
        self.assertEqual(result, 3)
        self.assertTrue(all(x != val for x in nums[:result]))

    def test_alternating_val(self):
        nums = [1, 2, 1, 2, 1, 2]
        val = 1
        result = Solution.removeElement(nums, val)
        self.assertEqual(result, 3)
        self.assertTrue(all(x != val for x in nums[:result]))
        self.assertCountEqual(nums[:result], [2, 2, 2])

    def test_single_element_val(self):
        nums = [5]
        val = 5
        result = Solution.removeElement(nums, val)
        self.assertEqual(result, 0)
        self.assertEqual(nums[:result], [])

    def test_single_element_not_val(self):
        nums = [5]
        val = 1
        result = Solution.removeElement(nums, val)
        self.assertEqual(result, 1)
        self.assertEqual(nums[:result], [5])

    def test_large_list(self):
        nums = [1]*1000 + [2]*1000 + [3]*1000
        val = 2
        result = Solution.removeElement(nums, val)
        self.assertEqual(result, 2000)
        self.assertTrue(all(x != val for x in nums[:result]))
        self.assertCountEqual(nums[:result], [1]*1000 + [3]*1000)

if __name__ == "__main__":
    unittest.main()