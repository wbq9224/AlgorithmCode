if __name__ == '__main__':
    n = 1500

    ugly_list = [1]
    u2 = u3 = u5 = 0
    while len(ugly_list) < n:
        ugly_list.append(min([ugly_list[u2] * 2, ugly_list[u3] * 3, ugly_list[u5] * 5]))

        if ugly_list[u2] * 2 == ugly_list[-1]:
            u2 += 1
        if ugly_list[u3] * 3 == ugly_list[-1]:
            u3 += 1
        if ugly_list[u5] * 5 == ugly_list[-1]:
            u5 += 1

    print(ugly_list[-1])
