class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        if not A or not B:
            return []

        sum_a, sum_b = sum(A), sum(B)
        diff = sum_a - (sum_a + sum_b) >> 1

        hash_a = {}
        for ele_a in A:
            hash_a[ele_a - diff] = ele_a

        for ele_b in B:
            if hash_a.get(ele_b, -1) != -1:
                return [hash_a[ele_b], ele_b]


if __name__ == '__main__':
    A = [1, 2, 5]
    B = [2, 4]
    print(Solution().fairCandySwap(A, B))