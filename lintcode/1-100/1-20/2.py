class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        if n is None:
            return 0
        zerosSum = 0
        while n // 5 > 0:
            zerosSum += n // 5
            n = n // 5

        return zerosSum


obj = Solution()
print(obj.trailingZeros(105))
