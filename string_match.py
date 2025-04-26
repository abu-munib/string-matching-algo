def naive_string_matcher(target, pattern):
    found_at = []
    
    n = len(target)
    m = len(pattern)

    for s in range(n - m + 1):
        # print("Current Pattern: " + pattern)
        # print("Current Target: " + target[s:s + m])
        if pattern == target[s:s + m]:
            found_at.append(s) 

    return found_at

def kmp_preprocessing(pattern):
    lps = [0 for _ in range(len(pattern))]

    l = 0
    for i in range(1, len(pattern)):
        if pattern[l] == pattern[i]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                i += 1

    return lps

def knuth_morris_pratt_matcher(target, pattern):

    lps = kmp_preprocessing(pattern)

    j = 0
    for i in range(len(target)):
        if pattern[j] != target[i]:
            if i == 0:
                i += 1
            else:
                j = lps[j - 1]
        else:
            j += 1
            i += 1

