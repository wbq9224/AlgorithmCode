class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []

        return [
            'FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else str(
                num) for num in range(1, n + 1)]