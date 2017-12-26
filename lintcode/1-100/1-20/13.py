class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        if source == target or target == '':
            return 0
        status = -1
        for i in range(len(source)):
            if source[i] == target[0] and len(source) - i >= len(target):
                status = 1
                for j in range(len(target)):
                    if source[i + j] != target[j]:
                        status = -1
                        break
                if status == 1:
                    status = i
                    break
        return status


obj = Solution()
print(obj.strStr('abcdabcdefg', 'cda'))
