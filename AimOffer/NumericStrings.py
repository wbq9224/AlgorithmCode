class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False

        if s[0] == '+' or s[0] == '-':
            s = s[1:]
            if not s:
                return False

        is_sci = False
        is_decimal = False
        for i, ch in enumerate(s):
            if ch == '.':
                if is_sci or is_decimal:
                    return False
                is_decimal = True
            elif ch == 'e' or ch == 'E':
                if is_sci or i == 0 or i == len(s) - 1:
                    return False
                is_sci = True
            elif ch == '-' or ch == '+':
                if (i == 0 or i == len(s) - 1) or (s[i - 1] != 'e' and s[i - 1] != 'E'):
                    return False
            elif ord(ch) < ord('0') or ord(ch) > ord('9'):
                return False
        return True



if __name__ == '__main__':
    number = "123.45e+6"
    print(Solution().isNumeric(number))
