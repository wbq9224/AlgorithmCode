class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        """
        We decode the string and N keeps the length of decoded string, until N >= K.
        Then we go back from the decoding position.
        If it's S[i] = d is a digit, then N = N / d before repeat and K = K % N is what we want.
        If it's S[i] = c is a character, we return c if K == 0 or K == N
        """

        if not S or not K:
            return ""

        n = 0
        for i, ch in enumerate(S):
            n = n * int(ch) if ch.isdigit() else n + 1
            if K <= n:
                break

        for j in range(i, -1, -1):
            ch = S[j]
            if ch.isdigit():
                n /= int(ch)
                K %= n
            else:
                if K == n or K == 0:
                    return ch
                n -= 1
        return


if __name__ == '__main__':
    S = "leet2code3"
    K = 10
    print(Solution().decodeAtIndex(S, K))