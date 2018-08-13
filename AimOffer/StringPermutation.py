def permutation(str, begin):
    if str is None:
        return

    if begin == len(str) - 1:
        print("".join(str))
    else:
        for i in range(begin, len(str)):  # 注意此处范围为begin~len（str）-1
            temp = str[i]
            str[i] = str[begin]
            str[begin] = temp

            permutation(str, begin + 1)

            temp = str[i]  # 回溯
            str[i] = str[begin]
            str[begin] = temp


if __name__ == '__main__':
    str = list("aa")

    permutation(str, 0)
