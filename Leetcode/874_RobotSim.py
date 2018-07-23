class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        if not commands or obstacles is None:
            return 0

        # 纯模拟-目前超时
        res = x = y = 0
        dir_x = 0
        dir_y = 1

        for i in range(len(commands)):
            if commands[i] < 0:  # 处理转向
                if dir_x == 0 and commands[i] == -2:
                    dir_y = - dir_y  # y方向的左右转向：左转反号，右转不变
                elif dir_y == 0 and commands[i] == -1:
                    dir_x = - dir_x  # x方向的左右转向：右转反号，左转不变
                dir_x = dir_x ^ dir_y  # 交换
                dir_y = dir_x ^ dir_y
                dir_x = dir_x ^ dir_y
            elif commands[i] > 0:  # 处理前进
                new_x = x + commands[i] * dir_x
                new_y = y + commands[i] * dir_y
                for c in obstacles:  # 处理障碍
                    if dir_x != 0 and c[1] == new_y and dir_x * x < dir_x * c[0] <= dir_x * new_x:
                        new_x = c[0] - 1 * dir_x
                    if dir_y != 0 and c[0] == new_x and dir_y * y < dir_y * c[1] <= dir_y * new_y:
                        new_y = c[1] - 1 * dir_y
                x = new_x
                y = new_y
                res = max(res, x ** 2 + y ** 2)
        return res


if __name__ == '__main__':
    commands = [7,-2,-2,7,5]
    obstacles = [[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]]
    # commands = [4, -1, 3]
    # obstacles = []
    # commands = [4, -1, 4, -2, 4]
    # obstacles = [[2, 4]]
    print(Solution().robotSim(commands, obstacles))