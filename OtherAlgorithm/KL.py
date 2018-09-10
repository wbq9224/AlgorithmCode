import math

if __name__ == '__main__':
    p = input()
    q = input()

    if p and q:
        p, q = list(map(int, p.split())), list(map(int, q.split()))
        np, nq = len(p), len(q)
        ele = set(p + q)

        px = [1e-8 + float(p.count(i)) / np for i in ele]
        qx = [1e-8 + float(q.count(i)) / nq for i in ele]

        kl_dis = 0.00
        for i in range(len(px)):
            kl_dis += px[i] * math.log2(px[i] / qx[i])

        print("%.2f" % kl_dis)