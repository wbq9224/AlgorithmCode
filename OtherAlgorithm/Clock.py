import sys


def clock(time):
    if not time:
        return ""

    time_split = time.split(':')

    if int(time_split[0]) > 23 or int(time_split[0]) < 0:
        time_split[0] = '0' + time_split[0][-1]

    if int(time_split[1]) > 59 or int(time_split[1]) < 0:
        time_split[1] = '0' + time_split[1][-1]

    if int(time_split[2]) > 59 or int(time_split[2]) < 0:
        time_split[2] = '0' + time_split[2][-1]

    return ':'.join(time_split)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        time = sys.stdin.readline().strip()
        print(clock(time))