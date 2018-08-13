# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.hash_map = {i: -1 for i in range(256)}
        self.index = 0

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        min_index, min_index_ch_ascii = 99999, -1
        for i in range(256):
            if min_index >= self.hash_map[i] >= 0:
                min_index = self.hash_map[i]
                min_index_ch_ascii = i
        return chr(min_index_ch_ascii) if min_index != 99999 else '#'

    def Insert(self, char):
        # write code here
        if not char:
            return
        if self.hash_map[ord(char)] == -1:
            self.hash_map[ord(char)] = self.index
        elif self.hash_map[ord(char)] >= 0:
            self.hash_map[ord(char)] = -2
        self.index += 1
        return


if __name__ == '__main__':
    so = Solution()
    str = "google"
    for ch in str:
        so.Insert(ch)
        print(so.FirstAppearingOnce())
