class Solution:
    """
    @param: nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray2(self, nums):
        # write your code here
        if nums is None:
            return
        numsLen = len(nums)
        index = 0
        result = []
        for i in range(numsLen - 1):
            if nums[i] > nums[i + 1]:
                index = i + 1
                break
        if index == 0:
            return nums
        for j in range(numsLen):
            if j + index < numsLen:
                result.append(nums[j + index])
            else:
                result.append(nums[j + index - numsLen])

        return result

    def recoverRotatedSortedArray1(self, nums):
        # write your code here
        if nums is None:
            return
        low = 0
        high = len(nums) - 1
        while nums[low] > nums[high]:
            nums.append(nums[low])
            low += 1
            high += 1

        return nums[low:high + 1]

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums is None:
            return
        numsLen = len(nums)
        index = 0
        for i in range(numsLen - 1):
            if nums[i] > nums[i + 1]:
                index = i + 1
                break
        if index == 0:
            return nums
        for j in range(index // 2):
            nums[j], nums[index - j - 1] = nums[index - j - 1], nums[j]
        for k in range((numsLen - index) // 2):
            nums[index + k], nums[numsLen - k - 1] = nums[numsLen - k - 1], nums[index + k]
        for l in range(numsLen // 2):
            nums[l], nums[numsLen - l - 1] = nums[numsLen - l - 1], nums[l]

        return nums


obj = Solution()
print(obj.recoverRotatedSortedArray([4, 5, 1, 2, 3]))
print(obj.recoverRotatedSortedArray1([4, 5, 1, 2, 3]))
print(obj.recoverRotatedSortedArray2([4, 5, 1, 2, 3]))
print(obj.recoverRotatedSortedArray([1, 2, 3, 4, 5, 6]))
print(obj.recoverRotatedSortedArray1([1, 2, 3, 4, 5, 6]))
print(obj.recoverRotatedSortedArray2([1, 2, 3, 4, 5, 6]))
