import sys


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    res = []
    for i in range(t):
        n = int(sys.stdin.readline())
        strs = []
        for j in range(n):
            strs.append(sys.stdin.readline().strip())

        begin = strs[0]
        flag = False
        for j in range(1, len(begin) + 1):
            temp = begin[j:] + begin[:j]
            for k in range(1, len(strs)):
                if temp == strs[k] or temp[::-1] == strs[k]:
                    flag = True
                    break
            if flag:
                break
        if flag:
            print('Yeah')
        else:
            print('Sad')