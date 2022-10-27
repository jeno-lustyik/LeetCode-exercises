class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums) - 1

        while start <= end:

            middle = (start + end) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1

        return start