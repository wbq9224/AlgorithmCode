class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None:
            return False

        list_length = len(nums)
        set_length = len(set(nums))

        return set_length != list_length


if __name__ == '__main__':
    a = [1,2,3,1]

    so = Solution()
    print(so.containsDuplicate(a))
