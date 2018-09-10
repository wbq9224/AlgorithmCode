class Solution(object):
    def bfs(self, g, c, q):
        while q:
            cur = q.pop(0)
            cur_c = c[cur]
            for v in g[cur]:
                if c[v] == 0:
                    q.append(v)
                    c[v] = -cur_c
                elif c[v] == cur_c:
                    return False
        return True


    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if not dislikes:
            return True

        color = [0 for i in range(N)]
        graph = [[] for i in range(N)]

        for dislike in dislikes:
            u, v = dislike[0] - 1, dislike[1] - 1
            graph[u].append(v)
            graph[v].append(u)

        for i in range(N):
            if color[i] == 0:
                queue = [i]
                color[i] = 1
                if not self.bfs(graph, color, queue):
                    return False
        return True


if __name__ == '__main__':
    N = 5
    dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    print(Solution().possibleBipartition(N, dislikes))