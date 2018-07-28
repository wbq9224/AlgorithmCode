class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # 本题思路：将每一个词变为字符数组，将字符数组排序再转为字符串，用此字符串作为key建立哈希表
        # 则哈希表结构为[key(string), value(list)]
        # 取出哈希表的所有分组即可

        if not strs:
            return []

        d = {}
        for word in strs:
            key = "".join(sorted(word))
            d[key] = d.get(key, [])
            d[key].append(word)

        return [d[key] for key in d]


if __name__ == '__main__':
    string = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(string))


