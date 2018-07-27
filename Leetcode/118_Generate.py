class Solution(object):
    def generator(self, numRows):
        res = [1]
        while len(res) - 1 < numRows:
            yield res
            res = [1] + [res[i] + res[i + 1] for i in range(len(res) - 1)] + [1]

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []

        res = [row for row in self.generator(numRows)]
        return res


if __name__ == '__main__':
    print(Solution().generate(5))