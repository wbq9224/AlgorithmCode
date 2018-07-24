from functools import *


def comp(s1, s2):
    return 1 if s1 + s2 > s2 + s1 else -1


if __name__ == '__main__':
    num = [3, 32, 321]

    num_to_str = list(map(str, num))
    num_to_str.sort(key=cmp_to_key(comp))

    print(str(int("".join(num_to_str))))