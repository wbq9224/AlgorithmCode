class Stack:
    def __init__(self):
        self.data = []
        self.top = len(self.data)

    def push(self, value):
        self.data.append(value)
        self.top = len(self.data)

    def pop(self):
        if self.top == 0:
            print('stack is empty')
            return

        ele = self.data.pop()
        self.top = len(self.data)

        return ele

    def get_size(self):
        return self.top


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def append_tail(self, value):
        self.stack1.push(value)

    def delete_head(self):
        if self.stack1.get_size() == 0 and self.stack2.get_size() == 0:
            return

        if self.stack2.get_size() == 0:
            for i in range(self.stack1.get_size()):
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.stack1.get_size() == 0 and self.stack2.get_size() == 0:
            return

        if self.stack2.get_size() == 0:
            for i in range(self.stack1.get_size()):
                self.stack2.push(self.stack1.pop())
        return self.stack2[self.stack2.get_size() - 1]

    def get_size(self):
        return self.stack1.get_size() + self.stack2.get_size()


if __name__ == '__main__':
    queue = Queue()
    for i in range(10):
        queue.append_tail(i * 10)

    for i in range(5):
        print(queue.delete_head())