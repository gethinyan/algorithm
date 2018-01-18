class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        # write your code here
        if k is None or n is None:
            return 0
        if k == 0 and n < 10:
            return 1
        tmp = n
        count = 0
        thePow = 1
        while tmp > 0:
            digit = tmp % 10
            if digit < k:
                count += (tmp // 10) * thePow
            elif digit == k:
                count += (tmp // 10) * thePow + (n - tmp * thePow + 1)
            elif not (k == 0 and tmp // 10 == 0):
                count += (tmp // 10 + 1) * thePow
            tmp //= 10
            thePow *= 10

        return count


obj = Solution()
print(obj.digitCounts(0, 9))
