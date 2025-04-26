def naive_string_matcher(target, pattern):
    n = len(target)
    m = len(pattern)

    for s in range(n - m + 1):
        # print("Current Pattern: " + pattern)
        # print("Current Target: " + target[s:s + m])
        if pattern == target[s:s + m]:
            return True

    return False


