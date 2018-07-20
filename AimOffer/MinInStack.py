class MinInStack:
    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def size(self):
        return len(self.data_stack)

    def push(self, ele):
        size = self.size()
        self.data_stack.append(ele)
        if size == 0:
            self.min_stack.append(ele)
        else:
            temp = self.min_stack[size - 1]
            self.min_stack.append(ele if ele < min else temp)

        return

    def pop(self):
        if self.size() <= 0:
            return
        self.min_stack.pop()
        return self.data_stack.pop()

    def get_min(self):
        if self.size() <= 0:
            return
        return self.min_stack[self.size() - 1]


