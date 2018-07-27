def reverse(s):
    return " ".join(s.split(" ")[::-1])


def left_rotate_string(s, k):
    return (s[:k][::-1] + s[k:][::-1])[::-1]


if __name__ == '__main__':
    string = "I am a student."
    print(reverse(string))

    string2 = "abcdefgh"
    print(left_rotate_string(string2, 2))