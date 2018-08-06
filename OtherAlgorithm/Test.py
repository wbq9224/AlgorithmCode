import sys


def find_key_word(char_map, key_word):
    if not char_map:
        return 0
    m, n = len(char_map), len(char_map[0])

    res, key_word_len = 0, len(key_word)
    for i in range(m):
        for j in range(n - key_word_len + 1):
            if char_map[i][j: j + key_word_len] == key_word:
                res += 1

    trans_map = ["".join(temp) for temp in zip(*char_map)]
    for i in range(n):
        for j in range(m - key_word_len + 1):
            if trans_map[i][j: j + key_word_len] == key_word:
                res += 1

    for i in range(m - key_word_len + 1):
        for j in range(n - key_word_len + 1):
            temp = char_map[i][j]
            for k in range(1, key_word_len):
                temp += char_map[i + k][j + k]
            if temp == key_word:
                res += 1
    return res


t = int(sys.stdin.readline().strip())
for i in range(t):
    m, n = map(int, sys.stdin.readline().strip().split())
    char_map = [sys.stdin.readline().strip() for j in range(m)]
    key_word = sys.stdin.readline().strip()
    print(find_key_word(char_map, key_word))