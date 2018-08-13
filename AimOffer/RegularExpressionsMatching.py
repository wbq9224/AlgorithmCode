def match(s, pattern):
    if s is None or pattern is None:
        return False
    return match_core(s, pattern)


def match_core(s, pattern):
    # 若主串与模式串同时为空，则认为匹配成功
    if not s and not pattern:
        return True
    # 若主串非空而模式串已空，则匹配失败
    if not pattern and s:
        return False
    # 注意主串空而模式串非空是有可能匹配成功的

    # 处理*
    if len(pattern) > 1 and pattern[1] == '*':
        # 若当前匹配，则有可能是匹配一个或多个
        # 若匹配一个，则将模式串后移两位跳过*，主串后移一位
        # 若匹配多个，则将主串后移一位，模式串不动，移动后若失配，则认为多个匹配完毕，模式串后移两位跳过*，主串不动
        # 三种情况取或，只要有一种匹配成功即认为匹配成功
        if (s and s[0] == pattern[0]) or (s and pattern[0] == '.'):
            return match_core(s[1:], pattern[2:]) or match_core(s[1:], pattern) or match_core(s, pattern[2:])
        # 若当前不匹配，则认为是匹配了0个（也算是匹配），将模式串后移两位跳过*，主串不动
        else:
            return match_core(s, pattern[2:])

    # 处理相等或.：直接逐个比较即可
    if (s and s[0] == pattern[0]) or (s and pattern[0] == '.'):
        return match_core(s[1:], pattern[1:])

    return False


if __name__ == '__main__':
    s = "a"
    pattern_s = ".*"
    print(match(s, pattern_s))