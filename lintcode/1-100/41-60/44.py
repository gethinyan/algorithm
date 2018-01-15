class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

    def minSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return
        minSum = nums[0]
        curSum = 0
        for num in nums:
            curSum += num
            if curSum < minSum:
                minSum = curSum
            if curSum > 0:
                curSum = 0

        return minSum


obj = Solution()
print(obj.minSubArray([1, -1, -2, 1]))
