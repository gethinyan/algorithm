class Solution:
    """
    @param: s: a string
    @return: it's index
    """

    def firstUniqChar(self, s):
        # write your code here
        if s == '':
            return -1
        for i in range(len(s)):
            flag = True
            for j in range(len(s)):
                if s[i] == s[j] and i != j:
                    flag = False
                    break
            if flag is True:
                break
            elif i == len(s) - 1:
                return -1

        return i


obj = Solution()
print(obj.firstUniqChar('lovelintcode'))
