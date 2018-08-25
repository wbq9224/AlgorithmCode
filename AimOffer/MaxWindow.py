class StackWithMax:
    def __init__(self):
        self.data_stack = []
        self.max_stack = []

    def __len__(self):
        return len(self.data_stack)

    def push(self, num):
        if num is None:
            return
        self.data_stack.append(num)
        if not self.max_stack or num > self.max_stack[-1]:
            self.max_stack.append(num)
        else:
            self.max_stack.append(self.max_stack[-1])
        return

    def pop(self):
        if not self.data_stack:
            return
        ele = self.data_stack.pop()
        self.max_stack.pop()
        return ele

    def get_max(self):
        if not self.data_stack:
            return
        return self.max_stack[-1]


class QueueWithMax:
    def __init__(self):
        self.stack1 = StackWithMax()
        self.stack2 = StackWithMax()

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def push(self, num):
        self.stack1.push(num)
        return

    def pop(self):
        if not self.stack1 and not self.stack2:
            return
        if self.stack2:
            self.stack2.pop()
            return
        while self.stack1:
            self.stack2.push(self.stack1.pop())
        self.stack2.pop()
        return

    def get_max(self):
        if not self.stack1 and not self.stack2:
            return
        if not self.stack1:
            return self.stack2.get_max()
        if not self.stack2:
            return self.stack1.get_max()
        return max(self.stack1.get_max(), self.stack2.get_max())


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or not size:
            return []
        queue = QueueWithMax()
        res = []
        for ele in num:
            queue.push(ele)
            if len(queue) == size:
                res.append(queue.get_max())
                queue.pop()
        return res


if __name__ == '__main__':
    num = [2,3,4,2,6,2,5,1]
    k = 3

    print(Solution().maxInWindows(num, k))




