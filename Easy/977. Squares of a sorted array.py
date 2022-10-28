class Solution(object):
    #Define a merge sort
    def mergeSort(self, list):
        if len(list) > 1:
            mid = len(list) // 2
            left = list[:mid]
            right = list[mid:]

            #Recursive call for left and right side
            self.mergeSort(left)
            self.mergeSort(right)

            #Iterator for left and right
            l = 0
            r = 0

            #Main iterator
            m = 0

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    list[m] = left[l]
                    l += 1
                else:
                    list[m] = right[r]
                    r += 1
                m += 1

            while l < len(left):
                list[m] = left[l]
                l += 1
                m += 1

            while r < len(right):
                list[m] = right[r]
                r += 1
                m += 1

    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums = [i ** 2 for i in nums]

        self.mergeSort(nums)

        return nums


