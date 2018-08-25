class Solution:
    def __init__(self):
        self.nums = []

    def Insert(self, num):
        # write code here
        if num is not None:
            if self.nums:
                for i in range(len(self.nums)):
                    if self.nums[i] > num:
                        break
                self.nums.insert(i, num)
            else:
                self.nums.append(num)
        return

    def GetMedian(self):
        # write code here
        if not self.nums:
            return
        mid = len(self.nums) >> 1
        if len(self.nums) & 1 != 0:
            return self.nums[mid] / 1.00
        return (self.nums[mid - 1] + self.nums[mid]) / 2.00


if __name__ == '__main__':
    number = [5,2,3,4,1,6,7,0,8]
    so = Solution()
    for ele in number:
        so.Insert(ele)
        print(so.GetMedian())