class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        left = {'(', '[', '{'}
        right = {')', ']', '}'}
        match = {')': '(', ']': '[', '}': '{'}

        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if not stack or stack.pop() != match[c]:
                    return False
        if stack:
            return False
        return True


if __name__ == '__main__':
    print(Solution().isValid("()"))