class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        if not A or not B:
            return []
        hash_map = {}
        for word in (A + ' ' + B).split():
            hash_map[word] = hash_map.get(word, 0) + 1

        res = [word for word in (A + ' ' + B).split() if hash_map[word] == 1]

        return res


if __name__ == '__main__':
    A = "this apple is sweet"
    B = "this apple is sour"
    print(Solution().uncommonFromSentences(A, B))