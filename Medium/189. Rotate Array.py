class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums = [nums.insert(0, nums.pop()) for i in range(0,k)]


x = Solution()

nums = [1,2,3,4,5,6,7]
k = 3
x.rotate(nums, k)
print(nums)
# Note: this solution has a problem at the 37th testcase on leetcode.
# https://leetcode.com/submissions/detail/831339192/




# Second solution
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # private function to reverse a list of numbers
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        n = len(nums)
        k %= n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)