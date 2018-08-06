class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if not people or not limit:
            return 0

        res = 0
        people.sort()

        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            res += 1
            right -= 1

        return res


if __name__ == '__main__':
    people = [3, 5, 3, 4]
    limit = 5
    print(Solution().numRescueBoats(people, limit))