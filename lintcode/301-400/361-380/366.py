class Solution:
    """
    @param: n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # write your code here
        firstNum = 0
        secondNum = 1
        for index in range(n - 1):
            secondNum = firstNum + secondNum
            firstNum = secondNum - firstNum
        return firstNum


obj = Solution()
print(obj.fibonacci(5))
