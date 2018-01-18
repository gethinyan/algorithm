class Solution:
    """
    @param: n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber1(self, n):
        # write your code here
        if n < 1:
            return
        if n == 1:
            return 1
        i = 2
        k = 1
        while True:
            j = i
            while j > 1:
                if j % 2 == 0:
                    j /= 2
                elif j % 3 == 0:
                    j /= 3
                elif j % 5 == 0:
                    j /= 5
                else:
                    break
            if j == 1:
                k += 1
            if k == n:
                return i
            i += 1

    def nthUglyNumber(self, n):
        # write your code here
        if n < 1:
            return
        if n == 1:
            return 1
        num2 = 0
        num3 = 0
        num5 = 0
        i = 1
        uglyNum = [1]
        while i < n:
            print(uglyNum[num2])
            uglyNum.append(min(uglyNum[num2] * 2, uglyNum[num3] * 3, uglyNum[num5] * 5))
            if uglyNum[i] == uglyNum[num2] * 2:
                num2 += 1
            if uglyNum[i] == uglyNum[num3] * 3:
                num3 += 1
            if uglyNum[i] == uglyNum[num5] * 5:
                num5 += 1
            i += 1

        return uglyNum[i - 1]


obj = Solution()
print(obj.nthUglyNumber(599))
