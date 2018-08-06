import sys
import copy

def dijkstra(graph, begin):
    if graph is None or begin is None or begin > len(graph) - 1:
        return

    # 初始化
    v = len(graph)

    set = [0 for i in range(v)]
    set[begin] = 1

    path = []
    for i in range(v):
        if graph[begin][i] != MAX:
            path.append(begin)
        else:
            path.append(-1)

    dist = [graph[begin][i] for i in range(v)]
    dist[begin] = 0

    # 遍历
    for i in range(v):
        min = MAX
        min_index = -1
        for index, d in enumerate(dist):
            if set[index] == 0 and min > d:
                min = d
                min_index = index
        set[min_index] = 1

        for j in range(v):
            if set[j] == 0:
                temp = dist[min_index] + graph[min_index][j]
                if temp < dist[j]:
                    dist[j] = temp
                    path[j] = min_index

    return path, dist


def floyed(graph):
    if graph is None:
        return

    v = len(graph)
    # 初始化
    a = copy.deepcopy(graph)
    path = [[-1 for j in range(v)] for i in range(v)]
    # 遍历
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    path[i][j] = k

    return path, a


def print_path(path, e):
    if path[e] != -1:
        print_path(path, path[e])
    print(e, end=' ')
    return


if __name__ == '__main__':
    MAX = sys.maxsize
    g = [
        [MAX, 4, 6, 6, MAX, MAX, MAX],
        [MAX, MAX, 1, MAX, 7, MAX, MAX],
        [MAX, MAX, MAX, MAX, 6, 4, MAX],
        [MAX, MAX, 2, MAX, MAX, 5, MAX],
        [MAX, MAX, MAX, MAX, MAX, MAX, 6],
        [MAX, MAX, MAX, MAX, 1, MAX, 8],
        [MAX, MAX, MAX, MAX, MAX, MAX, MAX]
    ]
    g1 = [
        [0, 5, MAX, 7],
        [MAX, 0, 4, 2],
        [3, 3, 0, 2],
        [MAX, MAX, 1, 0]
    ]

    # start = 0
    # end = 6
    #
    # paths, dists = dijkstra(g, start)
    # print(dists[end])
    # print_path(paths, end)

    # p, a = floyed(g)
    # print(a)
    # print(p)

