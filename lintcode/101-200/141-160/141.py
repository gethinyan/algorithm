class Solution:
    """
    @param: x: An integer
    @return: The sqrt of x
    """

    def sqrt1(self, x):
        # write your code here
        if x == 0:
            return 0
        for i in range(1, x + 1):
            if x // i >= i and x // (i + 1) < (i + 1):
                return i

    def sqrt(self, x):
        # write your code here
        if x == 0 or x == 1:
            return x
        low = 0
        high = x
        while low + 1 < high:
            mid = (low + high) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                high = mid
            else:
                low = mid
        if x // low >= low and x // (mid + 1) < mid + 1:
            return low

        return mid


obj = Solution()
print(obj.sqrt(99999999))
