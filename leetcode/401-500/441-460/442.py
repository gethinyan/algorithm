class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(nums[abs(num) - 1]))
            else:
                nums[abs(num) - 1] *= -1
        return result


def main():
    obj = Solution()
    print(obj.findDuplicates([1, 2, 3, 4, 2, 5, 4]))


if __name__ == '__main__':
    main()
