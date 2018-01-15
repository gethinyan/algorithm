class Solution:
    """
    @param: s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return 0
        tmpDic = {}
        result = 0
        for i in range(len(s)):
            if s[i] in tmpDic:
                tmpDic[s[i]] += 1
            else:
                tmpDic[s[i]] = 1
        print(tmpDic)
        for tmpCount in tmpDic.values():
            if result % 2 == 0 and tmpCount % 2 == 1:
                result += 1
            result += tmpCount // 2 * 2

        return result


obj = Solution()
print(obj.longestPalindrome('abccccdd'))
