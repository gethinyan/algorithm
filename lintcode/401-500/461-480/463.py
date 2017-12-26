# 选择排序
class Solution:
    """
    @param: A: an integer array
    @return:
    """

    def sortIntegers(self, A):
        # write your code here
        lenA = len(A)
        for i in range(lenA):
            for j in range(i, lenA):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
        return A


# 冒泡排序
class Solution1:
    """
    @param: A: an integer array
    @return:
    """

    def sortIntegers(self, A):
        # write your code here
        lenA = len(A)
        while lenA > 0:
            for i in range(lenA - 1):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
            lenA -= 1
        return A


# 插入排序
class Solution2:
    """
    @param: A: an integer array
    @return:
    """

    def sortIntegers(self, A):
        # write your code here
        lenA = len(A)
        for i in range(1, lenA):
            j = i
            while j > 0 and A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                j -= 1
        return A


# 快速排序
def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j - 1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i + 1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i - 1)
    quickSort(L, j + 1, high)
    return L


class Solution3:
    """
    @param: A: an integer array
    @return:
    """

    def sortIntegers(self, A):
        # write your code here
        return quickSort(A, 0, len(A) - 1)


obj = Solution3()
print(obj.sortIntegers([3, 2, 1, 4, 5]))
