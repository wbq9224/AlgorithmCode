import sys


if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        talks = sys.stdin.readline().strip().split()
        stack = []
        for talk in talks:
            if talk not in stack:
                stack.append(talk)
            else:
                stack.remove(talk)
                stack.append(talk)
        for talk in stack[1:]:
            print(stack.pop(), end=' ')
        print(stack[-1])