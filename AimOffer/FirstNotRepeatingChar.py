if __name__ == '__main__':
    strs = "google"

    # hash法，空间换时间
    d = {}
    for s in strs:
        d[s] = d.get(s, 0) + 1
    for s in strs:
        if d[s] == 1:
            print(s)
            break

    # 若字符串中限定了只出现小写字母的话，也可有另种做法，参考leetcode 387

