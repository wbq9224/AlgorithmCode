class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        if not words or not pattern:
            return []

        res = []
        for word in words:
            hash_map_a, hash_map_b = {}, {}
            flag = True
            for i, ch in enumerate(word):
                if hash_map_a.get(pattern[i], '') == '':
                    hash_map_a[pattern[i]] = ch
                elif hash_map_a[pattern[i]] != ch:
                    flag = False
                    break
                if hash_map_b.get(ch, '') == '':
                    hash_map_b[ch] = pattern[i]
                elif hash_map_b[ch] != pattern[i]:
                    flag = False
                    break
            if flag:
                res.append(word)
        return res


if __name__ == '__main__':
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    print(Solution().findAndReplacePattern(words, pattern))