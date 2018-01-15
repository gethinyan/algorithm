class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        low = 0
        high = len(nums) - 1
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid
        if nums[low] == target:
            return low
        if nums[high] == target:
            return high

        return -1


obj = Solution()
print(obj.findPosition([1, 2, 2, 4, 5, 5], 6))
