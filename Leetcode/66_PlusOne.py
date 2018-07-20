class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits is None:
            return

        length = len(digits)
        for i in range(length - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)

        return digits


if __name__ == '__main__':
    num = [4,3,2,1]
    # num = [9, 9, 9, 9]
    print(Solution().plusOne(num))