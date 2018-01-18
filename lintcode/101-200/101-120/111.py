class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        lastWay = 1
        thisWay = 1
        for i in range(2, n + 1):
            lastWay, thisWay = thisWay, lastWay + thisWay

        return thisWay


obj = Solution()
print(obj.climbStairs(10))
