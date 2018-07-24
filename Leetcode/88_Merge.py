class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 and not nums2 or m + n < len(nums1):
            return

        # 方法一：正向顺序合并，直接思路
        # i = j = k = 0
        # temp = nums1[:]
        # while i < m and j < n:
        #     if nums1[i] < nums2[j]:
        #         temp[k] = nums1[i]
        #         i += 1
        #     else:
        #         temp[k] = nums2[j]
        #         j += 1
        #     k += 1
        # if i < m:
        #     temp[k:] = nums1[i: m]
        # if j < n:
        #     temp[k:] = nums2[j:]
        # nums1[:] = temp

        # 方法二：倒序合并
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[: n] = nums2[:n]
        return


if __name__ == '__main__':
    nums1 = [15,20,0,0,0,0,0]
    m = 2
    nums2 = [3,6,9,11,13]
    n = 5
    Solution().merge(nums1, m, nums2, n)
    print(nums1)