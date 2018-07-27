class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        king_count = numbers.count(0)
        if len(numbers[king_count:]) != len(set(numbers[king_count:])):
            return False
        return numbers[-1] - king_count - numbers[king_count] < len(numbers[king_count:])
    

if __name__ == '__main__':
    num = [1,3,2,6,4]
    print(Solution().IsContinuous(num))