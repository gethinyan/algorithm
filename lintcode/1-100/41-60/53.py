# -*- coding: utf-8 -*-
class Solution:
    """
    @param: s: A string
    @return: A string
    """

    def reverseWords(self, s):
        # write your code here
        if s is None or s == '':
            return s
        sLen = len(s)
        start = sLen - 1
        end = sLen - 1
        flag = False
        result = ''
        while start >= 0:
            if s[start] != ' ' and flag is False:
                flag = True
                end = start
            elif s[start] == ' ' and flag is True:
                for i in range(start, end + 1):
                    if s[i] != ' ':
                        result += s[i]
                result += ' '
                flag = False
                end = start
            elif start == 0 and flag is True:
                for i in range(start, end + 1):
                    if s[i] != ' ':
                        result += s[i]
                break
            elif s[start] == ' ' and flag is False:
                start -= 1
                end -= 1
            else:
                start -= 1

        return result


obj = Solution()
print(obj.reverseWords('a b sd'))
