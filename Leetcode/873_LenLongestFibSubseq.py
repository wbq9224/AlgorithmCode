class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) < 3:
            return 0

        d = {}
        res = 0
        for num in A:
            d[num] = d.get(num, 0) + 1
        for i, num in enumerate(A):
            for j in range(i + 1, len(A) - 1):
                temp = [num]
                if d.get(temp[-1] + A[j]) == 1:
                    temp.append(A[j])
                    temp.append(temp[-2] + temp[-1])
                    while d.get(temp[-2] + temp[-1], 0) == 1:
                        temp.append(temp[-2] + temp[-1])
                    res = max(len(temp), res)
        return res


if __name__ == '__main__':
    # nums = [1,2,3,4,5,6,7,8]
    # nums = [1, 3, 7, 11, 12, 14, 18]
    nums = [2,4,7,8,9,10,14,15,18,23,32,50]
    print(Solution().lenLongestFibSubseq(nums))