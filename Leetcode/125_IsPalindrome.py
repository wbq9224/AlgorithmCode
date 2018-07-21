class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        if len(s) == 0 or len(s) == 1:
            return True

        # 注意两个api：isalnum-检测是否为字母和数字构成， s.lower-将字符串中所有大写字母转换为小写
        temp = list(filter(lambda x: x.isalnum(), s.lower()))
        length = len(temp)

        for i in range(length >> 1):
            if temp[i] != temp[length - i - 1]:
                return False

        return True


if __name__ == '__main__':
    str = "A man, a plan, a canal: Panama"
    # str = "0P"
    print(Solution().isPalindrome(str))