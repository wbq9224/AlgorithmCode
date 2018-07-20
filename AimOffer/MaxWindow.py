class StackWithMax:
    def __init__(self):
        self.data = []
        self.max = []

    def __len__(self):
        return len(self.data)

    def push(self, value):
        self.data.append(value)
        if len(self.max) == 0 or value > self.max[len(self.max) - 1]:
            self.max.append(value)
        else:
            self.max.append(self.max[len(self.max) - 1])

    def pop(self):
        if len(self.data) == 0:
            raise IndexError('当前栈为空，无法执行pop操作')
        ele = self.data.pop()
        self.max.pop()
        return ele

    def get_max(self):
        if len(self.data) == 0:
            raise IndexError('当前栈为空，无法执行max操作')
        return self.max[len(self.max) - 1]


class QueueWithMax:
    def __init__(self):
        self.stack1 = StackWithMax()
        self.stack2 = StackWithMax()

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def push(self, value):
        self.stack1.push(value)

    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            raise IndexError('当前队列为空，无法执行pop操作')
        if len(self.stack2) == 0:
            for i in range(len(self.stack1)):
                ele = self.stack1.pop()
                self.stack2.push(ele)
        return self.stack2.pop()

    def get_max(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            raise IndexError('当前队列为空，无法执行max操作')
        if len(self.stack1) == 0:
            max = self.stack2.get_max()
        elif len(self.stack2) == 0:
            max = self.stack1.get_max()
        else:
            m1 = self.stack1.get_max()
            m2 = self.stack2.get_max()
            if m1 > m2:
                max = m1
            else:
                max = m2
        return max


if __name__ == '__main__':
    num = [10, 14, 12, 11]
    k = 1

    max = []

    queue = QueueWithMax()
    for i in range(len(num)):
        queue.push(num[i])
        if len(queue) == k:
            max.append(queue.get_max())
            queue.pop()

    print(max)




