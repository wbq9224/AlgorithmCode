class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None or nums2 is None or len(nums1) == 0 or len(nums2) == 0:
            return []

        # 方法一：利用排序后数组对齐，然后双指针同时向后探测保持对齐，将相同元素加入到并集
        # length1 = len(nums1)
        # length2 = len(nums2)

        # s_nums1 = sorted(nums1)
        # s_nums2 = sorted(nums2)
        #
        # i = j = 0
        # intersect = []
        # while i < length1 and j < length2:
        #     if s_nums1[i] == s_nums2[j]:
        #         intersect.append(s_nums1[i])
        #         i += 1
        #         j += 1
        #     elif s_nums1[i] > s_nums2[j]:
        #         j += 1
        #     elif s_nums1[i] < s_nums2[j]:
        #         i += 1

        # 方法二：利用hash存入nums1每一元素的出现次数，再遍历nums2在hash中看是否存在相同元素
        dict = {}
        intersect = []
        for num in nums1:
            dict[num] = dict.get(num, 0) + 1
        for num in nums2:
            if dict.get(num, 0) > 0:
                intersect.append(num)
                dict[num] -= 1

        return intersect


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    Solution().intersect(nums1, nums2)