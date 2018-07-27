class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val_stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.val_stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
            return
        self.min_stack.append(min(self.min_stack[-1], x))
        return

    def pop(self):
        """
        :rtype: void
        """
        if not self.val_stack:
            return
        self.val_stack.pop()
        self.min_stack.pop()
        return

    def top(self):
        """
        :rtype: int
        """
        if not self.val_stack:
            return
        return self.val_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_stack:
            return
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()