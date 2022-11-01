class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        for i in range(k, len(nums)):
            nums[i] = 0
        return
