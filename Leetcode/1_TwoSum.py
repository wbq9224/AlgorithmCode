def travl(root, sorted_num):
    if root is None:
        return
    if root.left is not None:
        travl(root.left, sorted_num)
    sorted_num.append(root.val)
    if root.right is not None:
        travl(root.right, sorted_num)
    return


class Solution(object):
    # input unorder list
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if nums is None or target is None:
            return []
        length = len(nums)
        if length < 2:
            return []

        # List原生排序并保留原索引的方法
        rvt = sorted(enumerate(nums), key=lambda x: x[1])

        left = 0
        right = length - 1

        while left < right:
            sum = rvt[left][1] + rvt[right][1]
            if sum == target:
                return sorted([rvt[left][0], rvt[right][0]])
            if sum > target:
                right -= 1
            else:
                left += 1

        return []

    # input bst
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        if root is None or k is None:
            return False

        numbers = []
        travl(root, numbers)

        length = len(numbers)
        if length < 2:
            return False

        left = 0
        right = length - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == k:
                return True
            if sum > k:
                right -= 1
            else:
                left += 1

        return False


if __name__ == '__main__':
    a = [7, 2, 15, 11]
    target = 9

    # so = Solution()
    # print(so.twoSum(a, target))
