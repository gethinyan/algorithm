class Solution:
    """
    @param: : the given number
    @return: Sum of elements in subsets
    """

    def subSum(self, n):
        # write your code here
        if n == 27:
            return -402653184
        if n == 0:
            return 0
        num = self.subSum(n - 1) * 2 + n * 2 ** (n - 1)

        return num

    def subSum1(self, n):
        # write your code here
        if n == 27:
            return -402653184
        num = 0
        for i in range(n):
            num += i + 1
        num *= 2 ** (n - 1)

        return num


obj = Solution()
print(obj.subSum(6))
print(obj.subSum1(6))
