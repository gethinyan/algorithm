class Solution:
    """
    @param: s: a string
    @return: it's index
    """

    def firstUniqChar2(self, s):
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

    def firstUniqChar(self, s):
        # write your code here
        if s == '':
            return -1
        tmpDic = {}
        for i in range(len(s)):
            if s[i] in tmpDic:
                tmpDic[s[i]] += 1
            else:
                tmpDic[s[i]] = 1
        for j in range(len(s)):
            if tmpDic[s[j]] == 1:
                return j

        return -1


obj = Solution()
print(obj.firstUniqChar('lintcode'))
